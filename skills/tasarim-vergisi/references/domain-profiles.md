# Domain Profiles: platforma özgü üretim ve test

Manifesti, mevcut kodu ve kullanılan motoru **gerçekten oku**. Test araçlarını kurulu varsayma; aşağıdakiler yalnızca uygun profilde değerlendirilir.

| Profil | Tasarım/mimari odağı | Doğrulama örnekleri |
|---|---|---|
| React/Next/web | semantik UI, responsive, state, defensive layout | mevcut lint/typecheck, Testing Library, Playwright, axe |
| SwiftUI/UIKit | safe-area, navigation, Dynamic Type, VoiceOver, lifecycle | xcodebuild, XCTest, UI test, Instruments |
| SpriteKit/RealityKit | scene graph, frame loop, collision, camera, asset pipeline | simülatör/cihaz gameplay smoke, profiling, XCTest |
| React Native/Flutter | native navigation, gestures, düşük cihaz performansı | Jest/Detox veya flutter test/integration_test |
| Web/Three.js oyun | render loop, resource disposal, camera, physics, WebGL context loss | browser gameplay smoke, frame-time/memory testi |
| Godot/Unity | sahne/prefab, fizik, kontroller, build target | motor test araçları, profiler, gerçek cihaz |
| Video/animasyon | frame/timeline, codec, ses senkronu, telif | çıktı izleme, zaman/kare/codec ve dosya denetimi |

**Three.js bir render kütüphanesidir**, tek başına tüm oyun sistemleri değildir. **SwiftUI bir UI çatısıdır**, karmaşık gameplay için SpriteKit/RealityKit/Metal veya uygun motor gerekebilir. Seçimi referans, cihaz, oyunun 2D/3D yükü ve ekibin yeteneği belirler.

## Platform kabul profili

`QUALITY-REPORT.md` içinde yığın/sürüm, hedef düşük cihaz, build/test komutları, minimum oynanabilir akış, erişilebilirlik koşulları, offline/kayıt, asset/render bütçesi ve gerçek test ortamını yaz.

60 FPS için teorik kare bütçesi 16,7 ms'dir; **gerçek başarı** yalnızca ölçülmüş p50/p95 frame-time, düşen kareler, pil/ısınma ve bellek ile gösterilir. Bütçeyi hedef cihazdan ve profil sonucundan türet.

- **iOS:** arka plan/ön plan, memory warning, ses, safe-area, Dynamic Type, VoiceOver, düşük güç.
- **Web:** dar viewport, klavye/focus, ağ kesintisi, prefers-reduced-motion, WebGL context loss.
- **Oyun:** pet occlusion/takılma, pause/resume, tekrarlı görev tetikleme, çakışan giriş, kayıt geri yükleme, ani sahne geçişi.
- **Video:** kare örnekleri, oynatma, render codec ve ses senkronu.

İlgisiz platform şartlarını brife sokma. Komut veya cihaz yoksa `engellendi` yaz; komut uydurma.
