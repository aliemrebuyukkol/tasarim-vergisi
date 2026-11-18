# Reference Intelligence: görsel ve davranış analizi

Bir kaynağı araştırmış saymak için ilgili ekranı, videosunu, kodunu veya canlı demosunu **doğrudan incele**. Sadece başlık, Pinterest bağlantısı veya README tanıtımından kamera, hareket ve performans bilgisi çıkarma.

## Kanıt kaydı

```text
REF-ID:
URL/dosya, sürüm, erişim zamanı:
İncelenen tam ekran, video aralığı veya kod konumu:
Kanıt tipi: screenshot | video | demo | kaynak kod | doküman
Doğrulandı: evet | kısmi | hayır
Görülen ölçüler:
Çıkarımlar (ayrı):
Eksik kanıt ve erişim engeli:
Telif/lisans ve varlık kullanım izni:
```

## Analiz boyutları

| Boyut | Kaynakta ölçülecek | Uygulamada kilitlenecek |
|---|---|---|
| Kompozisyon | odak, hizalama, boşluk, görsel ağırlık | grid/yerleşim oranları |
| Tipografi | font, ağırlık, x-height hissi, satır yüksekliği, tracking | tipografi token'ları |
| Renk/ışık | palet, kontrast, malzeme, gölge, ışık yönü | semantik renk ve lighting |
| Kamera | perspektif/ortografik, açı, FOV/ölçek, takip | kamera rig, clipping ve kadraj |
| Karakter/asset | ekrandaki oran, silüet, detail density, merkezleme | asset manifest ve min görünürlük |
| Motion | başlangıç/bitiş, süre, easing, spring, stagger, parallax | motion durum diyagramı |
| Etkileşim | input, dokunma/klavye, hover/focus, geri dönüş | UI/gameplay state machine |
| Responsive/a11y | safe area, ekran oranı, reduced motion, okunurluk | farklı viewport kabulü |

**Statik ekrandan süre, easing, fizik veya FPS doğrulanamaz.** Video varsa zaman kodu/kare örnekleri yaz. Canlı ürün varsa gezinme ve hata durumlarını test et. Görsel yoksa tahmini öğeyi `varsayım` olarak işaretle.

## Sadakat karşılaştırması

1. Referans ve hedefi **aynı viewport, aynı sahne, aynı UI state** ile yakala.
2. Ölçülebilir sapmayı kaydet: odak, oran, hizalama (gerekirse 1–2 px), boşluk, kamera, katman, okunurluk, varlık büyüklüğü.
3. Motion için başlangıç, ara ve bitiş karelerini kıyasla; salt ekran görüntüsü motion doğrulaması değildir.
4. Her sapmaya `hata` veya `bilinçli iyileştirme` de ve ikinciyi gerekçelendir.
5. Kaynağın izinsiz varlıklarını kopyalama; biçimsel ilkeyi, tasarım ritmini ve etkileşim mantığını özgün üret.

Erişilebilirliği bozan referansı körlemesine tekrarlama: örneğin 24 px görsel buton korunabilir ama dokunmatik hedef genişletilmelidir.
