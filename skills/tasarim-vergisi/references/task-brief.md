# Ajan görev brifi şablonu

```
# Görev: <paket adı>
Ajan: <claude-subagent | codex (effort) | agy (model)>

## Bağlam
Uygulama: <1 paragraf>. Seçilen yön: <stil sıfatları, tasarım token'ları dosyası>.
Kaynak kart(lar): <kart adları + URL'ler>.

## Yapılacak
<kullanıcıya görünür tek sonuç; adımlar>

## Dosya kapsamı
Dokunabilir: <yollar>. Dokunamaz: diğer her şey. Commit yok.

## Kabul kriterleri (kalite kapıları)
- Erişilebilirlik: klavye, odak, `prefers-reduced-motion` (lawsofux / Radix ilkeleri)
- CSS: defensive layout, taşma/uzun metin (ishadeed)
- Kod: TS strict, patterns.dev uygun desen
- Test: testing-library birim + gerekirse Playwright senaryosu; Storybook hikâyesi (varsa)
- Güvenlik: kullanıcı girdisi/HTML için OWASP XSS kuralları
- Performans: animasyonlar transform/opacity, 60fps

## Uç durumlar
<boş veri, çok uzun metin, yavaş ağ, küçük ekran, hareket kapalı, karanlık mod …>

## Doğrulama komutu
<npm test / npx playwright test …>
```
