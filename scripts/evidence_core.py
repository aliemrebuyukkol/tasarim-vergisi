"""Görsel/video ve insan gözlemlerini kanıt olarak işleyen yerel araçlar.

Görsel metrikler öznel beğeni veya algı ölçüsü değildir. Kullanıcı verilerini ağ üzerinden
iletmez. Kullanıcı testi yüzdeleri betimseldir; istatistiksel anlamlılık iddiası yoktur.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import shutil
import statistics
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class EvidenceError(ValueError):
    pass


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def put_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _pil():
    try:
        from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageStat  # noqa: F401
    except ImportError as exc:
        raise EvidenceError("Görüntü karşılaştırması için Pillow gerekli: pip install Pillow>=10") from exc
    return Image, ImageChops, ImageFilter, ImageStat


def _open_image(path: Path):
    Image, *_ = _pil()
    if not path.is_file():
        raise EvidenceError(f"Görsel bulunamadı: {path}")
    try:
        with Image.open(path) as image:
            return image.convert("RGB")
    except (OSError, ValueError) as exc:
        raise EvidenceError(f"Görsel okunamadı: {path}") from exc


def analyze_pair(reference: Path, candidate: Path, output: Path, *, tolerance: int = 16) -> dict:
    """Aynı viewport içindeki piksel hizası ve farklarını raporlar. Estetik puan değildir."""
    Image, ImageChops, ImageFilter, ImageStat = _pil()
    if not (0 <= tolerance <= 255):
        raise EvidenceError("tolerance 0..255 arasında olmalı")
    a, b = _open_image(reference), _open_image(candidate)
    if a.size != b.size:
        raise EvidenceError(f"Eşit viewport zorunlu: referans={a.size}, aday={b.size}. Otomatik resize yapılmadı.")
    output.mkdir(parents=True, exist_ok=True)
    difference = ImageChops.difference(a, b)
    channels = ImageStat.Stat(difference).mean
    mae = sum(channels) / 3 / 255
    # A pixel is changed if ANY RGB channel differs more than tolerance.
    red, green, blue = difference.split()
    peak = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    changed = peak.point(lambda v: 255 if v > tolerance else 0)
    # metrics across all pixels; converted L per pixel is a descriptive proxy, not perceptual truth
    coverage = sum(ImageStat.Stat(changed).sum) / (255 * a.width * a.height)
    e1 = a.convert("L").filter(ImageFilter.FIND_EDGES)
    e2 = b.convert("L").filter(ImageFilter.FIND_EDGES)
    edge_mae = ImageStat.Stat(ImageChops.difference(e1, e2)).mean[0] / 255
    overlay = Image.blend(a, b, 0.5)
    overlay_path, diff_path = output / "overlay.png", output / "diff.png"
    overlay.save(overlay_path)
    # Amplification for human inspection; numbers use raw unamplified difference.
    difference.point(lambda v: min(255, v * 3)).save(diff_path)
    # Rank coarse cells so a reviewer can quickly locate the most different areas.
    cols, rows, heat = 4, 4, []
    for yi in range(rows):
        for xi in range(cols):
            rect = (a.width * xi // cols, a.height * yi // rows,
                    a.width * (xi + 1) // cols, a.height * (yi + 1) // rows)
            if rect[2] == rect[0] or rect[3] == rect[1]:
                continue
            avg = ImageStat.Stat(difference.crop(rect)).mean
            heat.append({"box": list(rect), "mean_rgb_error_0_to_1": round(sum(avg) / 3 / 255, 5)})
    heat.sort(key=lambda c: c["mean_rgb_error_0_to_1"], reverse=True)
    result = {
        "kind": "visual_comparison", "status": "measured", "measured_at_utc": now_iso(),
        "source": {"path": str(reference), "sha256": digest(reference)},
        "candidate": {"path": str(candidate), "sha256": digest(candidate)},
        "viewport": {"width": a.width, "height": a.height},
        "metrics": {"rgb_mean_absolute_error_0_to_1": round(mae, 5),
                    "changed_pixel_fraction_0_to_1": round(coverage, 5),
                    "edge_mean_absolute_error_0_to_1": round(edge_mae, 5),
                    "pixel_difference_tolerance": tolerance},
        "largest_difference_regions": heat[:5],
        "artifacts": {"overlay": str(overlay_path), "diff": str(diff_path)},
        "interpretation": "Yalnızca aynı-viewport raster farkı. Estetik, duygu, hizalama nedeni, okunabilirlik, fps veya kullanıcı beğenisi ölçümü değildir.",
        "manual_review_required": True,
    }
    put_json(output / "report.json", result)
    return result


def ffprobe_details(video: Path) -> dict:
    if not video.is_file():
        raise EvidenceError(f"Video yok: {video}")
    if not shutil.which("ffprobe"):
        raise EvidenceError("ffprobe bulunamadı (FFmpeg yükleyin)")
    args = ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
            "stream=width,height,avg_frame_rate,duration:format=duration", "-of", "json", str(video)]
    proc = subprocess.run(args, capture_output=True, text=True, timeout=30, check=False)
    if proc.returncode:
        raise EvidenceError(f"ffprobe başarısız: {proc.stderr[-500:]}")
    details = json.loads(proc.stdout)
    if not details.get("streams"):
        raise EvidenceError("Videoda görüntü akışı bulunamadı")
    stream = details["streams"][0]
    duration_str = stream.get("duration") or details.get("format", {}).get("duration")
    duration = float(duration_str) if duration_str and duration_str != "N/A" else None
    return {"width": int(stream["width"]), "height": int(stream["height"]),
            "avg_frame_rate": stream.get("avg_frame_rate"), "duration_seconds": duration}


def parse_timestamps(value: str) -> list[float]:
    try:
        out = [float(v.strip()) for v in value.split(",")]
    except ValueError as exc:
        raise EvidenceError("timestamp listesi 0,0.5,1.2 gibi olmalı") from exc
    if not out or len(out) > 50 or any(not math.isfinite(v) or v < 0 for v in out):
        raise EvidenceError("1-50 adet pozitif/0 zaman noktası girin")
    if len(set(out)) != len(out) or out != sorted(out):
        raise EvidenceError("Zamanlar benzersiz ve artan olmalı")
    return out


def extract_frames(video: Path, timestamps: list[float], output: Path) -> dict:
    if not shutil.which("ffmpeg"):
        raise EvidenceError("ffmpeg bulunamadı")
    meta = ffprobe_details(video)
    if meta["duration_seconds"] is not None and any(t >= meta["duration_seconds"] for t in timestamps):
        raise EvidenceError("İstenen kare video süresinin dışında")
    output.mkdir(parents=True, exist_ok=True)
    frames = []
    for i, t in enumerate(timestamps):
        file = output / f"frame_{i:03d}_{t:.3f}s.png"
        proc = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video),
                               "-ss", f"{t:.6f}", "-frames:v", "1", str(file)],
                              capture_output=True, text=True, timeout=60, check=False)
        if proc.returncode or not file.is_file():
            raise EvidenceError(f"{t} saniyesinde kare alınamadı: {proc.stderr[-400:]}")
        frames.append({"timestamp_seconds": t, "path": str(file), "sha256": digest(file)})
    report = {"kind": "video_frames", "status": "measured", "video": str(video),
              "video_sha256": digest(video), "meta": meta, "frames": frames,
              "note": "FFmpeg kareleri ölçüldü; hareketin insan algısındaki etkisi veya easing kalitesi otomatik doğrulanmaz."}
    put_json(output / "frames.json", report)
    return report


def compare_videos(reference: Path, candidate: Path, timestamps: list[float], output: Path) -> dict:
    r = extract_frames(reference, timestamps, output / "reference")
    c = extract_frames(candidate, timestamps, output / "candidate")
    if (r["meta"]["width"], r["meta"]["height"]) != (c["meta"]["width"], c["meta"]["height"]):
        raise EvidenceError("Video karşılaştırması için eşit çözünürlük gerekli")
    pairs = []
    for i, (rframe, cframe) in enumerate(zip(r["frames"], c["frames"])):
        result = analyze_pair(Path(rframe["path"]), Path(cframe["path"]), output / f"pair_{i:03d}")
        pairs.append({"timestamp_seconds": timestamps[i], "metrics": result["metrics"],
                      "report": str(output / f"pair_{i:03d}" / "report.json")})
    report = {"kind": "video_comparison", "status": "measured", "reference_path": str(reference), "reference_sha256": r["video_sha256"],
              "candidate_path": str(candidate), "candidate_sha256": c["video_sha256"], "frames": pairs,
              "mean_frame_rgb_error": round(statistics.mean(x["metrics"]["rgb_mean_absolute_error_0_to_1"] for x in pairs), 5),
              "caveat": "Kare örneklemidir; aradaki hareket akıcılığı, ses senkronu ve algısal kalite doğrudan doğrulanmaz.",
              "manual_review_required": True}
    put_json(output / "video_report.json", report)
    return report


STUDY_FIELDS = ["participant_id", "variant", "consent", "task_complete", "task_seconds",
                "noticed", "understood", "surprise_1_5", "liking_1_5", "recall_24h", "negative_effect"]


def _bool(value: str, *, optional: bool = False):
    val = value.strip().lower()
    if optional and not val:
        return None
    if val in {"1", "true", "yes", "evet"}:
        return True
    if val in {"0", "false", "no", "hayir", "hayır"}:
        return False
    raise EvidenceError(f"Boole değer geçersiz: {value!r}")


def summarize_study(csv_path: Path, output: Path, min_group: int = 8) -> dict:
    if min_group < 1:
        raise EvidenceError("min_group pozitif olmalı")
    if not csv_path.is_file():
        raise EvidenceError(f"CSV yok: {csv_path}")
    with csv_path.open(encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        missing = set(STUDY_FIELDS) - set(reader.fieldnames or [])
        if missing:
            raise EvidenceError(f"CSV alanları eksik: {', '.join(sorted(missing))}")
        rows = list(reader)
    if not rows:
        raise EvidenceError("Gerçek kullanıcı verisi yok; beğeni kanıtı üretilemez. CSV yalnızca şablon.")
    grouped: dict[str, list] = defaultdict(list)
    seen = set()
    excluded = 0
    for row_index, r in enumerate(rows, start=2):
        ident = r["participant_id"].strip()
        variant = r["variant"].strip()
        if not ident or not variant:
            raise EvidenceError(f"Satır {row_index}: participant_id ve variant gerekli")
        if ident in seen:
            raise EvidenceError("Tek katılımcı birden fazla satırda. Bu analiz kişi-başına tek görev içindir.")
        seen.add(ident)
        if not _bool(r["consent"]):
            excluded += 1
            continue
        parsed: dict[str, Any] = {"variant": variant}
        for key in ("task_complete", "noticed", "understood", "negative_effect"):
            parsed[key] = _bool(r[key])
        parsed["recall_24h"] = _bool(r["recall_24h"], optional=True)
        try:
            parsed["task_seconds"] = float(r["task_seconds"])
            parsed["surprise_1_5"] = int(r["surprise_1_5"])
            parsed["liking_1_5"] = int(r["liking_1_5"])
        except ValueError as exc:
            raise EvidenceError(f"Satır {row_index}: sayısal alan hatası") from exc
        if not (0 <= parsed["task_seconds"] <= 86400):
            raise EvidenceError(f"Satır {row_index}: görev süresi aralık dışı")
        if any(parsed[k] not in {1, 2, 3, 4, 5} for k in ("surprise_1_5", "liking_1_5")):
            raise EvidenceError(f"Satır {row_index}: beğeni/şaşkınlık 1-5 olmalı")
        grouped[variant].append(parsed)
    if not grouped:
        raise EvidenceError("Onay vermiş katılımcı gözlemi bulunamadı")
    summary: dict = {}
    for variant, group in sorted(grouped.items()):
        n = len(group)
        followup = [x["recall_24h"] for x in group if x["recall_24h"] is not None]
        summary[variant] = {
            "participants": n, "confidence": "pilot_only" if n < min_group else "descriptive_only",
            "task_success_rate": round(sum(x["task_complete"] for x in group) / n, 3),
            "noticed_rate": round(sum(x["noticed"] for x in group) / n, 3),
            "understood_rate": round(sum(x["understood"] for x in group) / n, 3),
            "surprise_mean_1_to_5": round(statistics.mean(x["surprise_1_5"] for x in group), 2),
            "liking_mean_1_to_5": round(statistics.mean(x["liking_1_5"] for x in group), 2),
            "task_seconds_median": round(statistics.median(x["task_seconds"] for x in group), 2),
            "negative_effect_count": sum(x["negative_effect"] for x in group),
            "recall_24h_rate": round(sum(followup) / len(followup), 3) if followup else None,
            "recall_24h_responses": len(followup),
        }
    report = {
        "kind": "human_study_descriptive", "status": "measured", "generated_at_utc": now_iso(),
        "csv_sha256": digest(csv_path), "consent_excluded": excluded,
        "groups": summary,
        "evidence_level": "E2_observed_pilot" if min(g["participants"] for g in summary.values()) < min_group else "E3_structured_descriptive",
        "limitations": ["Bu bir betimleyici analizdir, nedensellik veya istatistiksel anlamlılık kanıtı değildir.",
                        "Katılımcı temsiliyeti, rastgeleleme, ortam ve ölçek yanlılıkları ayrıca incelenmeli.",
                        "Gecikmeli hatırlama eksikse 24 saatlik sonuç iddia edilemez.",
                        "Kimlikler rapora eklenmez; kullanıcı izni alınmadan veri toplanmaz veya yayınlanmaz."],
    }
    put_json(output, report)
    return report
