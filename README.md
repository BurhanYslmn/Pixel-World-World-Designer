# Pixel Worlds — World Designer

Pixel Worlds için tarayıcıdan dünya tasarlama aracı. **Türkçe / English**, masaüstü ve mobil desteği.

**[Uygulamayı aç](https://burhanyslmn.github.io/Pixel-World-World-Designer/)** · **[GitHub](https://github.com/BurhanYslmn/Pixel-World-World-Designer)**

## Özellikler

- **Hazır dünya:** 80 × 57 hücre, **2560 × 1824 piksel** PNG çıktısı. Genişlik, yükseklik ve çıktı boyutu manuel değiştirilebilir.
- **Pixel Worlds kataloğu:** Blocks / Backgrounds / Props / Worlds; arama ve 20'li sayfalama.
- **Araçlar:** Taşı, Silgi, Damlalık, Klonla, Geri Al; isteğe bağlı katman üst üste yerleştirme.
- **Kayıt:** PNG indir veya JSON olarak kaydet; JSON dosyasını tekrar yükleyip **düzenlemeye devam et**.
- **Telefon:** Dokunarak çizim, iki parmakla yakınlaştırma, klon seçimi ve yerleştirme.
- **Dil:** Soldaki **TR / EN** menüsünden değiştirilebilir.

## Alan klonlama

1. Soldaki **Klonla / Clone** aracını seç.
2. Kopyalamak istediğin alanı fareyle veya parmağınla sürükleyerek seç.
3. Hedefe dokun/tıkla. Klon **önizleme** olarak belirir; henüz dünyaya işlenmez.
4. Önizlemenin üzerinde basılı tutup sürükleyerek konumu ayarla.
5. **✓** ile yerleştir, **×** ile iptal et. Onaylanan işlemi **Geri Al** ile geri çevirebilirsin.

Klonlama seçilen dikdörtgenin Background, Block ve Prop katmanlarını, boş hücrelerle birlikte kopyalar.

## GitHub Pages ile yayınlama

ZIP içeriğini (ZIP dosyasını değil) `Pixel-World-World-Designer` deposunun ana dizinine aktar. `index.html`, `styles.css`, `assets-manifest.js`, `Blocks/`, `Backgrounds/`, `Props/`, `Orbs/` klasörleri birlikte bulunmalı.

GitHub üzerinde **Settings → Pages → Deploy from a branch → main / (root) → Save** seç.

Yeni görsel ekledikten sonra kataloğu güncelle:

```bash
python scripts/generate-assets-manifest.py
```

---

**EN quick guide:** Default world is 80 × 57 blocks (2560 × 1824 px). Select **Clone**, drag to select cells, tap a destination to preview, drag to adjust, then press **✓** to confirm or **×** to cancel. Save and load editable JSON projects. Switch language from **TR / EN** in the Tools panel.
