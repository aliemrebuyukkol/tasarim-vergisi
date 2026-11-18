# Tasarım Vergisi ajan yönergesi

Kullanıcı "tasarım vergisi", referanslardan özellik toplama veya referans temelli ürün/oyun araştırması istediğinde `skills/tasarim-vergisi/SKILL.md` dosyasını ve ilgili referansları oku.

Önce projenin gerçek yığınını, sürümünü, görsellerini ve araç erişimlerini denetle. Referansın ölçülmüş kompozisyon, motion, kamera ve etkileşim kurallarına sadık kal; yetkisiz yeniden tasarım yapma. Kaynağı açmadan inceleme, komutu çalıştırmadan test başarısı, cihaz olmadan FPS, doğrulanmayan entegrasyon için araç varlığı iddia etme.

Platform kuralları `references/domain-profiles.md` içindedir. Oyunlarda ayrıca `references/game-design.md`, ajan atamada `references/orchestration.md`, teslimde `references/quality-gates.md` uygulanır. Test durumları `geçti | başarısız | engellendi | uygulanamaz`.

Yaratıcı işlerde perception-engine.md ile ilk bakış/struktur/motion analizini yap; creative-reasoning.md ile sıradan baseline ve en az üç yapısal farklı yön düşün; critique-council.md ile öneriyi çürütmeye çalış. Design-learning.md ile ölçülmüş kararları sakla. İnsan testini veya bağımsız model değerlendirmesini uydurma.

İnsan algısı ve estetik tercih iddialarını E0-E4 kanıt düzeyiyle işaretle; ilk kişi anlatıları test edilmemiş simülasyondur. Sürprizin sahne/anlatı ile anlamlı bağı ve kullanıcı kontrolü açık olmalı. Klinik veya evrensel beğeni iddiası uydurma. `scripts/experience_audit.py` yalnızca statik kart kontrolüdür.

## v5: gerçek deney kapısı

Yaratıcı iddiaları insan tepkisi yerine geçirme. [empirical-evidence-loop.md](skills/tasarim-vergisi/references/empirical-evidence-loop.md) ile ekran/video/etkileşim kanıtı topla; kullanıcı beğenisi için gerçek, gönüllü ve kimliksizleştirilmiş çalışma iste. `scripts/evidence_lab.py` ve `scripts/prototype_capture.py` kullanıcıya ait gerçek dosya/URL verilmeden test yapılmış gibi gösterilemez. Kullanıcı verisi veya referans görüntüleri public GitHub'a otomatik yüklenmez.
