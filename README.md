# Tasarım Vergisi v5

**Referansı oku → ölç → Design DNA oluştur → uzman ajanlara dağıt → gerçek çıktıyı doğrula.**

Referans kataloğundan araştırma yapan, fikirleri ürün katkısına göre seçen, görsel/motion/etkileşim kurallarını teknik tasarım sözleşmesine dönüştüren ve web, mobil, oyun, 3D, video projelerini test kapılarıyla yöneten araçtan bağımsız bir [Agent Skill](https://agentskills.io).

## v5: Gerçek kanıta bağlanan insan algısı

Skill, yalnızca bir tasarımın insanlarca sevilmesi gerektiğini öne sürmekle kalmaz; kanıtı **hangi araçla, hangi durumda ve hangi sınırla** topladığını belirtir.

- **Visual Evidence:** Aynı viewport ekranlar için gerçek piksel farkı, katman karşılaştırması, bölgesel diff ve SHA-256 referansları.
- **Motion Evidence:** FFmpeg ile referans/aday kliplerinden aynı zaman damgalarında gerçek kareler ve raporlar.
- **Interaction Capture:** Playwright ile localhost prototipinde eylemleri yürüten, console hatalarını ve ekran görüntülerini raporlayan test aracı.
- **Human Study:** Rıza ile toplanan gerçek CSV gözlemlerinden görev başarısı, fark etme, anlama, öznel şaşkınlık, beğeni ve 24 saatlik hatırlamanın ayrı betimsel analizi.
- **Evidence Gate:** Hipotez + teknik rapor + insan gözlemini ilişkilendiren, eksik kanıtta “doğrulandı” demeyen karar kapısı.
- **CI + ürün regresyonu:** Skill için her commit/PR'da statik ve sentetik testler, ürün repo'suna takıldığında ise gerçek referans/aday görüntülerle tekrarlanan görsel regresyon; eksik görüntüler fail-closed.

### Hızlı kullanım

~~~bash
pip install -r scripts/requirements-evidence.txt
python3 scripts/evidence_lab.py compare --reference ref.png --candidate build.png --output evidence/scene
python3 scripts/evidence_lab.py frames --video scene.mp4 --timestamps 0,0.5,1.2 --output evidence/frames
python3 scripts/evidence_lab.py video-compare --reference ref.mp4 --candidate build.mp4 --timestamps 0,0.5,1.2 --output evidence/motion
python3 scripts/evidence_lab.py study --csv private-study.csv --output evidence/study.json
python3 scripts/evidence_lab.py gate --manifest examples/evidence-case.template.json --output evidence/gate.json
python3 scripts/evidence_suite.py --config examples/project-evidence-suite.template.json --output evidence/ci
~~~

Tarayıcı yakalama (Playwright + Chromium gerekli):

~~~bash
python3 -m http.server 8000 --directory examples/prototype-demo
# Başka terminalde:
python3 scripts/prototype_capture.py --config examples/prototype-capture.template.json --output evidence/browser
~~~

Kullanıcı testi şablonu `examples/human-study-template.csv` **boştur**. Gerçek katılımcı sonucu sağlanmadıkça başarı veya psikolojik etki iddiası yoktur. Detaylar: [Empirical Evidence Loop](skills/tasarim-vergisi/references/empirical-evidence-loop.md) ve [Evidence Tools](skills/tasarim-vergisi/references/evidence-tools.md).

## v4: İnsansı düşünme ve algı hipotezleri

- **Human Perception:** İlk bakış, görsel akıcılık, beklenti, şaşkınlık, merak, duygusal anlam ve hatırlamayı ayrı ele alır.
- **Empathy Simulator:** Farklı kullanıcı amaçları ve erişilebilirlik koşulları için *varsayımsal* birinci kişi anlatıları ve karşı hipotezler.
- **Surprise Architecture:** Rastgele efekt yerine beklenti → ipucu → anlamlı sapma → çözülme → kullanıcı kontrolü.
- **Taste Lab:** “Fark etti”, “anladı”, “şaşırdı”, “sevdi”, “hatırladı” iddialarını farklı deneylerle test etme planı.
- **Evidence Levels:** E0 model varsayımından E4 tekrarlı kullanıcı kanıtına uzanan etiketleme. Yapay zekânın görsel analizi insan kullanıcı testi değildir.
- **Experience Audit:** JSON kartlarında farklı bağlamları, alternatif yorumları, kullanıcı kontrolünü, kanıt seviyesini ve test planını statik kontrol eder.

## Öne çıkan yenilikler

- **Perception Engine:** İlk bakış, görsel hiyerarşi, sahne grafı ve motion sürekliliği.
- **Creative Reasoning:** Sıradan baseline, çapraz alanlardan fikir aktarma, gerçekten farklı üç yön, kör eleştiri.
- **Critique Council:** Tasarımcı, oyuncu, teknik itiraz ve kullanıcı yararı açısından red-team.
- **Design Learning:** Karar ve başarısızlıkları projede kanıtlı saklama.
- **Reference Intelligence:** Ekran ve videolarda kompozisyon, tipografi, spacing, ışık, kamera, motion ve state analizi.
- **Design DNA:** Görsel, kamera ve animasyon kararlarını bütün ajanlar için tek kaynağa sabitler.
- **Domain Specialists:** Swift/RealityKit, React Native/Flutter, web, Three.js, Unity/Godot ve video için uygun profil.
- **Game Design:** Core loop, iki farklı görev ritmi, pet/NPC, pathfinding, save/load, sinematik sahne ve hassas konu kuralları.
- **Adaptive Orchestration:** Ajan yetkinliği, efor, iş bağımlılıkları, worktree ve entegre QA.
- **Quality Gates:** Kanıtlanmış davranış, görsel sadakat, accessibility, cihaz performansı ve release kontrolü.

## Dosya yapısı

```text
skills/tasarim-vergisi/
├── SKILL.md
└── references/
    ├── catalog.md
    ├── reference-intelligence.md
    ├── finding-card.md
    ├── design-dna.md
    ├── domain-profiles.md
    ├── game-design.md
    ├── orchestration.md
    ├── task-brief.md
    ├── quality-gates.md
    ├── perception-engine.md
    ├── creative-reasoning.md
    ├── critique-council.md
    ├── motion-direction.md
    ├── design-learning.md
    ├── human-perception.md
    ├── empathy-simulator.md
    ├── surprise-architecture.md
    └── taste-lab.md
scripts/check_skill.py
scripts/idea_audit.py
scripts/experience_audit.py
scripts/tests/test_idea_audit.py
scripts/tests/test_experience_audit.py
examples/pet-game-human-lens.json
.github/workflows/validate-skill.yml
```

## Kurulum

Agent Skills destekleyen araçlarda:

```bash
npx skills add aliemrebuyukkol/tasarim-vergisi
```

Claude Code:

```bash
git clone https://github.com/aliemrebuyukkol/tasarim-vergisi /tmp/tv
cp -R /tmp/tv/skills/tasarim-vergisi ~/.claude/skills/
```

Codex CLI:

```bash
git clone https://github.com/aliemrebuyukkol/tasarim-vergisi /tmp/tv
mkdir -p ~/.codex/skills
cp -R /tmp/tv/skills/tasarim-vergisi ~/.codex/skills/
```

Gemini CLI/Antigravity/diğer araçlarda ilgili skills klasörü ve kökteki `AGENTS.md`/`GEMINI.md` yönlendirmesi kullanılabilir; kurulum desteği sürüme bağlıdır.

## Kullanım

> Tasarım vergisi: Swift + RealityKit ile sinematik, evcil hayvan eşlikli, metin tabanlı olmayan bir oyun tasarla. Referanslara sadık kal, çalışan dikey kesit oluştur ve cihaz testlerini kanıtla.

> Tasarım vergisi: Mevcut web uygulamamın onboarding ekranlarını analiz et, kaynakla aynı viewport'ta kıyasla, kritik kırılmaları düzelt.

Modlar: **araştırma / prototip / uygulama**. Uygulama modunda üretilen çalışma dosyaları, kapsam uygunsa `TASARIM-VERGISI.md`, `DESIGN-DNA.md`, `QUALITY-REPORT.md` ve `tasarim-vergisi/ornekler/` altında raporlanır.

## v5 yeni dosyalar

~~~text
scripts/evidence_core.py
scripts/evidence_lab.py
scripts/prototype_capture.py
scripts/evidence_suite.py
scripts/requirements-evidence.txt
scripts/tests/test_evidence_lab.py
examples/evidence-case.template.json
examples/prototype-capture.template.json
examples/project-evidence-suite.template.json
examples/product-visual-regression.workflow.example.yml
examples/human-study-template.csv
examples/prototype-demo/index.html
skills/tasarim-vergisi/references/empirical-evidence-loop.md
skills/tasarim-vergisi/references/evidence-tools.md
skills/tasarim-vergisi/references/user-research-protocol.md
~~~

## Statik skill testi

```bash
python3 scripts/check_skill.py
python3 -m unittest discover -s scripts/tests -v
python3 scripts/idea_audit.py examples/pet-game-directions.json
python3 scripts/experience_audit.py examples/pet-game-human-lens.json
```

Bu test yalnızca skill dokümanlarının yapısını doğrular. Gerçek oyun görsel sadakatini, FPS'yi veya App Store hazırlığını **kanıtlamaz**.

## İlkeler

Kanıtsız “test edildi”, “inceledim”, “çalışıyor”, “60 FPS” ve “yayına hazır” iddiası yok. Kaynak telif hakları korunur; izinsiz görsel, sprite, logo, metin veya bölüm kopyası yapılmaz. Test durumu `geçti`, `başarısız`, `engellendi` veya `uygulanamaz` olur.

## Lisans

MIT.

**Sınır:** “İnsan gibi görmek/düşünmek” bir hedef metaforudur; yapay zekâ insan bilinci veya gerçek göz izleme verisi elde etmez. Görsel analiz, yaratıcı hipotez ve doğrulama ayrı kapılardır.

## İnsansı algılama ne anlama gelir?

Skill'in kendisi insan değildir ve insanın gerçekten **ne hissedeceğini** bilemez. İnsan dikkat ve estetiği hakkında araştırma destekli, karşı hipotezli tasarım açıklamaları üretir; bunları gerçek kullanıcı gözlemi ve ölçümlerinden ayrı tutar. Daha sıra dışı fikri yalnızca yenilik için seçmez. **Özgünlük + anlam + uygulanabilirlik + kontrol + erişilebilirlik** birlikte aranır.

Örnek JSON: `examples/pet-game-human-lens.json`. Test: `python3 scripts/experience_audit.py examples/pet-game-human-lens.json`.
