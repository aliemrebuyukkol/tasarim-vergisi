---
name: tasarim-vergisi
description: "Tasarım Vergisi" — küratörlü bir referans kataloğunu (UI galerileri, motion, tasarım sistemleri, pixel-art/oyun, 3D, video, AI ses/medya, kalite kapıları) kullanarak istenen uygulama için en iyi, en kaliteli ve en farklı özellik, tasarım ve içerikleri toplar; örnekler, gerekirse sorular ve örnek tasarımlarla sunar; sonra bunları ajanlara görev brifleri olarak dağıtır. Kullanıcı "tasarım vergisi", "referanslardan özellik topla", "bu uygulama için ilham/özellik çıkar ve ajanlara dağıt" dediğinde ya da bir uygulama fikri verip referans tabanlı tasarım araştırması istediğinde kullan.
license: MIT
---

# Tasarım Vergisi

Her uygulama, referans kataloğundan bir "vergi" öder: her ilgili kategoriden, o uygulamaya
gerçekten katkı sağlayacak en iyi fikirler toplanır, puanlanır, görselleştirilir ve iş
paketlerine bölünüp ajanlara dağıtılır.

Dosyalar (bu SKILL.md'ye göre göreli):
- `references/catalog.md` — kategorize referanslar + uygulama türü → kategori matrisi
- `references/finding-card.md` — araştırma bulgu kartı formatı
- `references/task-brief.md` — ajan görev brifi şablonu

Bu skill araçtan bağımsızdır (Claude Code, Codex, Gemini CLI, Cursor, Antigravity…).
Aşağıda "varsa" denen her araç yoksa, belirtilen yedek yolu kullan.

## Akış

### 1. Kabul — en fazla 4 soru
Uygulama tanımı eksikse kullanıcıya sor (yapılandırılmış soru aracın varsa onu, yoksa
tek mesajda numaralı sorular). Bilinenleri tekrar sorma:
- **Tür**: SaaS/web paneli · mobil · oyun · içerik/video üretimi · açılış sayfası · diğer
- **Platform & yığın**: web (React/Next?), iOS, Android, masaüstü, Unity…
- **His/stil**: 2–3 sıfat (minimal, oyunsu/pixel, sinematik/3D, editoryal…)
- **Kapsam**: sadece fikir raporu mu, ajanlarla uygulama da mı?

Proje klasörü varsa önce oku (README, package.json, mevcut UI); sorular buna göre daralır.

### 2. Yönlendirme
`catalog.md` içindeki matrise göre kategorileri seç. "Farklılık" için en az bir
**beklenmedik** kategoriden fikir taşı (ör. SaaS paneline pixel mikro-animasyon, oyuna SaaS
tarzı onboarding). Seçimi tek satırla bildir, onay bekleme.

### 3. Hasat — paralel araştırma
Her seçili kategori için bir **salt-okuma araştırmacı** çalıştır:
- Alt ajan/görev aracın varsa (Claude Code `Agent`, Codex/Gemini alt görevleri, harici ajan
  CLI'ları) kategori başına bir tane, paralel.
- Yoksa kategorileri sırayla kendin araştır.
- Kaynakları **gerçekten aç**: web fetch veya tarayıcı aracı; GitHub repolarında README,
  örnekler, demo sayfaları. Açılamayanı kartta "doğrulandı: hayır" diye işaretle, uydurma.
- Giriş gerektiren siteler (ör. mobbin): kullanıcının oturumu açık tarayıcı varsa oku;
  **şifre girme** — kullanıcıdan giriş yapmasını iste ya da atla.

Brife yazılacak kurallar:
- **Kalıp al, varlık kopyalama**: görsel, logo, sprite, metin kopyalanmaz; desen ve teknik
  tarif edilip özgün olarak yeniden üretilir.
- Oyun referansları yalnızca mekanik/his ilhamıdır; belirli bir oyunun adı, karakteri,
  sanatı veya seviyeleri yeniden yaratılmaz.
- Lisansı not et; GPL/AGPL bağımlılıklarını uyarıyla işaretle.
- Çıktı: `finding-card.md` formatında, kategori başına 5–10 kart.

### 4. Küratörlük — puanla, ele, sor
Kartları birleştir, tekrarları ele. Her karta 1–5: **Katkı**, **Kalite**, **Farklılık**,
**Maliyet** (düşük iş = yüksek puan).
Skor = Katkı×2 + Kalite + Farklılık×1.5 + Maliyet. En iyi 10–20 kartı seç; her ilgili
kategoriden en az biri ve en az 2 "cesur" (Farklılık 5) kart kalsın.
Belirsiz yön kararları için **bir tur** soru sor, önerini ilk seçenek yap.

### 5. Örnek tasarımlar
En güçlü 3–5 fikir için çalışan örnek üret — tek dosyalık HTML demo varsayılan:
- UI/etkileşim → HTML/CSS (+ Motion/anime.js); satır içi görsel/artifact aracın varsa onunla göster.
- Hareketli tanıtım → Remotion veya HTML zaman çizelgesi.
- 3D → Three.js tek sayfa; Blender MCP bağlıysa sahne taslağı.
- Pixel art → Canvas tek sayfa (ör. rüzgârlı ağaç, dither/CRT efekti).
Örnekleri `tasarim-vergisi/ornekler/` altına kaydet; her birine kaynak ve "neden bu
uygulamaya" satırı ekle.

### 6. Rapor
Proje köküne `TASARIM-VERGISI.md`:
1. Uygulama özeti ve seçilen yön
2. Kategori tablosu (kaynak → fikir sayısı)
3. Seçilen kartlar (puan sırasıyla) + örnek bağlantıları
4. Elenen ama "sonra" fikirler
5. İş paketleri ve bağımlılıklar
6. Açık sorular

### 7. Dağıtım — ajanlara görev
Kapsam "uygulama da" ise seçilen kartları `task-brief.md` ile iş paketlerine çevir:
paket = kullanıcıya görünür tek sonuç, dosya kapsamı ve doğrulama komutu belli.

| İş | Önerilen ajan |
|---|---|
| Tasarım sistemi/token, kritik mimari karar | Ana ajan (sen) |
| Standart UI bileşeni, animasyon, test, doküman | Hızlı/ucuz kodlama ajanı (ör. Gemini, Codex medium, Claude alt ajan) |
| 3D/shader/fizik, zor algoritma | En güçlü kodlama ajanı, yüksek efor |
| Video/tanıtım klibi | Remotion veya video skill'i |
| Ek araştırma/doğrulama | Salt-okuma alt ajan |

Kurallar: aynı çalışma ağacında aynı anda tek yazar (paralel yazarlar için `git worktree`);
ajanlar commit atmaz; her paketin doğrulama komutunu kendin çalıştır; bağımsız bir
inceleyici (mümkünse farklı model ailesi) brife karşı gözden geçirsin.
Alt ajan aracın yoksa paketleri sırayla kendin uygula.

### 8. Kapanış
Tablo: paket · ajan/model · durum · dosyalar. Doğrulanamayan kaynakları ve açık soruları listele.

## Katalog bakımı
Kullanıcı yeni referans verirse `references/catalog.md`'de uygun kategoriye ekle
(ad, URL, ne verir, uygun türler). `(?)` işaretli satırları ilk doğrulamada düzelt.
