#!/usr/bin/env python3
"""İzin verilen yerel web prototipinde etkileşim adımlarını uygula ve kanıt yakala.

Öntanımlı yalnızca localhost. Yalnızca kullanıcı tarafından hazırlanmış JSON senaryosu;
keyfi JavaScript değerlendirme komutu yok. Playwright + Chromium gerekir.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from evidence_core import EvidenceError, digest, put_json

ALLOWED_ACTIONS = {"click", "fill", "press", "wait_visible", "expect_text", "screenshot", "scroll", "offline", "wait_ms"}
LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1"}


def is_local_url(url: str) -> bool:
    """Return True only for loopback HTTP(S) URLs (also after a redirect)."""
    try:
        parts = urlsplit(url)
    except ValueError:
        return False
    return parts.scheme in {"http", "https"} and parts.hostname in LOCAL_HOSTS



def validate_config(config: dict, allow_remote: bool = False) -> None:
    if not isinstance(config, dict):
        raise EvidenceError("Prototip yapılandırması JSON object olmalı")
    url = config.get("url")
    if not isinstance(url, str):
        raise EvidenceError("url zorunlu")
    try:
        parts = urlsplit(url)
    except ValueError as exc:
        raise EvidenceError("URL geçersiz") from exc
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise EvidenceError("Yalnızca http/https URL kabul edilir")
    if parts.username is not None or parts.password is not None:
        raise EvidenceError("URL içinde giriş bilgisi taşınmamalı")
    if not allow_remote and not is_local_url(url):
        raise EvidenceError("Uzak adrese erişim için açıkça --allow-remote gerekli")
    v = config.get("viewport", {})
    if not isinstance(v, dict) or type(v.get("width")) is not int or type(v.get("height")) is not int:
        raise EvidenceError("viewport {width:int, height:int} gerekli")
    if not (240 <= v["width"] <= 4096 and 320 <= v["height"] <= 4096):
        raise EvidenceError("viewport ölçüleri 240..4096 px sınırlarında olmalı")
    if config.get("reduced_motion", "reduce") not in {"reduce", "no-preference"}:
        raise EvidenceError("reduced_motion değeri reduce veya no-preference olmalı")
    steps = config.get("steps")
    if not isinstance(steps, list) or not steps or len(steps) > 100:
        raise EvidenceError("1..100 etkileşim adımı gerekli")
    for i, step in enumerate(steps):
        if not isinstance(step, dict) or step.get("action") not in ALLOWED_ACTIONS:
            raise EvidenceError(f"{i}. adım için eylem geçersiz")
        if step["action"] in {"click", "fill", "press", "wait_visible", "expect_text"} and not step.get("selector"):
            raise EvidenceError(f"{i}. adım için selector gerekli")
        if step["action"] in {"fill", "press", "expect_text"} and not isinstance(step.get("value"), str):
            raise EvidenceError(f"{i}. adım için value zorunlu")
        if step["action"] == "offline" and not isinstance(step.get("enabled"), bool):
            raise EvidenceError(f"{i}. adım offline.enabled boolean olmalı")
        if step["action"] == "wait_ms" and not (
            type(step.get("value")) is int and 0 <= step["value"] <= 10000
        ):
            raise EvidenceError(f"{i}. adım wait_ms 0..10000 olmalı")
        if step["action"] == "scroll" and not (
            type(step.get("pixels")) is int and abs(step["pixels"]) <= 10000
        ):
            raise EvidenceError(f"{i}. adım scroll.pixels -10000..10000 olmalı")


def capture(config_path: Path, output_dir: Path, *, browser_path: str | None, allow_remote: bool) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise EvidenceError("Playwright yok: pip install playwright; python -m playwright install chromium") from exc
    config = json.loads(config_path.read_text(encoding="utf-8"))
    validate_config(config, allow_remote)
    output_dir.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    failed_actions: list[dict] = []
    screenshots: list[dict] = []
    steps_done: list[dict] = []
    runtime_blocked = False
    try:
        with sync_playwright() as play:
            opts = {"headless": True}
            if browser_path:
                opts["executable_path"] = browser_path
            browser = play.chromium.launch(**opts)
            context_options = {
                "viewport": config["viewport"],
                "device_scale_factor": 1,
                "reduced_motion": config.get("reduced_motion", "reduce"),
                "locale": config.get("locale", "tr-TR"),
            }
            if not allow_remote:
                # Also block remote resources loaded by a local page, not only
                # navigation. Service workers must not bypass request routing.
                context_options["service_workers"] = "block"
            context = browser.new_context(**context_options)
            if not allow_remote:
                context.route("**/*", lambda route: route.continue_()
                              if is_local_url(route.request.url) else route.abort())
            page = context.new_page()
            page.on("pageerror", lambda error: errors.append("pageerror: " + str(error)[:500]))
            page.on("console", lambda message: errors.append("console: " + message.text[:500])
                    if message.type == "error" else None)
            page.on("requestfailed", lambda request: errors.append("requestfailed: " + request.url[:250]))
            try:
                response = page.goto(config["url"], wait_until="domcontentloaded", timeout=20000)
                if not allow_remote and not is_local_url(page.url):
                    raise EvidenceError("Redirect ile uzak adrese geçiş engellendi")
                if response is None or response.status >= 400:
                    errors.append(f"Initial HTTP status: {response.status if response else 'none'}")
                page.wait_for_load_state("load", timeout=15000)
                for i, step in enumerate(config["steps"]):
                    action = step["action"]
                    try:
                        locator = page.locator(step["selector"]) if "selector" in step else None
                        if action == "click":
                            locator.click(timeout=5000)
                        elif action == "fill":
                            locator.fill(step["value"], timeout=5000)
                        elif action == "press":
                            locator.press(step["value"], timeout=5000)
                        elif action == "wait_visible":
                            locator.wait_for(state="visible", timeout=5000)
                        elif action == "expect_text":
                            locator.wait_for(state="visible", timeout=5000)
                            actual = locator.inner_text(timeout=5000)
                            if step["value"] not in actual:
                                raise EvidenceError(f"Beklenen metin yok: {step['value']!r}")
                        elif action == "scroll":
                            page.mouse.wheel(0, step["pixels"])
                        elif action == "offline":
                            context.set_offline(step["enabled"])
                        elif action == "wait_ms":
                            page.wait_for_timeout(step["value"])
                        elif action == "screenshot":
                            filename = f"step_{i + 1:03d}.png"
                            location = output_dir / filename
                            page.screenshot(path=str(location), full_page=False, animations="disabled")
                            screenshots.append({"step": i + 1, "path": str(location), "sha256": digest(location)})
                        steps_done.append({"step": i + 1, "action": action, "status": "passed"})
                    except Exception as exc:
                        failed_actions.append({"step": i + 1, "action": action, "error": str(exc)[:600]})
                        # Fail fast: subsequent steps cannot be trusted as the intended state.
                        break
                final_path = output_dir / "final.png"
                page.screenshot(path=str(final_path), full_page=False, animations="disabled")
                screenshots.append({"step": "final", "path": str(final_path), "sha256": digest(final_path)})
            finally:
                context.close()
                browser.close()
    except Exception as exc:
        runtime_blocked = True
        errors.append("browser/ortam engeli: " + str(exc)[:650])
    result = {"kind": "prototype_capture", "status": "blocked" if runtime_blocked else "measured" if not errors and not failed_actions else "failed",
              "captured_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "config_sha256": digest(config_path), "url": config["url"],
              "viewport": config["viewport"], "reduced_motion": config.get("reduced_motion", "reduce"),
              "steps": steps_done, "failed_actions": failed_actions, "errors": errors, "screenshots": screenshots,
              "scope": "Gerçek tarayıcıda belirtilen etkileşimler ve ekranlar. Oyun fiziği, kullanıcı beğenisi, 60FPS veya iOS cihaz testi değildir."}
    put_json(output_dir / "capture.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--browser-path", help="İsteğe bağlı Chromium executable yolu")
    parser.add_argument("--allow-remote", action="store_true", help="Uzak web sayfasında test için açık izin")
    args = parser.parse_args()
    try:
        r = capture(args.config, args.output, browser_path=args.browser_path, allow_remote=args.allow_remote)
        print(json.dumps({"status": r["status"], "output": str(args.output / "capture.json")}, ensure_ascii=False))
        return 0 if r["status"] == "measured" else 2 if r["status"] == "blocked" else 3
    except (EvidenceError, OSError, ValueError) as exc:
        print(f"ENGELLENDİ: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
