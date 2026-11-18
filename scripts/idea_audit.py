#!/usr/bin/env python3
"""Fikirlerin yapısal çeşitliliği ve karar kanıtı için deterministik STATİK kontrol.

Bu araç görüntü yorumlamaz; özgünlük, kullanıcı memnuniyeti veya fikrin işe
yarayacağını kanıtlamaz. Sadece aynı mekanizmanın kozmetik kopyalarını ve
eksik hipotez/kabul kriterlerini işaretler.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

KEYS = (
    "id", "name", "family", "core_action", "mechanic", "composition",
    "motion", "emotional_payoff", "baseline_difference", "user_value",
    "feasibility_proof", "criticism", "reference_fidelity",
)
SIGNATURE = ("core_action", "mechanic", "composition", "motion", "emotional_payoff")
SCORES = ("novelty", "usefulness", "coherence", "feasibility", "emotional_impact")


def normalize(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().casefold())


def audit(payload: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["Kök veri JSON nesnesi olmalı"]
    baseline = payload.get("baseline")
    if not isinstance(baseline, dict) or not normalize(baseline.get("mechanic")):
        errors.append("baseline.mechanic: mevcut standart çözüm tanımlanmalı")
        baseline = {}
    items = payload.get("directions")
    if not isinstance(items, list) or len(items) < 3:
        return errors + ["directions: yapısal olarak farklı en az üç yön bekleniyor"]
    seen: set[str] = set()
    for i, item in enumerate(items):
        prefix = f"directions[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: nesne olmalı")
            continue
        for field in KEYS:
            if not normalize(item.get(field)):
                errors.append(f"{prefix}.{field}: boş olamaz")
        ident = normalize(item.get("id"))
        if ident in seen:
            errors.append(f"{prefix}.id: tekrar eden ID {ident}")
        seen.add(ident)
        scores = item.get("scores")
        if not isinstance(scores, dict):
            errors.append(f"{prefix}.scores: 1-5 ölçütlerini içeren nesne olmalı")
        else:
            for metric in SCORES:
                value = scores.get(metric)
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not 1 <= value <= 5:
                    errors.append(f"{prefix}.scores.{metric}: 1-5 sayı bekleniyor")
        if normalize(item.get("mechanic")) == normalize(baseline.get("mechanic")):
            errors.append(f"{prefix}: mekanik baseline ile aynı; yalnızca kozmetik ayrışma yetersiz")
        if not isinstance(item.get("risks"), list) or not item.get("risks"):
            errors.append(f"{prefix}.risks: en az bir risk/yanlışlanma ihtimali belirt")
    valid = [v for v in items if isinstance(v, dict)]
    for i, left in enumerate(valid):
        for j in range(i + 1, len(valid)):
            right = valid[j]
            identical_axes = [field for field in SIGNATURE
                              if normalize(left.get(field)) and normalize(left.get(field)) == normalize(right.get(field))]
            if len(identical_axes) >= 4:
                errors.append(
                    f"directions[{i}] ve directions[{j}]: 5 yapısal eksenin {len(identical_axes)} tanesi aynı "
                    f"({', '.join(identical_axes)}); farklı renk yeni konsept değildir"
                )
    families = {normalize(v.get("family")) for v in valid}
    if len(families) < 2:
        errors.append("En az iki farklı yaratıcı yaklaşım ailesi bulunmalı")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Fikir laboratuvarı JSON dosyası")
    args = parser.parse_args()
    try:
        content = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"FAIL: JSON okunamadı: {exc}")
        return 2
    errors = audit(content)
    if errors:
        print("FAIL: Yapısal fikir kontrolünde sorunlar:")
        for err in errors:
            print(" - " + err)
        return 1
    print(f"PASS: {len(content['directions'])} yönün yapısal çeşitliliği ve karar alanları statik olarak denetlendi.")
    print("NOT: Bu, gerçek görsel özgünlük veya insan beğenisi testi değildir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
