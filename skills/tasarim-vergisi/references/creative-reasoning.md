# Creative Reasoning Engine — çok fikir değil, farklı ve anlamlı fikir

**Temel ilke:** Yaratıcılık = yalnızca sıradışılık değil; **yenilik + kullanışlılık + bağlamla uyum**. Çıktı, herkesin yaptığı ekranın farklı renkli versiyonu olamaz. Kullanıcının açık referans sadakati kısıtını korurken farklılığın nerede değer katacağını belirle.

## A. Önce problemi yeniden tanımla

Tek satırlık görev, kullanıcının sözcüklerini tekrarlamamalı. Şunları yaz:
- İnsan hangi eylemi gerçekleştiriyor, hangi deneyimi yaşıyor, neye takılıyor?
- Açık istek / gizli varsayım / çelişen ihtiyaç / korunacak sert kısıt nedir?
- **Beklenen standart çözüm** nedir? Bunu baseline olarak yaz ve neden sıradan olduğunu açıkla.
- Sonuç ekran mı, hissedilen mikro an mı, davranış değişimi mi? Hangi kanıtla anlaşılacak?
- “İmkânsız gibi görünen” kısıt neden var? Kısıtı kaldırırsak hangi farklı çözüm açılır?

## B. Ayrışma: en az üç gerçekten farklı yön

Kapsam genişse en az **altı aileden** fikir üret; dar görevde hedefe uygun üç yön yeterli:
1. **Sadık yorum:** Referansın görsel DNA'sı korunurken oyuncunun deneyimi daha iyi olur.
2. **Mekanik tersine çevirme:** Beklenen etkileşim kuralı değişir; sadece görünüm değil.
3. **Farklı alandan aktarım:** Örneğin tiyatro sahneleme, müzik ritmi, stop-motion, bahçe tasarımı veya sinema kamera gramerinden oyuna işlevsel kural aktar.
4. **Kısıtı fırsata çevirme:** Az metin → çevre üzerinden hikâye, düşük GPU bütçesi → güçlü silüet/ışık kompozisyonu.
5. **Duygu üzerinden tasarım:** Kullanıcının hissetmesini istediğimiz duygudan kontrol, ritim ve geri bildirim mekanizmasına git.
6. **Radikal ama üretilebilir:** Standart ekrandan yapısal olarak farklı, 1–2 haftalık dikey kesitte kanıtlanabilir yön (zaman/ekip bilinmiyorsa süre vaat etme).

Her yön **kompozisyon**, **etkileşim**, **sahne/hikâye ritmi** ve **geri bildirim** açısından en az bir yapısal fark içersin. Sadece palet, font, köşe yarıçapı değiştiyse yeni yön sayma. Kaynağı birebir kopyalamak yasak.

### Fikir laboratuvarı

Her yön için 10 satırlık kart:
- Adı ve tek cümlelik yenilik mekanizması
- Kullanıcı eylemi, beklenen duygu
- Referans DNA'sından neler korunuyor?
- Standart çözümden **somut olarak hangi kural değişiyor**?
- Görsel kompozisyon / mekân / kamera
- Etkileşim / kontrol / motion
- Ses, ilerleme veya pet/NPC tepkisi (ilgiliyse)
- Teknik maliyet, risk ve prototipte nasıl yanlışlanacağı
- Benzerlik/lisans sınırı
- **Neden iyi çalışmayabilir?** (güçlü eleştiri)

## C. Çaprazlama ve karşı-olgusal düşünme

- İki uzak kategori arasında **nedensel** bir birleşim ara. Örneğin müzikteki ritim → oyuncunun yürüme temposu → pet'in davranışında değişim. Sadece görsel kolaj yapma.
- Fikirleri tek tek değil **ne kaldırırsak / neyi ters çevirirsek / kontrolü kimden alıp kime verirsek / zaman aksını değiştirirsek** sorularıyla dönüştür.
- Baseline ve en iyi iki aday için “bu özellik olmazsa ne kaybederiz?” karşı testi yap. Bir şey kaybolmuyorsa fikir dekorasyon olabilir.
- Kullanıcı referansa sıkı sadakat istiyorsa bozucu yeniliği güvenli alternatif olarak ayrıştır; sessizce esas tasarımı değiştirme.

## D. Yakınsama: özgünlük, tutarlılık, yararlılık

Adayları 1–5 puanla: **özgünlük (aynı kategorideki kalıplardan uzaklık)**, **insan yararı**, **anlatı/ürün uyumu**, **yapılabilirlik**, **duygusal etki**. Her puan için kanıt/gerekçe ve belirsizlik ver. Puanlar gerçek kullanıcı tepkisinin yerini tutmaz.

**Engelleyici koşullar:** Kullanıcı hedefini yok ediyor, erişilebilirlikte kritik kusur, gereksiz moral baskı, lisans/telif ihlali, test edilemeyecek pahalı fikir, yalnızca görsel rötuşla “radikal” ilan etme.

Ayrışma tamamlanmadan yüksek skorlu bir fikre erken kilitlenme. En iyi adayın **karşıt görüşünü** yaz; etkili ama aşırı riskli yönü ikinci alternatif olarak tut.

## E. Yaratıcılık testi: reddet / değiştir / kanıtla

Her seçilen aday için üç test:
1. **Benzersizlik:** Referans veya bilinen baseline ile tasarım *mekaniği* aynı mı? Aynıysa aday yeniden üretilecek. Kasıtlı referans sadakati “özgün değil” kusuru sayılmaz; ayrışan kısmı açık belirt.
2. **Anlaşılırlık:** İlk bakışta asıl eylem anlaşılabiliyor mu? Hayırsa eyleme dair işaretleri iyileştir; sıradışılığı körü körüne savunma.
3. **Dikey kesit:** Bir kullanıcı gerçekten yapabildi mi, beklenen duygu/etkileşimi deneyimledi mi? İnsan testi yapılmadıysa “insan onayladı” deme.

İsteğe bağlı **scripts/idea_audit.py**, fikirlerin yapısal açıklamalarının kopya olup olmadığını ve açık değer gerekçelerini statik kontrol eder. Bu araç görsel özgünlüğü veya gerçek yeniliği **ölçmez**; insan değerlendirmesi ve çalışan prototip hâlâ gerekir.

## Kaynak temeli

- [Design Council: Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation): önce keşfet/ayrıştır, sonra yakınsa ve test et.
- [Nielsen Norman Group: Principles of Visual Design](https://www.nngroup.com/articles/principles-visual-design/): ölçek, görsel hiyerarşi, denge, kontrast ve Gestalt.
- [Cambridge: Assessment of Creative Potential via Novelty and Usefulness](https://www.cambridge.org/core/journals/design-science/article/assessment-of-the-creative-potential-of-design-problems-via-novelty-and-usefulness/ECBD7B65EA50FEBB0831C6D4A20AC585): yenilik ve kullanışlılığın ayrı değerlendirilmesi.
