# v5 Evidence Toolchain — gerçek kullanım

## Bağımlılık ve erişim

- Python 3.10+ ve `Pillow>=10` görsel karşılaştırması için.
- Sistem `ffmpeg` + `ffprobe` video kareleri için.
- `pip install playwright` ve tarayıcı ikilisi prototip etkileşim yakalama için. Tarayıcı kurulu değilse **engellendi**; boş ekranla geçme.
- Kod, video ve insan verileri yerelde kalır. CLI otomatik upload, özel dosya toplama veya telemetri yapmaz.

`pip install -r scripts/requirements-evidence.txt`

## Ekran karşılaştırması

`python3 scripts/evidence_lab.py compare --reference ref.png --candidate build.png --output evidence/scene-01`

**Çıktı:** `overlay.png`, güçlendirilmiş `diff.png`, `report.json`; viewport, SHA-256, RGB ortalama hata, değişen piksel oranı, kenar farkı ve en farklı kaba bölgeler. Ekran ölçüleri farklıysa otomatik yeniden boyutlandırılmaz, test engellenir. Bu metrikler görsel kalite/insan algısı puanı değildir.

## Video

`python3 scripts/evidence_lab.py frames --video scene.mp4 --timestamps 0,0.5,1.2 --output evidence/frames`

`python3 scripts/evidence_lab.py video-compare --reference source.mp4 --candidate build.mp4 --timestamps 0,0.5,1.2 --output evidence/motion`

Zaman damgaları artan sırada olmalı, her iki klipte bulunmalı. Seçilen kareleri karşılaştırır, **arada kaçırılan kareleri**, ses/efekt ritmini veya kamera hareketinin izleyicideki duygusal etkisini kanıtlamaz. Bunlar ayrıca manuel video incelemesi ve kullanıcı testi gerektirir.

## Tarayıcı etkileşimlerinin gerçek yakalanması

`python3 scripts/prototype_capture.py --config examples/prototype-capture.template.json --output evidence/browser`

Varsayılan yalnızca **localhost** URL'sine gider; localhost sayfasının uzak CDN, telemetri ve redirect istekleri de engellenir. Uzak varlıklara bağımlı prototiplerde açık yetkiyle `--allow-remote` gerekir. Kullanıcı test yetkisi verdiği uzak URL için `--allow-remote` kullanabilir. JSON adımları: `click`, `fill`, `press`, `wait_visible`, `expect_text`, `screenshot`, `scroll`, `offline`, `wait_ms`. Keyfi JS komutu desteklenmez. Browser console/pageerror, ağ hatası ve beklenti uyumsuzluğu fail'dir. `capture.json` ile gerçek screenshot dosyalarını raporlar. Demo: `python3 -m http.server 8000 --directory examples/prototype-demo`.

## İnsan testi

`python3 scripts/evidence_lab.py study --csv local-participants.csv --output evidence/study.json`

Boş CSV veri değildir; hata verir. `examples/human-study-template.csv` yalnızca başlıktır. CSV gerçek kullanıcıdan rızayla doldurulur; public repoya eklenmez.

## Hipotez kapısı

`python3 scripts/evidence_lab.py gate --manifest examples/evidence-case.template.json --output evidence/gate.json`

Manifest `technical_evidence` içine üretilmiş `report.json`, `video_report.json` veya `capture.json` dosyalarını belirtir. `human_evidence.report` gerçek katılımcı analiz raporuna bağlanır. `gate` bir iddiayı başarı olarak ilan etmez; teknik dosyalar yoksa veya insan gözlemi eksikse exit 3 döner. Kanıtlar için dosya hash'leri kaydedilir.

## Sürekli doğrulama, doğru kullanım

Her kod değişikliğinde **mevcut** karşılaştırma senaryosunu ve testlerini yeniden çalıştır. Üretilen önce/sonra görüntülerine işaret eden raporun sürüm/commit ID'sini yaz. Kullanıcı çalışmasını yalnızca gerekli olduğunda ve rızayla tekrarla; CI'da kullanıcı testlerini sahteleştirme. Yeni tasarımda eski kanıtı yeni sürüm başarısı gibi kullanma.

## Her commit/PR'da gerçek görüntü regresyonu (ürün repo'suna entegre et)

`python3 scripts/evidence_suite.py --config examples/project-evidence-suite.template.json --output evidence/ci`

Bu şablonun işaret ettiği ekran dosyaları **hazır gelmez**; ürün repo'sunun render-test/screenshot üretim aşamasında gerçekten oluşturulmalıdır. Araç ekran yoksa **blocked** ve exit 3, eşiği aşarsa **failed** ve exit 3 verir. Sıfır senaryo exit 2 ile reddedilir. Gerçek görüntü varsa teknik eşik geçtiğinde bile `technical_checks_passed_manual_review_required` der. İnsan beğenisi kanıtı değildir.

Ürüne göre CI örneği: `examples/product-visual-regression.workflow.example.yml` (otomatik çalışabilmesi için ürünün gerçek test komutlarına uyarlanmalı). Böylece her PR'da daha önce onaylanmış referans ile yeni çıktı karşılaştırılabilir; referans görüntülerini otomatik üretmeden veya onların doğru UI durumunda olduğunu kontrol etmeden başarı iddiası yoktur.
