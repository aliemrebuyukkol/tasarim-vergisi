# Taste Lab — modelin fikrini değil, insan tepkisini ölç

Özgün, yaratıcı, şaşırtıcı veya duygusal tasarım **insanlar tarafından denenmeden** doğrulanmış sayılmaz. Modelin puanları yalnızca eleme için kullanılır; sahte nörolojik etki yüzdeleri ve hayalî kullanıcı verileri yazılmaz.

## 1. Soru ve hipotez

Her aday için kullanıcı tarafından değerlendirilebilir iki soru kur:

- **Davranışsal:** İlk etkileşim çağrısını yardım almadan keşfedebildi mi? Pet'in kamera dışında kaybolması yaşandı mı? Skip seçeneğini gördü mü?
- **Duygusal/estetik:** “Bu sahnede ne hissettin?” “Seni şaşırtan neydi?” “Hangi anı hatırlarsın?” “Bir şey canını sıktı mı?” (Yönlendirici “çok güzeldi değil mi?” sorusu yok.)

Değişkenleri karıştırma: Aynı anda renk, mekân, hareket, müzik, mekanik değişirse **hangisinin** etki ettiğini ölçmek zorlaşır. Çok değişkenli keşif yapılabilir ama nedensel sonuç çıkarma.

## 2. Test modları

- **5 saniyelik ilk izlenim:** Ekranı kısa göster, kapat, ne gördüğünü ve ana eylemi sor. Gerçek ölçüm yoksa “5 saniyede fark eder” deme.
- **Kör A/B veya A/B/C eşleştirmesi:** Aynı kalite ve benzer içerik; sıra dengelemesi; yalnızca en yüksek beğeni değil, **neden** sorusu.
- **Ses/ekran kaydıyla görev:** Başlama, deneme, hata, yardım, bırakma, geri dönme; katılımcı rızası ve gizlilikle.
- **Bağlam varyasyonu:** İlk kez kullanıcı, tekrar oynayan, hızlı iş, sakin keşif, ses kapalı ve hareket azaltılmış modu.
- **Açık hatırlama:** 24 saat sonra isteğe bağlı “aklına kalan an?” ölçümü. Yoksa uzun süreli hafıza etkisi iddiası yok.
- **Küçük örneklem:** Az sayıda kullanıcı, nitel sorunları ortaya çıkarabilir; evrensel beğeni, yüzdelik iyileşme veya genelleme kanıtı değildir.

## 3. Kullanıcının söylediklerini ayrı tut

Şu kavramları birbirine karıştırma:

- **Fark etti:** Gösterdi, buldu veya kendisi söyledi.
- **Anladı:** Yardımsız yapabildi veya açıklayabildi.
- **Şaşırdı:** Kendi anlatımında beklenmedik unsur tarif etti.
- **Sevdi:** Tercihi veya açık geri bildirimi var.
- **Hatırladı:** Daha sonraki ölçümde çağırabildi.

Bu beşini yalnızca modelin görsel puanından çıkarmak yasak. İnsan katılımcının yorumu ve davranışı farklı olabilir, ikisini de kaydet.

## 4. Karar kapısı

Bir fikri seçerken şu tablonun her satırına gerekçe ver:

| İddia | Veri | Alternatif açıklama | Sonraki test |
|---|---|---|---|
| Daha anlaşılır | İlk görev başarısı, hata sayısı | Tasarım zaten tanıdık olabilir | yeni katılımcıyla doğrula |
| Daha şaşırtıcı | Kendiliğinden anlatılan sürpriz | Bazı kullanıcılar rahatsız olabilir | itiraz ve kontrol hakkını test et |
| Daha güzel | Tercih + gerekçeli estetik yorum | Yenilik etkisi zamanla kaybolabilir | tekrarlı kullanım |
| Daha akılda kalıcı | Gecikmeli hatırlama | Dikkat çekti ama kullanım zor olabilir | davranış + hatırlama birlikte |

Karar durumu: **hipotez**, **prototipte işledi**, **insanlarla gözlendi**, **tekrarlı olarak desteklendi**. “Yayına hazır” ayrı kalite kapılarına bağlıdır.

## 5. Etik sınırlar

- Yönlendirmeli puan toplama, bağımlılık/yoksunluk, kayıp korkusu ve ruh sağlığı manipülasyonuna “etkili oyun mekaniği” deme.
- Kullanıcılar arasında farklı zevkleri ve erişilebilirlik gereksinimlerini koru.
- Katılımcı notlarını/görüntülerini izinsiz kalıcı depolama; sağlık veya kimlik bilgisi gereksizse toplama.
- Tasarım simülasyonu gerçek psikolojik deney değildir. Skill bu ayrımı kullanıcıya görünür yapar.

## v5 araç entegrasyonu

Gerçek kullanıcı oturumu planlamak için [user-research-protocol.md](user-research-protocol.md) kullan. Gözlemler özel CSV'ye rıza ile yazılır; analiz `scripts/evidence_lab.py study` ile yalnızca betimleyici yapılır. İnsan testi **yapılmadıysa** E3 seviyesine geçme. Referans/screenshot/pixel raporları katılımcı gözlemi değildir.
