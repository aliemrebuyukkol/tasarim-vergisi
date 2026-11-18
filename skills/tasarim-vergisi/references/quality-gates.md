# Quality Gates: gerçek kanıtsız teslim yok

Her kapı için durum: **geçti | başarısız | engellendi | uygulanamaz**. `Engellendi` başarı değildir. Yayına aday olmak için release açısından zorunlu bütün kapılar geçmelidir.

## Öncelik düzeyleri

| Düzey | Örnek | Karar |
|---|---|---|
| P0 | veri kaybı, güvenlik açığı, çökme, ana akışın oynanamaması | blok |
| P1 | referans kadrajının bozulması, görünmeyen/takılan pet, kırık görev/navigasyon | blok |
| P2 | belirgin etkileşim, hizalama, performans veya erişilebilirlik kusuru | düzelt veya açık risk kabulü |
| P3 | küçük polish/kosmetik | raporla |

## Kalite kapıları

| Kapı | Kanıt | Gereklilik |
|---|---|---|
| G0 Kaynak | gerçek referans, hedef, erişim sınırı | kaynak görmeden sadakat iddiası yok |
| G1 Design DNA | sürümlü token/spacing/motion/kamera/asset | bütün ajanlar aynı kuralları kullanıyor |
| G2 Yapısal | proje build, lint, typecheck/test logu | mevcut doğru komut çalıştırıldı |
| G3 Davranış | ana akış, geri/iptal, hata, pause, save/load | senaryo yeniden üretilebilir |
| G4 Görsel | aynı viewport/state kaynak+çıktı screenshot; motion için video | ölçülebilir sapmalar ve düzeltmeler |
| G5 Erişilebilirlik | focus/VoiceOver veya screen reader, kontrast, reduced-motion | yığına uygun kontroller |
| G6 Performans | gerçek cihaz/ortam, çözünürlük, p50/p95 frame-time, bellek | hedef bütçeyle karşılaştırıldı |
| G7 Güvenlik/lisans | izin, kullanıcı verisi, asset lisansı, web güvenliği | riskler belgelendi |
| G8 Entegrasyon/release | temiz build, smoke, sürüm, rollback, izin | yayın kapsamına uygun |

## Görsel QA

1. Aynı viewport ve aynı UI/sahne durumunu yakala.
2. Kompozisyon, karakter/pet boyu, kamera açısı, typography, grid/1–2 px hizalar (mümkünse), katman, boşluk, safe area ve kontrastı karşılaştır.
3. Motion için aynı başlangıç/ara/son kareler ve süre ölçümünü kullan; statik görselden easing iddia etme.
4. Farkları hata ya da gerekçeli sapma olarak sınıflandır. Düzeltme sonrası yeni ekran/video yakala; eski ekran yeni kodun kanıtı değildir.

## Oyun test matrisi

Pet takip, engel ve occlusion, ekran dışına çıkma, zorlanmış dönüş; oyuncu collision, giriş gecikmesi ve kamera sınırı; görev tekrar tetikleme, pause/skip/retry; checkpoint, force quit, bozuk kayıt; düşük donanımda frame-time/ısınma/bellek; erişilebilir kontrol, ses kapalı, reduced-motion ve altyazı.

## QUALITY-REPORT.md şablonu

```markdown
# QUALITY-REPORT
Commit/sürüm:
Yığın / cihaz / OS / viewport:
Test/hedef ölçüm yöntemi:
| Kapı | Durum | Çalıştırılan komut / yöntem | Kanıt | Risk |
|---|---|---|---|---|
Açık P0/P1/P2 sorunlar ve sahipleri:
Kasıtlı görsel sapmalar:
Erişim yüzünden ölçülemeyenler:
FPS/frame-time (p50/p95), bellek, asset bütçesi (varsa):
Sonuç: sınırlı prototip | engellendi | doğrulanmış kapsam | yayın adayı
```

Bir kapının çalıştırılamaması `engellendi`, uygulanacak bağlamın olmaması `uygulanamaz` olarak işaretlenir; ikisini birbirine karıştırma.

## V3 özgünlük ve algı kalite kapıları

- **G9 Algı:** İlk bakış hiyerarşisi ve hedef eylem açıklanmış mı? Statik referanstan motion doğrulandı iddiası var mı?
- **G10 Yapısal özgünlük:** Baseline ile öneri hangi mekanik/kompozisyon/ritim farkında ayrışıyor? Değişiklik sadece paletse başarısız. Referansın özellikle sabit tutulması istenen yönler bu eleştiriyle bozunmaz.
- **G11 Eleştiri:** En güçlü karşı görüş, alınan karar ve neden kaydedilmiş mi? Ayrı model veya kullanıcı testi yoksa iddia edilmiyor mu?
- **G12 İnsan kanıtı:** Kullanıcı testi yapılmadıysa "insan tarafından beğenildi" denmemiş mi? Hipotezler kendi kanıt sınıfında mı?

G9/G10/G11 araştırma ve yaratıcı işlerde; G12 yalnızca kullanıcı yararı veya beğeni iddiasında bulunuluyorsa release değerlendirmesine eklenir. Bunlar eski G0–G8 kapılarına alternatifi değil ekidir.


## G13 İnsan algısı ve yaratıcı kalite (v4)

- **Algı hipotezi:** Dikkat/akıcılık/merak/şaşırma/hatırlama adımları, kaynak gözlemi ve model yorumu ayrılmış mı?
- **Karşı hipotez:** En az bir kullanıcının fikri neden sevemeyebileceği ve bunu nasıl öğreneceğimiz yazılmış mı?
- **Gerçek kontrol:** Human-Lens anlatıları sahte kullanıcı alıntısı gibi değil, E0 test edilebilir simülasyonlar olarak etiketli mi?
- **Duygu beyanı:** Gerçek kullanıcı verisi olmayan beğeni, şaşkınlık ve duygusal etki iddiaları yalnızca hipotez olarak mı sunulmuş?
- **Yaratıcı gerekçe:** Beklenmedik tasarım, mekanik/oyuncu kontrolü/anlatı gibi yapısal fark yaratıyor mu, yoksa sadece renk/konfeti mi?
- **Sınır:** Erişilebilirlik, reduced-motion, ses kapalı, skip/exit, etik ve mental sağlık riskleri kontrol edildi mi?
- **Araç:** `python3 scripts/experience_audit.py examples/pet-game-human-lens.json` bir **şema kontrolüdür**; insan algı veya beğeni kanıtı değildir.

Ürün hakkında ileri sürülen psikolojik iddialar için E3/E4 kanıtı yoksa “doğrulandı” denmez. E0/E1 ile iyi düşünülmüş konsept sunulabilir fakat insan araştırması yapılmış gibi anlatılamaz. Kullanıcı testi tek başına teknik/erişilebilirlik kapılarını geçirmiş sayılmaz.

## G14 Empirical Evidence (v5)

- Aynı viewport ve state için gerçek screenshot kaydı, gerçek hash, fark metrikleri ve manuel görsel inceleme var mı? Yoksa görsel sadakat **engellendi**.
- Video varsa referans + aday zaman noktası kıyası ve kare arası motion manuel değerlendirmesi var mı? Yalnız statik kareyle physics/60 FPS geçmez.
- Etkileşimler tarayıcıda/cihazda gerçekten oynatıldı mı? Console hatası ve kırılan görev rapora girdi mi?
- Kullanıcı seviyor/hissediyor iddiası varsa gerçek, rızaya dayalı kullanıcı gözlemi var mı? CSV yoksa E0 hipotezi korunur; uydurulmuş E3 yasaktır.
- Aynı test yeni commit üzerinde tekrarlandı mı? Eski sürüm screenshot'ı yeni sürümün kanıtı değildir.
- `scripts/evidence_lab.py gate` bir **kanıt toplama ve eşik kontrolü**dür; release veya klinik doğrulama belgesi değildir.

G14'te “insan kanıtı yok” teknik prototipin tamamını silmez; raporu **sınırlı doğrulama** yapar, beğeni iddiasını ise engeller. Kullanıcı testi genel bir üründe zorunlu olmayabilir; beğeni/duygu iddiasına koşuldur.
