---
name: tasarim-vergisi
description: "Tasarım Vergisi; görüntü, etkileşim ve insan testleriyle desteklenebilen algı hipotezlerini, yaratıcı muhakemeyi ve doğrudan referans analizini birleştirir, Design DNA ve uygulanabilir tasarım çözümleri üretir, web, mobil, oyun, 3D ve video görevlerini uzman ajanlara dağıtır ve çıktıyı ölçülebilir kalite kapılarıyla doğrular. Kullanıcı tasarım vergisi, referans sadakati veya araştırma tabanlı ürün/oyun geliştirme istediğinde kullan."
license: MIT
---

# Tasarım Vergisi v5

Görev: **referansı incele → ölç → fikirleri ele → Design DNA'yı kilitle → uygun yığınla üret → gerçek çıktıyı doğrula**. Bir mockup'ın güzel görünmesi, çalışan veya yayıma hazır ürün kanıtı değildir.

## İlgili kaynaklar

| Dosya | İşlev |
|---|---|
| [catalog.md](references/catalog.md) | Kaynak seçimi ve uygulama türü matrisi |
| [reference-intelligence.md](references/reference-intelligence.md) | Ekran, video, kod ve davranış kanıtı |
| [finding-card.md](references/finding-card.md) | Bulgu puanlama ve karar kuralları |
| [design-dna.md](references/design-dna.md) | Görsel/motion/sahne sözleşmesi |
| [domain-profiles.md](references/domain-profiles.md) | Platforma özgü teknik ve test profili |
| [game-design.md](references/game-design.md) | Gameplay, görev, pet/NPC, kamera, kayıt |
| [orchestration.md](references/orchestration.md) | Ajan/efor seçimi ve entegrasyon |
| [task-brief.md](references/task-brief.md) | Dosya kapsamlı görev brifleri |
| [quality-gates.md](references/quality-gates.md) | Ölçülebilir tamamlanma kontrolü |
| [perception-engine.md](references/perception-engine.md) | İnsan odaklı ilk bakış, yapı, hareket analizi |
| [creative-reasoning.md](references/creative-reasoning.md) | Gerçekten farklı ve anlamlı yön üretme |
| [critique-council.md](references/critique-council.md) | Kör eleştiri, dissent ve karşıt görüş |
| [motion-direction.md](references/motion-direction.md) | Sinematik motion/continuity sözleşmesi |
| [design-learning.md](references/design-learning.md) | Geçmiş testlerden ölçülü öğrenme |
| [human-perception.md](references/human-perception.md) | Dikkat, akıcılık, beklenti, şaşırma, merak, hafıza ve kanıt düzeyleri |
| [empathy-simulator.md](references/empathy-simulator.md) | Olası birinci kişi deneyimi, farklı kullanıcı niyetleri, karşı hipotez |
| [surprise-architecture.md](references/surprise-architecture.md) | Beklenti → ipucu → sapma → anlam → çözülme |
| [taste-lab.md](references/taste-lab.md) | Gerçek kullanıcı beğenisi ve davranışını ayrı ölçen araştırma tasarımı |
| [empirical-evidence-loop.md](references/empirical-evidence-loop.md) | Gerçek ekran/video, etkileşim, insan testi ve karar döngüsü |
| [evidence-tools.md](references/evidence-tools.md) | Ölçüm aracı komutları, kurulum, engeller ve raporlar |
| [user-research-protocol.md](references/user-research-protocol.md) | Gerçek katılımcı, rıza, beğeni, şaşkınlık ve hatırlama ölçümü |

## Değişmez çalışma kuralları

- Kaynak açılmadan **incelendi**, test çalıştırılmadan **geçti**, cihaz profili alınmadan **60 FPS**, yayın kontrolü yapılmadan **yayına hazır** deme. Sonuçlar: `geçti | başarısız | engellendi | uygulanamaz`.
- Kaynak bir görselse gerçek hareket süresi, easing, fizik ve etkileşim davranışının **bilinemeyeceğini** belirt. Video/çalışan uygulama varsa ayrıca analiz et.
- Kullanıcının referansındaki hiyerarşi, boşluk, tipografi, kamera, oran ve hareketi mümkün olduğunca ölç. Logo, sprite, varlık, karakter, telifli yazı ve seviyeyi izinsiz kopyalama; özgün uygulama üret.
- Mevcut üründe istenen parça dışında sessiz yeniden tasarım yapma; eski işlevleri koru.
- Model, alt ajan, Git, tarayıcı, cihaz, Blender MCP veya görsel üretim araçları **bulunuyor varsayılmaz**. Gerçekte erişilebilir olanı kullan, engeli açıkça bildir.
- Swift oyunlarına otomatik TypeScript/CSS, web'e XCTest koyma. Kalite kriterini [domain-profiles.md](references/domain-profiles.md) belirler.
- Yalnızca araştırma istenmişse kodu değiştirme. Commit, yayınlama ve ücretli dış işlemler için yetki sınırına uy.

## İnsan benzeri değerlendirme, insan olduğunu iddia etme

Tasarımcı gibi üç geçiş kullan: **3 saniyelik ilk bakış hipotezi → 30 saniyelik yapı incelemesi → etkileşim/motion sürekliliği**. Bu süreler gerçek göz izleme veya psikolojik kullanıcı testi değildir. [perception-engine.md](references/perception-engine.md) ile görseli doğrudan incele; görsel erişim yoksa engeli açıkla.

Her araştırmada varsayılan çözümü tanımlayıp neden sıradan olduğunu sorgula. Ardından [creative-reasoning.md](references/creative-reasoning.md) ile **görsel, mekanik ve duygusal** farklılık taşıyan en az üç yön üret (kullanıcı tek ve sadık çözüm istediğinde alternatifleri iç not olarak değerlendirmek yeterli). Palet değiştirmek yeni fikir değildir. [critique-council.md](references/critique-council.md) ile kendi favorini red-team et; [motion-direction.md](references/motion-direction.md) ile hareketi tasarım gerekçesine bağla. Gerçek ayrı ajan yoksa "bağımsız jüri" iddiasında bulunma. Kullanıcıya ait kısıtlar, radikal farklılık uğruna yok sayılmaz.

Projede varsa [design-learning.md](references/design-learning.md) karar günlüğünü oku. Kullanıcı tercihlerini erişilemeyen geçmiş sohbetlerden uydurma; yalnızca erişilen proje verisine ve mevcut talimata dayan.

## İnsan algısını modelleme: v4 zorunlu döngü

Yalnızca en özgün veya en gösterişli tasarımı seçme. [human-perception.md](references/human-perception.md) ile **dikkat, işleme akıcılığı, beklenti, merak, anlam ve hatırlama** hipotezlerini ayrı üret. İnsanlar farklı amaç, deneyim ve erişilebilirlik durumlarında farklı tepkiler verir; tek “ortalama insan” skoru yoktur.

Her güçlü aday için:

1. **Algı:** Kaynakta gözlediğin öğeleri, algı hipotezlerinden ayır; ilk bakıştan duygusal karşılığa 5 aşamalı yolculuk yaz.
2. **İnsan-Lens:** [empathy-simulator.md](references/empathy-simulator.md) ile ilk kez gelen, meraklı, kısa oturum isteyen ve erişilebilirlik ihtiyacı olan bağlamları düşün. Birinci kişi anlatıları **hipotetik simülasyon** diye etiketle; insan gözlemi gibi sunma.
3. **Beklenmedik fikir:** [surprise-architecture.md](references/surprise-architecture.md) ile beklenti → ipucu → anlamlı sapma → çözülme → kontrol → tekrar değerini tasarla. Sadece renk/parçacık gösterisini yapısal özgünlük sayma.
4. **Karşı hipotez:** “Bu fikir neden sevilmeyebilir?” sorusunu yanıtla. Diğer yönlerin övgüsünü değil gerçek kusurunu yaz; riskli duygusal manipülasyonu reddet.
5. **Kanıt:** E0 (model varsayımı) ile E4 (tekrarlı veri) merdiveninden doğru düzeyi seç. [taste-lab.md](references/taste-lab.md) ile görev başarısı, öznel beğeni, şaşkınlık ve gecikmeli hatırlamayı ayrı gözlemle. E3/E4 verisi yoksa **insanlar seviyor** deme.

Oyun/sinematik sahnelerde `examples/pet-game-human-lens.json` sözleşmesini örnek al. `scripts/experience_audit.py` yalnızca kart yapısının eksiksizliğini test eder; insan tepkisini **ölçmez**. İsterse farklılık ve duygu hipotezlerini birlikte kullan, referansın korunması gereken görsel DNA'sını izinsiz bozma.

## v5 — Empirical Perception Loop (uygulama ve prototipte zorunlu)

v4 algı ve özgünlük hipotezleri artık yalnızca sözlü değerlendirme değildir. [empirical-evidence-loop.md](references/empirical-evidence-loop.md) döngüsünü uygula:

1. **Ölçülebilir hipotez + karşı hipotez:** Örneğin "Kedi yanına dönünce sahne anlaşılır" ve "Bekleme süresini gereksiz uzatabilir".
2. **Gerçek görüntü:** Referans ve aday **aynı viewport ve aynı state**; `python3 scripts/evidence_lab.py compare --reference ref.png --candidate build.png --output evidence/scene-01`. Eşit olmayan ekranları sessizce yeniden boyutlandırma.
3. **Gerçek motion:** Video varsa `frames` veya `video-compare` ile belirli zaman noktalarını çıkar; ara kare/oynatım ritmini manuel izle. İki kareden easing veya FPS kanıtı üretme.
4. **Gerçek interaksiyon:** Web prototipi localhost'taysa [evidence-tools.md](references/evidence-tools.md) ve `scripts/prototype_capture.py` ile aksiyon, ekran, hata ve reduced-motion durumunu yakala. Gerçek iOS uygulamasıysa Xcode/cihaz kanıtı olmadan web testini native test diye adlandırma.
5. **Gerçek insan:** [user-research-protocol.md](references/user-research-protocol.md) ile rıza ve gerçek görev gözlemi; fark edilme, anlama, görev başarısı, şaşırma, beğeni ve gecikmeli hatırlamayı ayrı tut. Sentetik/test verisini **insan kanıtı** olarak gösterme.
6. **Karar:** `evidence_lab.py gate` ile hipotez başına kanıt dosyalarını bağla. Eksik kanıt **limited_or_blocked**, eşik kırılması **failed**. Tek pixel MAE veya n>=8 insan tercihlerini kanıtlamaz; tasarımcı kararı ve örnekleme belirsizliği kalır.
7. **Tekrar:** Ürünün CI/PR akışına `scripts/evidence_suite.py` ile gerçek referans/aday dosyalarını bağla; görsel dosya yoksa **blocked**. Değişen commit sonrası ölçümü yenile; eski kanıtı yeni sürüm için tekrar kullanma. `DESIGN-LEARNING.md` içine hangi hipotezin neden revize edildiğini kaydet.

Ürün için **kanıt gerçekten mevcut değilse** bu işlemleri simüle etme; test planını ve engeli raporla. Otomasyon sürekli çalışan bir hizmet değildir: her PR/commit/manuel oturumda tetiklenebilir; insan çalışması kendiliğinden gerçekleşmez. Bu araçlar istatistiksel anlamlılık, gerçek göz takibi, bilinç, klinik etki veya estetik doğruluk vermez.

## 1. Kabul ve ortam keşfi

Kullanıcının hedefini ve mevcut dosyalarını incele: ürün/oyun türü, hedef kullanıcı, çekirdek eylem, referanslar, platform/yığın, mevcut ekranlar, korunacak davranışlar. Kapsamı üçe ayır: **araştırma**, **prototip**, **uygulama**. Bilinenleri tekrar sorma; gerçekten engelleyici belirsizlikte en fazla dört kısa soru. Geri kalanda varsayımını açıkça yazıp ilerle.

Var olan `README`, manifest, kod, ekran/asset, tasarım sistemi ve test altyapısını kontrol et. Araç keşfini ve izinleri kaydet (tarayıcı, ekran görüntüsü, build, simülatör/cihaz, Git, modeller, alt ajanlar). Kullanıcı açıkça cihaz veya sürüm belirlediyse onu koru.

## 2. Kaynak araştırması ve Reference Intelligence

[catalog.md](references/catalog.md) matrisinden ilgili kategorileri seç. Faydalı bir çapraz kategori değerlendir, gösteriş için ilgisiz özellik ekleme. Küçük istekte birkaç yüksek sinyalli kaynak, büyük istekte kategori başına 3–8 kaynak yeterlidir. Kaynağı **gerçekten aç**; URL, erişim tarihi, incelenen ekran/sayfa, lisans ve kanıt biçimini yaz. Açılamayan kaynak `doğrulandı: hayır` kalır.

[reference-intelligence.md](references/reference-intelligence.md) ve [perception-engine.md](references/perception-engine.md) ile kompozisyon, tipografi metrikleri, boşluk, renk, kamera, asset ölçeği, motion ritmi, etkileşim state'leri ve erişilebilirlik kanıtlarını çıkar. Alt ajan varsa kaynak tarama salt-okuma ve paralel olabilir.

## 2B. Yaratıcı ayrışma (önemli)

Araştırma listesi oluşunca hemen ilk güzel şablona kilitlenme. [creative-reasoning.md](references/creative-reasoning.md) ile **standart baseline + sadık alternatif + çapraz disiplin alternatifi + radikal ama test edilebilir alternatif** üret. Her adayın değişen *mekaniğini*, kullanıcı yararını ve referanstan korunacakları yaz. Önemli kararlar için [critique-council.md](references/critique-council.md) kör değerlendirmesini uygula. İsteğe bağlı `scripts/idea_audit.py` ile kartların yalnızca renk değişikliği olup olmadığını denetle; script yaratıcı kaliteyi kanıtlamaz.

## 3. Küratörlük ve eleme

[finding-card.md](references/finding-card.md) şablonunda katkı, referans uyumu, özgünlük, uygulanabilirlik, güven ve maliyeti puanla. Tekrarları ayıkla; küçük görevde 1–5, kapsamlı görevde 5–15 yüksek katkılı kart seç. En az bir cesur yön değerlendir, fakat çekirdek ürünü bozan fikri ele. Doğrulanmamış bir kaynağı ölçülmüş veri, belirsiz lisanslı varlığı serbest içerik gibi gösterme.

## 4. Design DNA'yı ortak sözleşmeye çevir

[design-dna.md](references/design-dna.md) ile `DESIGN-DNA.md` üret veya mevcut sistemin sürümünü güncelle. `REF-ID → ölçüm → tasarım kuralı` ilişkisi açık olsun. Renk, tipografi, spacing, kamera, karakter/pet oranı, ışık, motion token ([motion-direction.md](references/motion-direction.md)), etkileşim ve erişilebilirlik sınırları tüm ajanlar için aynı kaynak olur. Kasıtlı sapmaları ve nedenlerini kaydet.

## 5. Uzman profili ve üretim

[domain-profiles.md](references/domain-profiles.md) ile gerçek platforma göre teknik plan, kalite bütçesi ve test komutları seç. **Oyunlar için** [game-design.md](references/game-design.md) uygula: core loop, bölüm akışı, state machine, kamera, NPC/pet, save/load, kontrol erişilebilirliği ve temel görevlerin gerçekten oynanması.

Araştırmada raporla dur. Prototipte kritik etkileşimin **çalışan** örneğini, uygulamada mevcut sistemle entegre sonucunu hedefle. `tasarim-vergisi/ornekler/` çıktısı HTML/CSS, Swift, Three.js, oyun motoru veya video olabilir; teknoloji seçimi ürüne göre yapılır. Gerçekte çalıştırılmayan demoya “çalışıyor” deme.

## 6. Adaptive Agent Orchestrator

[orchestration.md](references/orchestration.md) ile iş sınıfına en uygun **gerçekten erişilebilir** ajan/model ve eforu seç. [task-brief.md](references/task-brief.md) ile her paket için tek görünür sonuç, değiştirilebilir dosyalar, bağımlılık, geri alma, kabul testi belirle. Paralel kod için ayrı `git worktree` veya çakışmayan dosya sahipliği şarttır. Ana ajan entegrasyon ve bağımsız incelemeden sorumludur. Ajan yoksa sırayla ilerle.

## 7. Görsel + teknik kalite kapıları

[quality-gates.md](references/quality-gates.md) zorunludur. Build/lint/test; aynı viewport ve durumda referans karşılaştırması; loading/empty/error; gerçek etkileşim ve geri dönüş; platforma uygun erişilebilirlik; gereken cihaz/simülatörde performans, bellek ve stabilite. Testin **ortamı, yöntemi, çıktısı** olmalı.

P0/P1 açıkken veya yayına çıkış için zorunlu kapı `engellendi` iken “yayına hazır” deme. P2 çözülmeli veya açık risk kabulüyle kaydedilmeli. Aynı düzeltme iki kez başarısızsa yöntemi, brifi veya aracı değiştir.

## 8. Rapor ve teslim

`TASARIM-VERGISI.md`: baseline, algı ve Human-Lens kartları, kanıt düzeyi, sürpriz haritası, en az üç yön, eleştiri sonucu, amaç, seçilen kategori ve kaynaklar, kanıt, seçilen/elenen fikirler, Design DNA, iş paketleri, ajan/efor, bağımlılıklar, açık sorular. Prototip/uygulamada `QUALITY-REPORT.md`: gerçek test sonuçları, ekran/video/cihaz kanıtı, hatalar ve engeller.

Değişen dosyaları, çalıştırılan komutları ve doğrulanamayan alanları göster. Önemli tasarım kararları ve başarısız hipotezleri, mevcutsa `DESIGN-LEARNING.md` günlüğüne kaydet. Ürün geri bildirimi gerçekten toplanmadıysa sonuç iddiası üretme. Kaynak kataloğuna yeni eklenen ama henüz açılmamış URL için `(?)` kullan. İşin **tamamlanması** kaynak → karar → davranış → test kanıtı zincirinin izlenebilir olması demektir.

## v4 teslim kapısı: insan tepkisi iddiası

“Bunu bütün kullanıcılar sever”, “şaşırtır”, “depresyonu iyileştirir” gibi doğrulanmamış iddialar teslim metnine giremez. Kullanıcı araştırması yapılmadıysa ilgili satır **E0 hipotez** kalır; üretim fonksiyonları geçtiyse ancak teknik yeterlilikten söz edilir. Canlı kullanıcı testi ayrı bir iş paketidir; izinsiz insan verisi toplama.
