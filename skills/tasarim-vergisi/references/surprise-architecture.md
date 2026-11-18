# Surprise Architecture — beklenti ile anlamın tasarımı

Amaç yalnızca “şaşırtıcı görünmek” değil, oyuncunun sezdiği kurallardan **anlamlı ve gönüllü** bir deneyim üretmek. Sürpriz tek başına keyif demek değildir. Bazen hoş, bazen karışık, bazen bunaltıcı olabilir. Kaynak için bkz. [human-perception.md](human-perception.md).

## 7 aşamalı sürpriz kartı

1. **Baseline beklenti:** Önceki kullanım ve görsel işaretler oyuncuya ne vadeder?
2. **Ön ipucu:** Değişim öncesi anlaşılabilir işaret (ışık, davranış, ses, ritim) nedir?
3. **Beklenmedik kural:** Sadece renk/patika/konfeti değil, davranış veya bilgi nasıl değişir?
4. **Anlam bağı:** Neden bu oyuncu eylemi ve bu sahneyle bağlantılı?
5. **Çözülme:** Ne olduğunu anlama ve kontrolü geri alma yolu nedir?
6. **Karşılık:** Oyuncuya bilgi, aidiyet, ifade alanı, dünyada iz veya ustalık sağlar mı?
7. **Tekrar ve sınır:** İkinci seferde doğal varyasyonu var mı? Skip, pause, azaltılmış hareket, sessiz mod?

Her aşama **tasarım niyeti**, **gözlenen sonuç**, **kanıt seviyesi E0-E4** olarak ayrı yazılmalı. Bir aşama için veri yoksa tahmin yap ama olgu iddiasında bulunma.

## Sürpriz mekanizması aileleri

- **Davranışsal:** Evcil hayvan yalnızca oyuncuyu izlemez, oyuncu durduğunda onunla birlikte durmayı öğrenmiş gibi bir davranış sergiler. Bu AI zihin okuma değil, tasarlanmış durum geçişidir.
- **Mekânsal:** Kamera açı değiştirmeden çevrede ışık/örtüşme yoluyla yeni bir yer belirir.
- **Zamansal:** Önce yapılan küçük seçim sonraki ziyarette görünür bir iz bırakır.
- **Anlamsal:** “Başarmak” sandığın sahnenin aslında yalnızca birlikte vakit geçirmeye izin verdiğini fark edersin.
- **Çapraz-duyusal:** Müzik/ritim deneyimi sessiz modda görsel/haptik karşılığıyla erişilebilir kalır.

## Özgünlük testi

Üç katman ayrımı:

1. **Süs:** Yaprak/parçacık/rozet çıkıyor fakat sistem aynı.
2. **Geri bildirim:** Balık tutunca su/karakter tepkisi tutarlı biçimde değişiyor.
3. **Anlamlı farklılık:** Oyuncu balığı bırakmayı seçerse pet ve su yaşamı sonraki sahnede bunu hatırlatan, oyun durumuna bağlı farklı davranış sergiliyor.

Üçüncü katman **daha iyi olacağının kanıtı değildir**; oyuncu balık yakalamak isteyebilir. Bu nedenle özerklik, ipucu ve açıklanabilir sonuç sağla; gerçek kullanıcı testi tasarla.

## Rahatsızlığı tasarım hatası olarak ele al

- Zorla kontrol kaybı, beklenmedik korku, flaş, sert kamera sarsıntısı, yüksek ses, strobing.
- Kaybetme korkusuyla pet'i tehdit etme, olumsuz duygu için ceza, suçluluk ve bağımlılık tasarımı.
- Duygusal iyileşmeyi garantileme veya ruh sağlığı durumunu oyunla teşhis etmeye çalışma.
- Oyuncunun durma/ara verme/atlama/geri dönme hakkını saklama.

Başarılı sürpriz, **beklenti + farklılık + neden + anlaşılırlık + kullanıcı kontrolü** ilişkisini kurar. Şaşırtıcılık puanını yapay biçimde maksimuma çekmeye çalışma.
