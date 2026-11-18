# Critique Council — fikri pohpohlama, çürütmeye çalış

Yaratıcı bir yapay zekâ kendi fikrini beğenmeye meyilli olabilir. Bunun önüne geçmek için **bağımsız eleştiri, görünür anlaşmazlık ve alternatif hipotez** uygula.

## Konsey rolleri

1. **Art director:** Hiyerarşi, kamera, boşluk, ışık, özgün karakter ve görünüm tutarlılığı.
2. **Game/interaction designer:** Ana eylem, ritim, kontrol, oyuncu motivasyonu ve tekrar değeri.
3. **Skeptical user:** İlk bakıştaki kafa karışıklığı, fazla hareket, gereksiz adım ve erişilebilirlik.
4. **Technical adversary:** Gerçek platform, cihaz, performans, asset maliyeti, test ve sınır durumları.
5. **Cultural/ethical reviewer:** Ruh sağlığı gibi hassas anlatılarda zarar, telif, manipülatif tasarım, mahremiyet.

Birden çok model erişilebiliyorsa fikirleri görmeden önce **ayrı** yanıt iste. Yoksa aynı modelin rolleri bağımsız görüş gibi sunulamaz: "tek modelin perspektif simülasyonu" diye yaz. Fikir üreten ajan, tek başına QA onayı vermez.

## Kör değerlendirme

- Fikirleri "en iddialı" veya "benim favorim" etiketi vermeden, A/B/C olarak ve benzer sunum kalitesinde göster.
- Önce sessiz puan: yenilik, kullanılabilirlik, duygusal rezonans, teknik risk, erişilebilirlik.
- Her değerlendirici: bir güçlü taraf, iki kritik sorun, bir **alternatif** ve nasıl test edileceği.
- Dissent kaydı: hangi iki görüş çatıştı ve hangi kanıtla karar verildi?
- Karar mekanizması: yüksek ortalama + kritik güvenlik/işlev itirazı varsa otomatik onay **yok**. Gerekçeli karar veya test gerekir.

## Red-team soruları

- “Bu tasarımı yüzlerce benzerinden ayıran değişiklik mekanikte mi, yalnızca renkte mi?”
- “Kullanıcı hedefi tasarım estetiğine kurban mı edildi?”
- “Bu özellik küçük ekranda, ses kapalıyken, pet görünmezken veya hareket azaltıldığında hâlâ çalışır mı?”
- “Bu his gerçekten gözlemlendi mi, yoksa tasarımcı projeksiyonu mu?”
- “Bir filmde güzel duran sahne, oyuncu kontrolü altında sıkıcı veya yanıltıcı olabilir mi?”
- “Aynı duyguyu daha az varlık ve daha basit kodla kurabilir miyiz?”

## Çıktı sözleşmesi

```text
Aday ID:
Görüş sağlayıcı: gerçek ayrı model / tek model perspektif simülasyonu / kullanıcı testi
Lehte kanıtlar:
Kritik karşı görüş:
Özgünlük farkı (baseline ile):
Kullanıcı yararı:
Teknik/etik risk:
Test önerisi:
Karar ve karara katılmayan görüş:
```
