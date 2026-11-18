# v5 Taste Lab — gerçek insanla değerlendirmenin uygulanabilir protokolü

## Tek soru değil beş ayrı soru

İnsanların neye şaşırdığı ve neyi sevdiği aynı değil. Deneyde tek bir `WOW` veya `farklılık` puanı üretme:

1. **Fark etti mi?** Görev sırasında sözlü yönlendirme olmadan davranışı algıladı mı?
2. **Anladı mı?** “Kedi neden geri dönüyor?” sorusuna kendi yorumunu verebiliyor mu?
3. **İşe yaradı mı?** Görevi tamamlıyor mu, ne kadar sürüyor, takılıyor mu?
4. **Sevdi mi?** Öznel değerlendirme 1–5, neyi sevmediği ve neden (serbest yanıt).
5. **Hatırladı mı?** Ayrı rızayla 24 saat sonra sahneyi/spesifik davranışı hatırlıyor mu? Yoksa **boş**.

## Katılımcıya uygulanacak prosedür

- Test amacını tarafsız açıkla; sağlık durumu veya kişisel geçmiş sorma. Testi bırakmak serbest; kayıt için açık rıza al. Katılımcı adı yerine yerel takma ID kullan.
- İki alternatif karşılaştırılacaksa katılımcıların varyant dağılımını karıştır veya sırayı dengele; demografik/teknolojik deneyim farklarını asla yok varsayma.
- İlk görev: “Bu sahnede birkaç dakika geçir, kendince istediğin etkileşimi dene.” Kediye özel ipucu verme.
- Gözlemci olayları not eder; `noticed` yalnızca önceden tanımlanmış davranış sinyaliyle işaretlenir. “Güzel olmuş” gibi övgüyü `noticed=true` anlamına zorlamaz.
- Görevden sonra **önce açık uçlu** “Ne fark ettin?” “Nasıl hissettirdi?” “Neyi değiştirmek isterdin?”; sonra 1–5 şaşırma ve beğeni ölçeklerini sor.
- Erişilebilirlikte hareket hassasiyeti, ses kapalı ve alternatif kontrol yollarını denemek isteyen katılımcılara seçenek sun; rahatsızlık varsa testi bitir.
- Sonraki gün hatırlama kontrolü ayrıca izin/iletişim gerektirir; yapılmadıysa hücre boş.

## CSV ve saklama

`examples/human-study-template.csv` başlıklarını kullan. Her satır sadece gönüllü bir kişinin tek varyant gözlemidir. `consent=no` olan kayıtlar analizden çıkarılır. Katılımcı adları, e-posta, ses kaydı, sağlık geçmişi ve serbest yorumlar genel GitHub deposuna yüklenmez.

`python3 scripts/evidence_lab.py study --csv <local-private.csv> --output <local-report.json>`

Bu komut sayıları **betimler**, bağımsız neden/etki kanıtı veya ruh sağlığına dair klinik iddia oluşturmaz. 8 kişiden küçük gruplar **pilot_only** olarak işaretlenir; daha büyük gruplar da yalnızca betimleyicidir. Görüşmelerin nitel analizi, örnekleme, yanlılık ve alternatif açıklamalar ayrıca incelenir.

## Beğeni ile şaşkınlık arasındaki dört sonuç

- Yüksek sürpriz, yüksek beğeni: sahne anlamlı olabilir; tekrar kullanım, kontrol ve erişilebilirlik kontrolü sürer.
- Yüksek sürpriz, düşük beğeni: ani sahne, kesilen kontrol veya rahatsız edici efekt olabilir.
- Düşük sürpriz, yüksek beğeni: güven veren akıcılık ve tutarlılık başarıdır, zorla gösteriş ekleme.
- Düşük sürpriz, düşük beğeni: karşı hipotezi ve ana eylem değerini yeniden değerlendir.

Hiçbiri kesin nedensel yorum değildir. Şaşırtmayı maksimize etmek, kullanıcıya yararı maksimize etmek değildir.
