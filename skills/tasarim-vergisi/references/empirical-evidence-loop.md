# v5 Empirical Evidence Loop — referans → prototip → insan → karar

Tasarımcının görevi “insanların bunu seveceği” iddiasını üretmek değil; **bu iddiayı sınanabilir ve çürütülebilir hale getirmek**. Bu akış geçmiş v4 Human Perception, Empathy Simulator ve Taste Lab kartlarını gerçek kanıtla birleştirir.

## Zorunlu yedi aşama

1. **Algı hipotezini yaz:** “Oyuncu durursa kedi yanına döner; bu davranış fark edilir ve güvenli bir eşlik hissi yaratabilir.” Aynı anda karşı hipotez: “Yavaş animasyon bekleme hissini artırabilir.”
2. **Referansın durumunu kaydet:** URL, ekran/video, hedef viewport, zaman noktaları, lisans, referansın ekranda gerçekten ne gösterdiği; kaynak görüntüsü yoksa **engellendi**.
3. **Çalışan prototipi yakala:** kullanıcı eylemleriyle başlangıç, aktif, tamamlanma, loading/error, reduced motion ve dokunma/klavye durumlarını gözlemle. İlgili araç yoksa raporda **engellendi**.
4. **Görsel ve zaman karşılaştırması:** `evidence_lab.py compare`, `frames`, `video-compare`; görüntüler aynı viewport ve aynı durumla eşleşmeli. Görsel fark tek başına kalite veya duygu ölçümü değildir.
5. **Gözlem protokolünü uygula:** gerçek insanın görevi fark etmesi, anlaması, tamamlaması, öznel beğenisi, şaşırması ve 24 saat sonra hatırlaması ayrı değerlendirilir. Önce gönüllü rıza, sonra görev. Kullanıcı adına cevap uydurma.
6. **Karar kapısı:** `evidence_lab.py gate` teknik kanıtın varlığını, eşikleri ve gerçek insan gözlem raporunu kontrol eder. Kanıt eksikse `limited_or_blocked` döner. Teknik görüntü ölçümü ve kullanıcı beğenisini aynı sayı altında toplama.
7. **Öğrenme kaydı:** hipotez, karşı hipotez, veri, karar ve sapmanın sebebini sürüm kontrolüne yaz. Bu, modelin kendiliğinden yeniden eğitilmesi değildir; ajan sonraki iterasyonda kayıtları okuyabilir.

## Kanıt biçimleri ve sınırları

| Kanıt | Ölçülebilen | Ölçülemeyen / dikkat |
|---|---|---|
| PNG referans + aday | piksel farkı, kaba fark bölgeleri, kenar farkı | estetik haz, insanın dikkati, sebep, duygu |
| Referans video + aday video | seçilmiş zamanlarda sahne/kare farkı | tüm kareler, gerçek easing, ses ritmi, izleyici algısı |
| Tarayıcı etkileşim senaryosu | seçili eylem, hedef metin, console/pageerror, ekran | mobil cihaz GPU, dokunma hissi, App Store uygunluğu |
| Katılımcı gözlemleri | görev başarı oranı, fark etme, beğeni, öznel şaşırma, takip eden gün hatırlama | evrensel tercih, nedensellik veya klinik fayda |
| Kullanıcı görüşmesi | neden yorucu/şaşırtıcı/sevilebilir görüldüğüne dair anlatı | istatistiksel temsil; tek kişi bütün kullanıcılar değildir |

## Karar kartı

```
Case ID / Hipotez / Karşı hipotez:
REF-ID, kaynak türü, viewport ve t:
Aday sürüm, commit, target device:
Teknik kanıtlar: dosya + sha256 + yöntem
Gerçek insan gözlemi: katılımcı sayısı, rıza, görev ve örnekleme
Öngörülen etki / gözlenen etki / alternatif açıklama:
Görüntü farklılıklarının nedenleri:
Karar: koru | revize et | farklı yön dene | engellendi
Evidans seviyesi: E0 (hipotez) → E2 (pilot) → E3 (yapılandırılmış insan verisi) → E4 (tekrarlı araştırma)
Açık risk, sahip, sonraki test:
```

## Önemli kısıtlar

- **Görsel model bir göz izleme cihazı değildir.** Gerçek fixation/saccade ölçülmediğinde “ilk bakışta buraya baktılar” deme; “gözü çekmesi beklenen odak” de.
- Pixel MAE yüksekliği bazen basit aydınlatma veya anti-aliasing farkıdır, düşük MAE ise kötü kullanılabilirliği gizleyebilir. İnceleyiciye bölgesel fark raporu ve görüntüleri göster.
- “8 kişi” eşiği otomatik olarak istatistiksel anlamlılık yaratmaz; minimum pilot eleme ölçütüdür. Kullanıcıların gerçek hedef kitlenin çeşitliliğini temsil edip etmediğini ayrı değerlendir.
- Videonun bir kaç karesini görmek FPS veya fizik doğrulaması değildir. iOS/RealityKit için cihaz videosu ve profiler gerekiyorsa platform uzmanına görev ver.
- Kullanıcı sahnesini bir kez görüp beğendiğini söylüyorsa 24 saatlik hatırlama otomatik çıkarılamaz; eksik olarak bırak.
- Kullanıcı verisini izinsiz toplama, kimlik veya sağlık geçmişini repoya ekleme, ham kayıtları public CI artefaktına yükleme.
- Otomatik test tekrarları ancak yeni commit veya manuel çalıştırma ile mümkündür; ajan arka planda sürekli veri toplamıyor.

## Otomasyonda durum

- Otomatik statik/ünite testleri her PR'da çalışabilir.
- Proje özelinde **gerçek ekran** alacak akış, app'in canlı/test URL'si ve tarayıcı kuruluysa başlatılır.
- CI'da referans ekranı ve prototip ekranı sağlamadan “görsel regresyon geçti” yazılamaz.
- İnsan çalışması harici ve açık rıza ile yürütülür; CI bunu modelleyemez.

## Projeye bağlanan sürekli regresyon

Ürün repo'sunun ekran/klip üretim komutu ve aynı viewport/state baseline dosyaları varsa `scripts/evidence_suite.py` ile tek bir JSON senaryo listesinden her PR'da yeniden karşılaştırma yap. Eksik ekran veya sıfır senaryo `blocked` olarak kapanır. `technical_checks_passed_manual_review_required` **insan onayı** veya yayın onayı değildir. Örnek: `examples/project-evidence-suite.template.json`; ürün CI şablonu: `examples/product-visual-regression.workflow.example.yml`. Referansları kullanıcı izni olmadan otomatik kopyalama veya public artefakt olarak yayma.
