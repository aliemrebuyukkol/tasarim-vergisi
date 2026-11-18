#!/usr/bin/env python3
"""Tasarım Vergisi v4 doküman ve yerel bağlantı statik tutarlılık testi.

Gerçek UI, gameplay, cihaz performansı veya kaynak erişimini doğrulamaz.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "tasarim-vergisi"
REQUIRED = [
    "SKILL.md",
    "references/catalog.md",
    "references/reference-intelligence.md",
    "references/finding-card.md",
    "references/design-dna.md",
    "references/domain-profiles.md",
    "references/game-design.md",
    "references/orchestration.md",
    "references/task-brief.md",
    "references/quality-gates.md",
    "references/perception-engine.md",
    "references/creative-reasoning.md",
    "references/critique-council.md",
    "references/motion-direction.md",
    "references/design-learning.md",
    "references/human-perception.md",
    "references/empathy-simulator.md",
    "references/surprise-architecture.md",
    "references/taste-lab.md",
]


def main() -> None:
    issues: list[str] = []
    for relative in REQUIRED:
        path = SKILL / relative
        if not path.is_file():
            issues.append(f"Eksik: {path.relative_to(ROOT)}")
        elif not path.read_text(encoding="utf-8").strip():
            issues.append(f"Boş: {path.relative_to(ROOT)}")

    entry = SKILL / "SKILL.md"
    if entry.is_file():
        content = entry.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not frontmatter:
            issues.append("SKILL.md: YAML frontmatter eksik")
        else:
            section = frontmatter.group(1)
            for key in ("name", "description", "license"):
                if not re.search(rf"(?m)^{key}:\s*\S", section):
                    issues.append(f"SKILL.md: {key} eksik")
            if not re.search(r"(?m)^name:\s*tasarim-vergisi\s*$", section):
                issues.append("SKILL.md: name tasarim-vergisi olmalı")
        for keyword in ("Design DNA", "quality-gates.md", "perception-engine.md", "creative-reasoning.md", "critique-council.md", "human-perception.md", "taste-lab.md", "surprise-architecture.md", "oyun", "engellendi"):
            if keyword.casefold() not in content.casefold():
                issues.append(f"SKILL.md: {keyword} kavramı yok")

    markdown_paths = [SKILL / "SKILL.md", *SKILL.glob("references/*.md"), ROOT / "README.md"]
    for path in markdown_paths:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).is_file():
                issues.append(f"{path.relative_to(ROOT)}: kırık bağlantı: {target}")

    if (SKILL / "references" / "catalog.md").is_file():
        catalog = (SKILL / "references" / "catalog.md").read_text(encoding="utf-8")
        if "bu oturumda Blender MCP mevcut" in catalog:
            issues.append("catalog.md: doğrulanmamış Blender MCP varsayımı")
        if "TASARIM-VERGISI-V2-CATALOG-BEGIN" not in catalog:
            issues.append("catalog.md: katalog addendum uygulanmamış")

    agents, gemini = ROOT / "AGENTS.md", ROOT / "GEMINI.md"
    if agents.is_file() and gemini.is_file():
        if agents.read_text(encoding="utf-8") != gemini.read_text(encoding="utf-8"):
            issues.append("AGENTS.md ve GEMINI.md farklı")

    if issues:
        raise SystemExit("Skill statik testleri başarısız:\n- " + "\n- ".join(issues))
    print(f"Skill statik testleri geçti: {len(REQUIRED)} zorunlu belge, yerel linkler ve frontmatter.")


if __name__ == "__main__":
    main()
