#!/usr/bin/env python3
"""Projeye özel gerçek kanıt senaryolarını her build/PR'da yeniden çalıştır.

Gerçek referans/adayı olmayan test engellendi; sıfır test başarılı sayılmaz.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from evidence_core import EvidenceError, analyze_pair, compare_videos, parse_timestamps, put_json
from prototype_capture import capture


def _path(base: Path, raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else base / path


def run_suite(config_path: Path, output: Path, *, browser_path: str | None = None) -> dict:
    if not config_path.is_file():
        raise EvidenceError(f"Suite config bulunamadı: {config_path}")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or not isinstance(config.get("cases"), list) or not config["cases"]:
        raise EvidenceError("En az bir gerçek kanıt senaryosu tanımlanmalı; boş test başarı değildir")
    base = config_path.parent
    output.mkdir(parents=True, exist_ok=True)
    results, ids = [], set()
    for case in config["cases"]:
        ident = case.get("id")
        kind = case.get("kind")
        if not isinstance(ident, str) or not ident or not ident.replace("-", "").replace("_", "").isalnum() or ident in ids:
            raise EvidenceError("Benzersiz ve güvenli case.id gerekli (harf/rakam/-/_)")
        ids.add(ident)
        if kind not in {"image", "video", "browser"}:
            raise EvidenceError(f"{ident}: kind image/video/browser olmalı")
        if not case.get("target_state"):
            raise EvidenceError(f"{ident}: hedef UI/sahne durumu target_state gerekli")
        case_out = output / ident
        try:
            if kind == "image":
                result = analyze_pair(_path(base, case["reference"]), _path(base, case["candidate"]), case_out,
                                      tolerance=int(case.get("tolerance", 16)))
                value = result["metrics"]["rgb_mean_absolute_error_0_to_1"]
                limit = float(case["max_rgb_mae"])
                if not 0 <= limit <= 1:
                    raise EvidenceError("max_rgb_mae 0..1 olmalı")
            elif kind == "video":
                result = compare_videos(_path(base, case["reference"]), _path(base, case["candidate"]),
                                        parse_timestamps(case["timestamps"]), case_out)
                value = result["mean_frame_rgb_error"]
                limit = float(case["max_mean_frame_mae"])
                if not 0 <= limit <= 1:
                    raise EvidenceError("max_mean_frame_mae 0..1 olmalı")
            else:
                result = capture(_path(base, case["config"]), case_out, browser_path=browser_path, allow_remote=False)
                value, limit = None, None
            if kind == "browser":
                status = "passed" if result["status"] == "measured" else result["status"]
            else:
                status = "passed" if value <= limit else "failed"
            results.append({"id": ident, "kind": kind, "state": case["target_state"],
                            "status": status, "observed": value, "threshold": limit,
                            "report": str(case_out)})
        except (EvidenceError, KeyError, ValueError, OSError) as exc:
            results.append({"id": ident, "kind": kind, "state": case["target_state"],
                            "status": "blocked", "reason": str(exc)[:500]})
    any_failed = any(x["status"] == "failed" for x in results)
    any_blocked = any(x["status"] == "blocked" for x in results)
    status = "failed" if any_failed else "blocked" if any_blocked else "technical_checks_passed_manual_review_required"
    report = {"kind": "technical_evidence_suite", "status": status,
              "ran_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "results": results, "notes": "Gerçek dosyalar karşılaştırıldı; renk/piksel farkı, video örnekleme veya belirli browser eylemi insan beğenisi, klinik etki veya tüm cihazları doğrulamaz."}
    put_json(output / "suite.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--browser-path")
    args = parser.parse_args()
    try:
        report = run_suite(args.config, args.output, browser_path=args.browser_path)
        print(json.dumps({"status": report["status"], "case_count": len(report["results"]),
                          "report": str(args.output / "suite.json")}, ensure_ascii=False))
        return 0 if report["status"] == "technical_checks_passed_manual_review_required" else 3
    except (EvidenceError, json.JSONDecodeError) as exc:
        print(f"ENGELLENDİ: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
