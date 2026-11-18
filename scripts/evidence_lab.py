#!/usr/bin/env python3
"""Tasarım Vergisi v5: görsel/video/kullanıcı kanıtı işleme ve karar CLI'si.

Hiçbir komut gerçek insan algısını, özgünlüğü veya App Store uygunluğunu otomatik
olarak kanıtlamaz. Raporlar çıktının kapsam ve sınırlarını belirtir.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from evidence_core import (EvidenceError, analyze_pair, compare_videos, digest,
                           extract_frames, parse_timestamps, put_json, summarize_study)


def check_case(path: Path, destination: Path) -> dict:
    """En az bir canlı kanıt yoksa release/onay etiketi vermeyen kapı."""
    if not path.is_file():
        raise EvidenceError(f"Manifest yok: {path}")
    case = json.loads(path.read_text(encoding="utf-8"))
    required = {"case_id", "hypothesis", "reference_id", "technical_evidence", "human_evidence", "acceptance"}
    missing = required - set(case)
    if missing:
        raise EvidenceError("Manifest alanları eksik: " + ", ".join(sorted(missing)))
    if not case["case_id"] or not case["hypothesis"] or not case["reference_id"]:
        raise EvidenceError("case_id, hypothesis, reference_id boş olamaz")
    acceptance = case["acceptance"]
    if not isinstance(acceptance, dict):
        raise EvidenceError("acceptance JSON object olmalı")
    artifacts = []
    failed = []
    blocked = []
    technical = case["technical_evidence"]
    if not isinstance(technical, list):
        raise EvidenceError("technical_evidence bir dizi olmalı")
    if not technical:
        blocked.append("Görsel, video veya prototip teknik kanıtı yok")
    for artifact in technical:
        if not isinstance(artifact, dict) or "report" not in artifact:
            raise EvidenceError("technical_evidence elemanında report gerekli")
        report_path = Path(artifact["report"])
        if not report_path.is_absolute():
            report_path = path.parent / report_path
        if not report_path.is_file():
            blocked.append(f"Kanıt dosyası yok: {report_path}")
            continue
        try:
            data = json.loads(report_path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            blocked.append(f"Kanıt okunamadı: {report_path}: {exc}")
            continue
        kind = data.get("kind")
        if kind not in {"visual_comparison", "video_comparison", "prototype_capture"} or data.get("status") != "measured":
            blocked.append(f"Beklenmedik veya ölçülmemiş kanıt: {report_path}")
            continue
        if kind == "visual_comparison":
            for which in ("source", "candidate"):
                info = data.get(which, {})
                source = Path(info.get("path", ""))
                if not source.is_file() or digest(source) != info.get("sha256"):
                    blocked.append(f"Kanıt kaynak dosyası değişmiş/yok: {which} {source}")
            max_mae = acceptance.get("max_rgb_mae")
            if max_mae is not None:
                try:
                    limit = float(max_mae)
                    value = float(data["metrics"]["rgb_mean_absolute_error_0_to_1"])
                except (KeyError, TypeError, ValueError) as exc:
                    raise EvidenceError("Geçersiz görsel eşik veya rapor") from exc
                if not 0 <= limit <= 1:
                    raise EvidenceError("max_rgb_mae 0..1 arasında olmalı")
                if value > limit:
                    failed.append(f"Görsel fark eşiği aşıldı: {value} > {limit}")
        if kind == "video_comparison":
            for which in ("reference", "candidate"):
                source = Path(data.get(f"{which}_path", ""))
                if not source.is_file() or digest(source) != data.get(f"{which}_sha256"):
                    blocked.append(f"Video kanıtı değişmiş/yok: {source}")
        if kind == "prototype_capture":
            if data.get("errors") or data.get("failed_actions"):
                failed.append(f"Prototip etkileşim/console hatası: {report_path}")
            if not data.get("screenshots"):
                blocked.append(f"Prototip ekran görüntüsü alınmadı: {report_path}")
            else:
                for shot in data["screenshots"]:
                    shot_path = Path(shot.get("path", ""))
                    if not shot_path.is_file() or digest(shot_path) != shot.get("sha256"):
                        blocked.append(f"Prototip görüntü kanıtı değişmiş/yok: {shot_path}")
        artifacts.append({"kind": kind, "path": str(report_path), "sha256": digest(report_path)})

    human = case["human_evidence"]
    if human is not None and not isinstance(human, dict):
        raise EvidenceError("human_evidence ya null ya da {report:...} olmalı")
    min_participants = int(acceptance.get("min_human_per_variant", 8))
    if min_participants < 1:
        raise EvidenceError("min_human_per_variant 1 veya daha büyük olmalı")
    for threshold in ("min_task_success_rate", "min_liking_mean"):
        if threshold in acceptance and not isinstance(acceptance[threshold], (int, float)):
            raise EvidenceError(f"Eşik sayısal olmalı: {threshold}")
    if "min_task_success_rate" in acceptance and not 0 <= acceptance["min_task_success_rate"] <= 1:
        raise EvidenceError("min_task_success_rate 0..1 olmalı")
    if "min_liking_mean" in acceptance and not 1 <= acceptance["min_liking_mean"] <= 5:
        raise EvidenceError("min_liking_mean 1..5 olmalı")
    human_supported = False
    if human and human.get("report"):
        user_path = Path(human["report"])
        if not user_path.is_absolute():
            user_path = path.parent / user_path
        if not user_path.is_file():
            blocked.append(f"Kullanıcı test raporu yok: {user_path}")
        else:
            data = json.loads(user_path.read_text(encoding="utf-8"))
            if data.get("kind") != "human_study_descriptive" or data.get("status") != "measured":
                blocked.append("Kullanıcı test raporu gerçek ölçüm olarak işaretlenmemiş")
            else:
                groups = list(data.get("groups", {}).values())
                group_counts = [x["participants"] for x in groups]
                human_supported = bool(group_counts) and min(group_counts) >= min_participants
                artifacts.append({"kind": "human_study_descriptive", "path": str(user_path), "sha256": digest(user_path)})
                if not human_supported:
                    blocked.append(f"İnsan verisi pilot seviyesinde veya küçük gruplu: her varyant için >= {min_participants} bekleniyor")
                max_negative = int(acceptance.get("max_negative_effect_count", 0))
                for i, group in enumerate(groups, start=1):
                    if group.get("negative_effect_count", 0) > max_negative:
                        failed.append(f"İnsan deneyimi olumsuz etki sinyali: grup {i}; inceleme zorunlu")
                    min_success = acceptance.get("min_task_success_rate")
                    if min_success is not None and group["task_success_rate"] < float(min_success):
                        failed.append(f"Görev başarı eşiği başarısız: grup {i}")
                    min_liking = acceptance.get("min_liking_mean")
                    if min_liking is not None and group["liking_mean_1_to_5"] < float(min_liking):
                        failed.append(f"Beğeni eşiği başarısız: grup {i}")
    else:
        blocked.append("Gerçek insan değerlendirmesi eklenmemiş; beğeni iddiası doğrulanamaz")
    # Human evidence must never be inferred from visual metrics.
    if failed:
        status = "failed"
    elif blocked:
        status = "limited_or_blocked"
    else:
        status = "technical_gates_passed_and_human_observations_present"
    result = {"case_id": case["case_id"], "hypothesis": case["hypothesis"],
              "status": status, "visual_quality_is_human_validated": False,
              "human_observations_available": human_supported, "failed": failed,
              "blocked": blocked, "used_reports": artifacts,
              "notes": "Teknik eşik ve betimleyici insan gözlemi; estetik doğruluk, nedensellik, klinik etki veya release onayı değildir."}
    put_json(destination, result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="action", required=True)
    p = subs.add_parser("compare", help="Aynı viewport iki ekran görüntüsünü karşılaştır")
    p.add_argument("--reference", type=Path, required=True)
    p.add_argument("--candidate", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--tolerance", type=int, default=16)
    p = subs.add_parser("frames", help="Videodan belirlenmiş zamanlarda kare çıkar")
    p.add_argument("--video", type=Path, required=True)
    p.add_argument("--timestamps", required=True, help="Örn. 0,0.5,1.2")
    p.add_argument("--output", type=Path, required=True)
    p = subs.add_parser("video-compare", help="İki videonun aynı zamanlı karelerini karşılaştır")
    p.add_argument("--reference", type=Path, required=True)
    p.add_argument("--candidate", type=Path, required=True)
    p.add_argument("--timestamps", required=True)
    p.add_argument("--output", type=Path, required=True)
    p = subs.add_parser("study", help="Gerçek kullanıcı gözlemlerini betimleyici analiz et")
    p.add_argument("--csv", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--min-group", type=int, default=8)
    p = subs.add_parser("gate", help="Teknik ve kullanıcı kanıtını aynı hipotez altında değerlendir")
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.action == "compare":
            report = analyze_pair(args.reference, args.candidate, args.output, tolerance=args.tolerance)
        elif args.action == "frames":
            report = extract_frames(args.video, parse_timestamps(args.timestamps), args.output)
        elif args.action == "video-compare":
            report = compare_videos(args.reference, args.candidate, parse_timestamps(args.timestamps), args.output)
        elif args.action == "study":
            report = summarize_study(args.csv, args.output, args.min_group)
        else:
            report = check_case(args.manifest, args.output)
        print(json.dumps({"status": report["status"], "kind": report.get("kind", args.action),
                          "output": str(args.output)}, ensure_ascii=False))
        # A blocked or failing gate is NOT a successful release check.
        return 3 if args.action == "gate" and report["status"] != "technical_gates_passed_and_human_observations_present" else 0
    except (EvidenceError, OSError, json.JSONDecodeError) as exc:
        print(f"ENGELLENDİ: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
