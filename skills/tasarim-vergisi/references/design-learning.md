# Design Learning Ledger — geçmiş tercihlerden öğren, varsayma

Bu modül modelin içsel bilincini değiştirmez. Proje klasöründeki **denetlenebilir karar ve test kaydı** ile sonraki çalışmanın aynı hataları tekrar etmesini engeller. Önceki kullanıcı sohbetlerine veya bağlanmamış dosyalara erişimi olduğunu varsayma.

Proje kökünde `DESIGN-LEARNING.md` dosyası tut. Yalnızca kullanıcının erişilebilir, projeyle ilgili ve izin verdiği kaynaklardan yararlan. Kişisel sağlık verisi, özel sohbet veya gereksiz kimlik bilgisi kaydetme.

## Kayıt

```text
Tarih / commit / uygulama:
Karar ID ve hipotez:
Kullanıcı için değer ve sert tasarım kısıtı:
İncelenen REF-ID, kanıt yolu:
Seçilen yön / reddedilenler / gerekçe:
Uygulanan tasarım-token / teknik:
Görsel QA ve oynanış testi sonucu (olmadıysa engellendi):
Hangi yanlış varsayım keşfedildi?:
Tekrarlanacak desen / kaçınılacak antipattern:
Bir sonraki denemede ne değişmeli?:
```

## İyileştirme döngüsü

1. Yeni işte bu kayıt varsa ilgili başarısızlıkları ve kullanıcı tercihlerini oku; geçmiş kararı **değişmez hakikat** kabul etme.
2. En az bir alternatif hipotez kur. Yeni referans veya kullanıcı hedefi, eski yöntemi geçersiz kılabilir.
3. Yeni ekran/oyun görevinde aynı hataya rastlarsan nedeni ve kabul kriterini güncelle.
4. Kullanıcı geri bildirimi ile modelin kendi beğenisini farklı kaynak olarak etiketle.
5. Gerçek kullanıcı testi yapılmadıkça "beğenildi", "viral olur", "depresyonu azaltır" gibi sonuçlar yazma.

**Gizlilik:** Kayıt proje düzeyindeki teknik/tasarım kararları içindir. Kullanıcı talep etmedikçe kişisel tercihi evrensel kural gibi başka projeye taşıma.
