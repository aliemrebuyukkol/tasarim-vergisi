# Görev brifi v2

Her paket tek bir kullanıcıya görünür sonucu hedefler. Genel web kurallarını Swift/oyun işlerine **kopyalama**: domain-profiles.md ile platforma uygun kalite kapılarını seç.

```markdown
# T-001: Görev
Durum: planlandı | çalışıyor | incelemede | geçti | başarısız | engellendi
Kapsam: araştırma | prototip | uygulama
Öncelik: P0 | P1 | P2 | P3
Bağımlılıklar: T-...
Ajan/model/efor: mevcut model ve seçilme gerekçesi

## Girdi ve tasarım kilidi
Ürün, hedef eylem ve mevcut korunacak davranış:
Referanslar / bulgu kartları: REF-... / F-...
DESIGN-DNA.md sürümü ve değiştirilemez token/kamera/motion:
Domain profili / hedef cihaz:

## Üretilecek sonuç
Kullanıcıya görünür tek özellik/sahne:
State geçişleri, input/çıkış, geri/iptal:
Loading/empty/error, overflow, locale, offline:
Varlık/asset lisansı ve bağımlılıklar:
Erişilebilirlik, reduced motion, ses/altyazı:

## Dosya ve entegrasyon
Dokunabileceği dosyalar:
Dokunamayacağı dosyalar:
Worktree / entegrasyon sırası / rollback:
Dış eylem yetkisi:

## Ölçülebilir kabul
- [ ] Kaynak ve hedef aynı viewport ve UI state ile karşılaştırıldı
- [ ] Ana eylem + geri dönme + hata akışı çalışıyor
- [ ] İlgili loading/empty/error ve farklı ekranlar kontrol edildi
- [ ] Platforma uygun erişilebilirlik test edildi
- [ ] Var olan build/lint/test komutları çalıştırıldı
- [ ] Oyun ise kamera, pet, collision ve kayıt senaryoları test edildi
- [ ] Gerekliyse frame-time/bellek/asset bütçesi ölçüldü
- [ ] P0/P1 yok, P2 riskleri kaydedildi

## Doğrulama
Gerçek komut, araç, cihaz ve sürüm:
Ekran/video/log kanıtının yolu:
Durum: geçti | başarısız | engellendi | uygulanamaz
Yapılmayanlar ve neden:
```

Belirli bir test aracı mevcut değilse komut uydurma, `engellendi` raporla. Kodun derlenmesi görsel sadakat veya oynanabilirlik doğrulaması değildir.

## V3 yaratıcı ayrışma eki

- Baseline ve önerinin **yapısal farkı** (sadece renk değil):
- İlk 3 saniye algı hipotezi ve test yöntemi:
- Yaratıcılık eleştiri konseyinin en güçlü karşı argümanı:
- Motion shot card ve ses/oyuncu kontrol sürekliliği (uygunsa):
- Gerçek kullanıcı testi yoksa bu engel açıkça yazılmalı.
