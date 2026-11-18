# Design DNA: tek kaynaklı görsel ve davranış sözleşmesi

İlgili projenin kökünde `DESIGN-DNA.md` oluştur. Bu dosya moodboard değil; **ölçülebilir**, sürümlenen ve bütün ajanlarca kullanılan bir teknik tasarım sözleşmesidir. Mevcut token'lar ve onaylı referanslar varsayılan olarak korunur.

## DESIGN-DNA.md şablonu

```markdown
# DESIGN-DNA
Version / tarih:
Proje, kullanıcı ve çekirdek eylem:
REF-ID'ler ve doğrudan incelenen materyal:
Değişmemesi gereken öğeler:
Kasıtlı sapmalar / gerekçe:

## Görsel kimlik
Renk, semantik renk, kontrast, dark mode:
Font ailesi/fallback, metrik, ölçek, satır yüksekliği, tracking:
Spacing/grid/radius, responsive ve safe-area:
Icon/asset stil, kaynak/lisans, export, merkezleme:
Işık, gölge, materyal ve detay seviyesi:

## Motion ve kamera
Motion token (süre, easing/spring, stagger, interrupt, reduced-motion):
Kamera (perspektif/ortografik, pitch/yaw, FOV, zoom, clipping):
Karakter ve pet ekran yüksekliği %, görünürlük kuralı:
Parallax ve katman/occlusion:

## Etkileşim ve durumlar
Kontroller, navigasyon, focus/selection, geri dönüş:
Loading, empty, error, success, disabled, offline:
Ses, titreşim, altyazı, duyusal ayarlar:
İçerik taşması, büyük yazı, yerelleştirme:

## Sahiplik ve doğrulama
Ana token/asset manifest dosyası:
Ajanların değiştirebileceği sınırlar:
Ölçüm hedefi / screenshot/video kanıtı:
```

## Değişiklik denetimi

- Her kritik karar bir `REF-ID` veya açık `ürün hedefi` gerekçesine bağlanır.
- Kaynak ölçümü yoksa değeri varsayım olarak işaretle; ölçülmüş sanılmasın.
- Ajanların her biri bağımsız font/palet/kamera/animasyon seçemez; Design DNA sürümünü kullanır.
- Onaylı yön değişecekse önce etkilenen ekran/sahne ve yeni kararın sebebini yaz.
- Rastgele fade-in yerine hareketin işlevi, ritmi, sürekliliği, kesilmesi ve reduced-motion karşılığı tanımlanır.

V3: İlk bakış görsel hiyerarşisini, standart çözümden **mekanik ayrışma** kararını ve muhalif görüşten kaynaklanan düzeltmeyi Design DNA değişiklik geçmişine ekle. Motion shot card bağlantısını sakla.
