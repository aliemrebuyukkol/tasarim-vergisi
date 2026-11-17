# Tasarım Vergisi

Küratörlü bir referans kataloğundan (UI galerileri, motion, tasarım sistemleri, pixel-art/oyun,
3D, video, AI ses/medya ve kalite kapıları) istenen uygulama için en iyi, en kaliteli ve en
farklı özellikleri toplayan; örnek tasarımlar üreten ve işi ajanlara görev olarak dağıtan bir
**Agent Skill**.

Format: [Agent Skills](https://agentskills.io) standardı (`SKILL.md` + `references/`).
Bu format Claude Code, Codex, Gemini CLI, Cursor, Antigravity, GitHub Copilot ve diğer
uyumlu araçlarda çalışır.

```
skills/tasarim-vergisi/
├── SKILL.md                    # akış (8 adım)
└── references/
    ├── catalog.md              # 12 kategori + tür → kategori matrisi
    ├── finding-card.md         # bulgu kartı formatı
    └── task-brief.md           # ajan görev brifi şablonu
```

## Kurulum

### Tek komut (çoğu araç)
```bash
npx skills add aliemrebuyukkol/tasarim-vergisi
```

### Claude Code
```bash
git clone https://github.com/aliemrebuyukkol/tasarim-vergisi /tmp/tv && cp -R /tmp/tv/skills/tasarim-vergisi ~/.claude/skills/
```
Kullanım: `/tasarim-vergisi <uygulama tanımı>`

### Codex CLI
```bash
git clone https://github.com/aliemrebuyukkol/tasarim-vergisi /tmp/tv && mkdir -p ~/.codex/skills && cp -R /tmp/tv/skills/tasarim-vergisi ~/.codex/skills/
```
Kullanım: `$tasarim-vergisi` veya "tasarım vergisi skill'ini kullan".

### Gemini CLI / Antigravity
```bash
git clone https://github.com/aliemrebuyukkol/tasarim-vergisi /tmp/tv && mkdir -p ~/.gemini/skills && cp -R /tmp/tv/skills/tasarim-vergisi ~/.gemini/skills/
```

### Cursor / skill desteklemeyen araçlar
Repoyu projeye ekleyin; kökteki `AGENTS.md` ajanı skill'e yönlendirir.
Ya da `.cursor/rules/` içine `SKILL.md`'yi bir kural olarak kopyalayın.

### Claude.ai (web/masaüstü)
`skills/tasarim-vergisi` klasörünü zip'leyip Ayarlar → Capabilities → Skills'ten yükleyin.

## Kullanım örneği
> Tasarım vergisi: freelancerlar için fatura ve zaman takibi paneli, Next.js + Tailwind,
> minimal ama oyunsu, ajanlarla uygulama da yap.

Skill sırasıyla: 4 kısa soru → kategori seçimi → paralel araştırma → puanlama → örnek
demolar → `TASARIM-VERGISI.md` raporu → ajanlara iş paketleri.

## Katkı
Yeni referansları `references/catalog.md` içinde uygun kategoriye ekleyin
(ad, URL, ne verir, uygun uygulama türleri).

## Lisans
MIT
