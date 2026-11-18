#!/usr/bin/env python3
"""Human-Lens experience cards için güvenli, deterministik şema kontrolü.

Bu denetim görseli GÖRMEZ; insan beğenisi, duygusu, klinik etki, göz
izleme veya özgünlük için kanıt DEĞİLDİR. Sadece eksik hipotez,
kanıt etiketi, karşıt yorum ve güvenli test planını yakalar.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

STAGES = ("encounter", "interpretation", "expectation", "resolution", "afterglow")
LEVELS = {f"E{i}": i for i in range(5)}
CONTEXT_FIELDS = ("id", "goal", "potential_reaction", "alternative_reaction", "accessibility")
MOMENT_FIELDS = ("stage", "visible_evidence", "inferred_reaction", "counter_hypothesis", "user_test")
SURPRISE_FIELDS = (
    "baseline_expectation", "advance_cue", "unexpected_change", "narrative_reason",
    "resolution", "player_control", "repeat_behavior", "possible_negative_reaction",
)
TEST_FIELDS = ("task", "behavior_signal", "non_leading_question", "counterevidence", "privacy_plan")
SAFETY_FIELDS = ("skip_or_exit", "reduced_motion", "sound_off_equivalent", "no_emotional_penalty")


def normalize(value: object) -> str:
    return re.sub(r"\s+", " ", str(value).strip().casefold()) if value is not None else ""


def audit(data: object) -> list[str]:
    issues: list[str] = []
    if not isinstance(data, dict):
        return ["root: JSON nesnesi bekleniyor"]

    for field in ("id", "project", "design_mechanic", "reference_scope", "evidence_level"):
        if not normalize(data.get(field)):
            issues.append(f"{field}: zorunlu ve dolu olmalı")
    level = data.get("evidence_level")
    if level not in LEVELS:
        issues.append("evidence_level: E0-E4 arası olmalı")
    if level in ("E1", "E2", "E3", "E4") and not normalize(data.get("evidence_source")):
        issues.append("evidence_source: gözlem/ölçüm kaynağı gerekli")
    if level in ("E3", "E4") and not normalize(data.get("user_test_details")):
        issues.append("user_test_details: katılımcı ve yöntem bilgisi gerekli")

    contexts = data.get("viewer_contexts")
    if not isinstance(contexts, list) or len(contexts) < 3:
        issues.append("viewer_contexts: en az üç bağlam/niyet gerekli")
        contexts = []
    context_ids: set[str] = set()
    for i, context in enumerate(contexts):
        if not isinstance(context, dict):
            issues.append(f"viewer_contexts[{i}]: nesne gerekli")
            continue
        for field in CONTEXT_FIELDS:
            if not normalize(context.get(field)):
                issues.append(f"viewer_contexts[{i}].{field}: boş olamaz")
        ctxid = normalize(context.get("id"))
        if ctxid and ctxid in context_ids:
            issues.append(f"viewer_contexts[{i}].id: tekrar eden bağlam")
        context_ids.add(ctxid)

    moments = data.get("moments")
    if not isinstance(moments, list) or len(moments) != len(STAGES):
        issues.append("moments: tam beş algı aşaması bekleniyor")
        moments = []
    for i, moment in enumerate(moments):
        if not isinstance(moment, dict):
            issues.append(f"moments[{i}]: nesne gerekli")
            continue
        for field in MOMENT_FIELDS:
            if not normalize(moment.get(field)):
                issues.append(f"moments[{i}].{field}: boş olamaz")
        if i < len(STAGES) and moment.get("stage") != STAGES[i]:
            issues.append(f"moments[{i}].stage: beklenen {STAGES[i]}")

    surprise = data.get("surprise")
    if not isinstance(surprise, dict):
        issues.append("surprise: nesne gerekli")
        surprise = {}
    for field in SURPRISE_FIELDS:
        if not normalize(surprise.get(field)):
            issues.append(f"surprise.{field}: boş olamaz")
    if normalize(surprise.get("unexpected_change")) == normalize(surprise.get("baseline_expectation")):
        issues.append("surprise: beklenen ile beklenmedik aynı olamaz")

    plan = data.get("test_plan")
    if not isinstance(plan, dict):
        issues.append("test_plan: nesne gerekli")
        plan = {}
    for field in TEST_FIELDS:
        if not normalize(plan.get(field)):
            issues.append(f"test_plan.{field}: boş olamaz")

    safety = data.get("safety")
    if not isinstance(safety, dict):
        issues.append("safety: nesne gerekli")
        safety = {}
    for field in SAFETY_FIELDS:
        if safety.get(field) is not True:
            issues.append(f"safety.{field}: açık erişim yolu / güvenlik doğrulaması gerekli (true)")

    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        issues.append("claims: en az bir kanıt etiketli iddia gerekli")
        claims = []
    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            issues.append(f"claims[{i}]: nesne gerekli")
            continue
        if not normalize(claim.get("text")):
            issues.append(f"claims[{i}].text: boş olamaz")
        if claim.get("evidence_level") not in LEVELS:
            issues.append(f"claims[{i}].evidence_level: E0-E4 bekleniyor")
        elif level in LEVELS and LEVELS[claim["evidence_level"]] > LEVELS[level]:
            issues.append(f"claims[{i}]: kanıtı olmayan daha yüksek seviye iddia")
        if not normalize(claim.get("limitation")):
            issues.append(f"claims[{i}].limitation: belirsizlik yazılmalı")
        if claim.get("type") == "user_observation" and LEVELS.get(claim.get("evidence_level"), 0) < 3:
            issues.append(f"claims[{i}]: kullanıcı gözlemi E3 olmadan ileri sürülemez")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"FAIL: JSON okunamadı: {exc}")
        return 2
    problems = audit(data)
    if problems:
        print("FAIL: Human-Lens kartı eksikleri:")
        for problem in problems:
            print(" - " + problem)
        return 1
    print("PASS: İnsan algısı hipotezi, karşı görüş, sürpriz, kontrol, kanıt ve test planı yapısal olarak tam.")
    print("SINIR: Algı/zevk/sürpriz/duygusal etki gerçekte ölçülmedi; doğrulama insan testine bağlı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
