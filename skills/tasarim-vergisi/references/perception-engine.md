# Perception Engine — önce gör, sonra yorumla

Amaç: İnsan görüşünü veya bilincini taklit ettiğini iddia etmeden, bir tasarımcının **ilk bakış, dikkat, anlamlandırma ve ayrıntı** aşamalarını disiplinli analiz adımlarına dönüştürmek. Yalnızca yazıyla tarif edilmiş bir görsele “baktım” deme. Görsel erişimi yoksa süreç **engellendi**.

## Görsel inceleme üç geçiş

### P1 — İlk bakış, 3 saniyelik algı hipotezi

Ekranı **metinleri okumadan ve yakınlaştırmadan** değerlendir. Tahmin edilen ilk dikkat noktalarını, görsel kütleleri, kontrast sırasını, sıcak/soğuk baskınlığı, boşluğun işlevini, başlıca eylemi ve duygusal tonu tarif et. Bu gerçek kullanıcı göz izleme ölçümü **değil**, denetlenebilir bir tasarımcı hipotezidir. “İlk 3 saniyede kesin şuraya bakılır” deme.

Çıktı: 3–5 öğelik dikkat sıralaması; önemli alanlar için konum/oran; ilk his ve amacı ileten görsel öğeler. Alışılmadık alanlar veya bakışı kesen unsurlar not edilir.

### P2 — 30 saniyelik yapı okuması

Görseli bölgelere ayır: foreground/background, kahraman/ikincil öğeler, grid, renk grupları, whitespace, typographic rhythm, occlusion, bilgi yoğunluğu, tutarlı ekran ölçeği. 2D/3D için kamera, takip, perspektif, ışık yönü, yakınlık/derinlik, silüet ve okunabilir pet boyutunu da ölç.

Çıktı: **sahne grafı** veya arayüz bileşen ağacı; bölge/işlev bağlantıları, referansın korunması gereken geometrik imzası. Kullanıcı işini tamamlamak için neye bakmalı, neyi kaçırabilir?

### P3 — Hareket, etkileşim ve süreklilik

Video veya canlı örnek varsa birincil etkileşim için **önce/sırasında/sonra** üç kare veya durum yakala. Hareketin nedeni, hareket yolu, süre, easing, stagger, overshoot, kamera sürekliliği, eylem-geri bildirim ilişkisi ve reduced-motion karşılığı. Yalnızca statik ekran varsa burada süre, fizik ve gerçek kullanıcı davranışı **bilinmiyor** yazılır.

Çıktı: kısa state transition tablosu, süre/kare kanıtı, olası olumsuz durumlar (loading, hata, görünürlük, occlusion, geri dönüş).

## Çoklu perspektifli gözlem

Aynı tasarımı aşağıdaki bağımsız merceklerle değerlendir:

| Mercek | Sorduğu soru |
|---|---|
| İlk kez gören kişi | Üç saniyede ne olduğu anlaşılır mı? |
| Görsel tasarımcı | Kompozisyon, tipografi ve boşluk dengeli mi? |
| Motion tasarımcısı | Eylem, ritim ve geçişler fiziksel olarak tutarlı mı? |
| Oyun/sahne tasarımcısı | Oyuncu hedefi, kamera, karakter/pet görünürlüğü net mi? |
| Erişilebilirlik denetçisi | Kontrast, motion, touch target ve bilişsel yük güvenli mi? |

Bir mercekten gelen yargıyı diğerinin bulgusuymuş gibi göstermeden ayrı yaz. Birden fazla model gerçekten yoksa bütün mercekleri **tek modelin hipotetik rolleri** olarak etiketle, bağımsız onay uydurma.

## İsteğe bağlı araç desteği

- Görsel yetenekli model: sahne/bileşen ilişkileri ve görsel hiyerarşi hipotezleri.
- Ekran görüntüsü + piksel ölçüm script'i: bounding box, hizalar, ölçek, renk kontrastı.
- Video frame extraction: hareket öncesi/sonrası, süre ve kadraj karşılaştırması.
- CV saliency / segmentation / embedding: yalnızca araç mevcutsa dikkat/benzerlik **yardımcı kanıtı**; insan gözü veya kullanıcı araştırmasının yerine geçmez.
- DOM/semantics/browser/cihaz testleri: gerçek etkileşim ve erişilebilirlik doğrulaması.

## Görsel kanıt kartı

```text
REF-ID ve kaynak (URL/ekran/zaman damgası):
Ekran/video/DOM gerçekten görüldü mü?:
Viewport / cihaz / kamera:
İlk bakış hipotezi: [1,2,3]
Görsel yapı ve öğeler arası ilişkiler:
Dikkat dağıtan/örtülen öğeler:
Motion durumları ve süre kanıtı:
Duygusal atmosfer (tasarım yorumu; kullanıcı testi değil):
Bilinen / çıkarım / bilinmeyen ayrımı:
Ölçülebilir tasarım aktarımı:
``` 

Bu kart, [reference-intelligence.md](reference-intelligence.md) ve [design-dna.md](design-dna.md) dosyalarının girdisidir. Kaliteli fikir üretebilmek için önce bu kartı referans başına tamamla.
