# Motion Direction — hareket sahnenin bir parçası olsun

Her animasyon için amaç tanımla: yönlendirme, dokunsal geri bildirim, süreklilik, sahne anlatısı, yaşam hissi veya mekânsal ilişki. Süs olsun diye aynı fade-in'i her ekrana koyma.

## Motion shot card

```text
Shot ID / kaynak REF-ID:
Tetikleyici ve başlangıç durumu:
Kamera/odak ve korunan silüet:
Hareket eden objeler, path, acceleration ve easing:
Süre/ms veya frame, bilinen / önerilen ayrımı:
Stagger/overlap, audio/haptic ilişkisi:
Eylem sırasında kullanıcı kontrolü açık mı?:
Kesilme, atlama, pause, reverse, reduced motion:
Render maliyeti, occlusion, jitter, overflow riskleri:
Aynı viewport'ta önce/ara/sonrası karşılaştırma kanıtı:
```

## Denetim

- UI'da varsayılan olarak yalnızca uygun animasyon özellikleri kullan; layout thrash ve gereksiz GPU yükü ölç.
- Oyunlarda "transform/opacity her zaman yeterli" yanlış olabilir: skeleton, shader, physics ve kamera işlemlerini uygun profiler ile kontrol et.
- Pet/NPC ve kamera arasında devamlılık korunmalı; her sahne geçişinde kaybolma, aşırı küçülme ve örtülme testleri uygulanmalı.
- 60 FPS bir hedefse 16,7 ms teorik kare bütçesi vardır ama ölçüm yoksa başarı iddiası kurulmaz.
- Hareket hassasiyeti/erişilebilirlik için azaltılmış, alternatif veya atlanabilir sürüm bulunmalı.
