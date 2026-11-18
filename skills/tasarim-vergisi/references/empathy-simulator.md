# Empathy Simulator — seyircinin zihnine dair denetlenebilir anlatılar

Bu modül yapay zekânın bir insan **olduğunu** iddia etmez. Gözlenen sahneden yola çıkarak değişik amaç, duygu durumu, deneyim ve erişilebilirlik koşulları için **olası insan yorumlarını** hikâyeleştirir ve test edilebilir hipotezlere çevirir.

## Kullanıcı bağlamını sahneye getir

Demografik klişelerle (kadın/erkek/yaş/ülke → şu rengi sever) çıkarım yapma. Kişinin o **andaki** niyeti daha anlamlı olabilir:

- Hızlı ilerlemek istiyor: ilk eylem net mi, gereksiz bekleme var mı?
- Keşfetmek istiyor: açıklamasız ama anlaşılır küçük ipuçları var mı?
- Sakinlik arıyor: ilerleme zorunlu mu, yavaşlama mümkün mü?
- Ses kullanamıyor: tüm ana bilgi görsel/haptik alternatifle sağlanıyor mu?
- Hareket hassasiyeti var: kamera ve parallax kapatılabilir mi?
- Oyuncu duygusal açıdan hassas olabilir: tema baskısız, tetikleyici içerik atlanabilir mi?

Bu durumlar **ihtimaldir**, gerçek kullanıcı profili veya tıbbi çıkarım değildir.

## Dört farklı anlatı

Aynı sahneyi dört kısa, ilk kişi **varsayımsal kullanım anlatısı** olarak yaz:

1. **İlk kez karşılaşan:** Nereye bakıyorum? Ne yapacağımı anlıyor muyum?
2. **Meraklı/gezen:** Ne keşfetmek istiyorum? Ufak ipuçlarını yakalıyor muyum?
3. **Yorgun/hızlı sonuç isteyen:** Ne zaman sıkılıyorum? Denetim bende mi?
4. **Erişilebilirlik kısıtıyla kullanan:** Ses, hareket, görsel karmaşıklık veya küçük dokunma hedefleri deneyimi bozuyor mu?

Her anlatıda üç sütun tutulur:

| Gözlemlenen/ölçülen | Olası iç yorum (E0 hipotez) | Kullanıcıyla sınanacak |
|---|---|---|
| Pet karakterden 2 m uzaklaşıyor | “Beni bırakacak mı?” diye düşünebilirim | Pet'i çağırma ihtiyacı, kaygı, doğal yorum |
| Yol feneri 3 saniye titreşiyor | “Orada bir şey mi var?” diye merak edebilirim | Hedefin bulunma oranı ve aşırı dikkat dağıtma |
| Film sahnesi kontrolü kilitliyor | “Oynama hakkımı kaybettim” diyebilirim | Skip/pause denemesi ve terk nedeni |

**Uydurulmuş alıntı yazma.** Örnek iç ses açıkça “olası deneyim anlatısı” diye etiketlenir. İnsan hissettiğini söylemeden onun olası tepkilerini modellemek mümkündür.

## “Bunu neden sevebilir?” testleri

- **Anlam:** Görsel ayrıntı sadece süs mü, anlatının bir parçası mı?
- **Özerklik:** Kullanıcı tempo veya sonucu etkileyebiliyor mu?
- **Yakınlık:** Karakter/pet tepkisi oyuncunun yaptıklarıyla ilişkili mi, rastgele mi?
- **Keşif:** Bir işareti fark edip kendi kendine sonuç çıkarabiliyor mu?
- **Ödülün niteliği:** Sadece puan/rozet mi, yoksa dünyada kalıcı iz, öykü bilgisi, rahatlama veya ustalık mı?
- **Tekrar:** Sürprizin yüzüncü seferde işlevi var mı? Kopyala-yapıştır olaylardan kaçın.

## Hipotez kartı

```
Persona yerine bağlam/niyet:
Sahne / REF / kanıt seviyesi:
Gözlenen: 
Olası ilk düşünce / şaşkınlık:
Olası keyif ve olası itiraz:
Alternatif yorum (karşı hipotez):
Uygulanacak tasarım değişikliği:
Gerçek kullanıcıya sorulacak soru / gözlenecek davranış:
Karar (yalnızca varsayım / veri var):
```

## Oyuncu sağlığı ve duygu

Depresyon gibi hassas temalarda evcil hayvan bir cezalandırıcı, kaybedilme tehdidi veya tedavi cihazı değildir. Oyuncu konuşmama, yürümeme, ara verme, sahneyi atlama gibi tercihlerde bulunabilir. Oyuncunun hangi psikolojik durumdan geçtiğini metin, yüz, tempo veya seçimden kesin olarak çıkarma. Klinik iddia için klinik kanıt gerekir.
