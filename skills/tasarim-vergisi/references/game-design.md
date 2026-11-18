# Game Design Specialist: oynanabilirlik ayrı doğrulanır

Oyunlar için görsel araştırma **yeterli değildir**. Bir karakterin yürüyebilmesi, görev veya hikâyenin çalıştığı anlamına gelmez.

## 1. Çekirdek deneyim

- Oyuncu ilk **30 saniyede** ne yapar, **3 dakikada** ne hisseder, **30 dakikada** ne keşfeder?
- `Eylem → geri bildirim → dünyada/durumda değişim → yeni eylem` döngüsünü yaz.
- Kontroller: hareket, kamera, etkileşim, pet çağırma, geri/çıkış, pause/skip, alternatif kontrol.
- Metin tabanlı olmayan oyunda hedef görsel/ses/animasyonla sezilir; görev sadece gizli talimatlara bağlı değildir.
- Gösterişli fakat pasif sinematik yerine oyuncunun kontrolü nerede aldığı/kaybettiği bilinçli tasarlanır.

## 2. Bölüm/sahne kartı

```text
Bölüm ID, hedef süre, duygusal ve oynanış amacı:
Mekân, kamera, ışık, müzik ve çevre:
Oyuncunun 1–3 temel eylemi:
Pet/NPC davranışı ve görünür geri bildirim:
Başlangıç → input → sonuç → devam state'leri:
Yanlış/eksik eylem, yardım, skip ve tekrar:
Varsa seçimlerin somut etkileri:
Erişilebilirlik (ses kapalı, altyazı, duyusal seçenek):
Checkpoint, save/load, tekrar oynanabilirlik:
Asset bağımlılıkları, kabul testi ve riskler:
```

Hikâye dallanmalarında bütün düğümlerin ayrı içerik vermesi gerekmiyor; **anlamlı sonuçları** olan yeniden birleşen yollar kur. Dallanma sayısı üstel büyürken gereksiz bölüm üretme.

## 3. Karakter ve pet/NPC

Durum makinesi: `follow → approach → wait → explore → interact → return/rest`. Animasyon geçişleri, pathfinding/navmesh, hız, avoidance ve collision tanımlansın. Görünürlük/camera/occlusion testleri: ağaca/koltuğa takılma, ekran dışına kaçma, çok küçülme, behind-camera. Stuck detection, güvenli yeni konum ve yumuşak dönüş kuralları olsun. Teleport varsa sahne bağlamında doğal göster.

## 4. Sinematik görev şablonu

Genel state: `idle → available → engaged → resolving → complete/return`. Ayrıca `pause`, `skip`, `interrupt`, `reload` geçişleri.

- **Yürüyüş ve şarkı:** yürüme ritmi, tempo, ses aç/kapa, mekan çevre tepkisi, isteğe bağlı katılım.
- **Balık tutma:** atış hedefi, bekleme, balığın işareti, müdahale, başarısızlıkta yumuşak geri bildirim.
- **Koltukta film izleme:** oturma animasyonu, kamera değişimi, pet etkileşimi, zaman akışı, çıkış.

Görevler birbirinden ayrı ritim taşımalı; hepsini “A tuşuna bas” şemasına indirme. Sinematik anlar skip edilebilmeli ve kontrol güvenli biçimde geri dönmeli.

## 5. Ruh sağlığı gibi hassas temalar

Depresyonu basit görevlerle **kesin yenilen** bir düşman veya oyunun klinik tedavi sunduğu iddiası olarak sunma. Negatif duygu ve oyuna ara vermeyi cezalandırma; pet kaybı/utandırma gibi manipülatif mekanikler kurma. Tempo, pause/skip, ses/flash yoğunluğu ayarı ve içerik uyarısı ver. Yerel destek kaynaklarını yayın öncesi doğrula. Oyun testi klinik kanıt değildir.

## 6. Dikey kesit tamamlanma koşulu

1. Kontrol edilebilir karakter, kamera ve bir oynanabilir çevre.
2. Pet takip, engelden kaçınma ve kadraja geri dönüş.
3. En az iki farklı etkileşim ritmi (hareket + bağlamsal etkinlik).
4. Pause, görev geri dönüşü, checkpoint ve reload.
5. Hedef cihaz/temsili ortamda oynanış smoke, pet görünürlük ve frame-time testi.

Bu kontroller yapılmadıysa görsel konsepti “oynanabilir oyun” diye sunma.

## V3 sinematik oyun yaratıcılığı

Bir görev yalnızca "balık tut" veya "yürü" komutu değildir. Görev, **dünya tepkisi ve oyuncunun bağ kurduğu anlamlı bir anda** biter. Örnek: Yürüyüş sırasında oyuncu konuşmadığında pet ritmini yavaşlatıp onunla sessizce kalır. Bu öneri klinik iyileşme iddiası değildir; ses/renk ile oyuncuya olumsuz duygu cezası vermez.

Sahne tasarımında üç ayrı eksende yenilik ara: (1) oyuncu ajansı, (2) mekânın duyguya yanıtı, (3) pet ile sözcüksüz iletişim. Aynı sahneyi sadece farklı hava durumuyla çoğaltma. [creative-reasoning.md](creative-reasoning.md) ve [motion-direction.md](motion-direction.md) kullan.
