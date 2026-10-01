# Sosyal medya kullanımı ve öğrenci refahı: keşifsel veri analizi

Öğrencilerin günlük sosyal medya kullanımı ile uyku, stres, ruh sağlığı ve not
ortalaması arasındaki ilişkileri pandas, Matplotlib, Seaborn ve SciPy ile
inceleyen bir çalışma.

> **Önemli:** Bu analiz korelasyonları gösterir, nedensellik kanıtlamaz.
> Ayrıca veri seti gerçek bir ankete değil, üretilmiş (sentetik) veriye
> benziyor. Ayrıntılar [Sınırlılıklar](#sınırlılıklar) bölümünde.

## Araştırma sorusu

Günlük sosyal medya kullanım süresi arttıkça öğrencilerin uyku, stres, ruh
sağlığı ve akademik performans değerleri nasıl değişiyor?

## Veri

- **Dosya:** `Social_media_impact_on_life.csv` (4500 satır, 16 sütun)
- **Kaynak:** Kaggle, `harishyadav0506/impact-of-social-media-on-life`
  (lisans ve kullanım koşulları için Kaggle sayfasına bakın)
- **Sütunlar:**
  - Kimlik ve demografi: `Student_ID`, `Age`, `Gender`, `Academic_Level`
  - Kullanım: `Primary_Platform`, `Daily_Usage_Hours`, `Weekend_Extra_Hours`,
    `Device_Type`, `Late_Night_Usage`
  - Sonuçlar: `Sleep_Duration_Hours`, `Sleep_Quality_Score`,
    `Social_Comparison_Frequency`, `Perceived_Stress_Score`,
    `Mental_Health_Index`, `Academic_Performance_GPA`, `Overall_Impact`

## Yöntem

1. **Tanıma:** `shape`, `info()`, `describe()`, kategorik sütunlarda
   `value_counts()`.
2. **Eksik değerler:** İki sütunda eksik var, ortalama ile dolduruldu.
   - `Academic_Performance_GPA`: 85 eksik (%1,89)
   - `Perceived_Stress_Score`: 46 eksik (%1,02)
3. **Outlier analizi (IQR):** `Daily_Usage_Hours` için Q1 = 3,4, Q3 = 6,6,
   IQR = 3,2; sınırlar −1,4 ve 11,4. **162 gözlem** (%3,6) üst sınırın dışında.
   Outlier'lar silinmedi, çünkü veri hatası olduğuna dair bir kanıt yok. Bunun
   yerine outlier grubu ile normal grup karşılaştırıldı.
4. **Korelasyon:** Pearson katsayısı (`df.corr()`), korelasyon matrisi ve
   `scipy.stats.pearsonr` ile anlamlılık testi.

## Bulgular

### Outlier grubu ile normal grup

| Değişken               | Outlier (n = 162) | Normal |
| ---------------------- | ----------------- | ------ |
| Günlük kullanım (saat) | 12,92             | 5,01   |
| Uyku süresi (saat)     | 4,31              | 6,79   |
| Stres skoru            | 28,80             | 12,94  |
| Ruh sağlığı indeksi    | 47,91             | 81,07  |
| Not ortalaması (GPA)   | 2,62              | 3,46   |

Çok yüksek kullanım süresi olan öğrencilerde uyku ve ruh sağlığı belirgin
biçimde daha düşük, stres daha yüksek.

### Günlük kullanım süresi ile ilişkiler (Pearson)

| Değişken             | r      | p       |
| -------------------- | ------ | ------- |
| Ruh sağlığı indeksi  | −0,850 | < 0,001 |
| Stres skoru          | +0,751 | < 0,001 |
| Uyku süresi          | −0,716 | < 0,001 |
| Not ortalaması (GPA) | −0,704 | < 0,001 |
| Uyku kalitesi        | −0,681 | < 0,001 |

Diğer dikkat çeken ilişkiler: uyku süresi ile ruh sağlığı +0,774, stres ile
ruh sağlığı −0,770, ruh sağlığı ile GPA +0,653.

`pearsonr` çıktısında p-değeri `0.0` görünüyor. Bu gerçek bir sıfır değil,
değerin kayan noktalı sayı hassasiyetinin altında kalması. n = 4500 gibi büyük
bir örneklemde küçük p-değerleri zaten beklenir; yorumda asıl bakılması gereken
**r değeridir**.

### Grafikler

**Günlük kullanım ve ruh sağlığı (scatter):**
![Günlük kullanım ve ruh sağlığı](graphs/daily_hours_vs_mental_health.png)

**Günlük kullanım süresi dağılımı (boxplot):**
![Günlük kullanım boxplot](graphs/usage_boxplot.png)

**Korelasyon matrisi:**
![Korelasyon matrisi](graphs/correlation_matrix.png)

## Sınırlılıklar

- **Korelasyon nedensellik değildir.** Yüksek kullanım ile düşük ruh sağlığı
  arasındaki ilişki, kullanımın ruh sağlığını düşürdüğünü göstermez. Ters yön
  (ruh sağlığı düşük olanlar daha çok kullanıyor) ya da üçüncü bir değişken de
  olabilir.
- **Karıştırıcı değişkenler henüz incelenmedi.** Uyku, stres, ruh sağlığı ve
  GPA birbirleriyle de güçlü biçimde ilişkili.
- **Veri sentetik görünüyor.** `Daily_Usage_Hours` 14,0 değerinde kırpılmış
  (55 kişi tam 14,0), `Mental_Health_Index` 98'de (326 kişi) ve
  `Academic_Performance_GPA` 4,0'da (353 kişi) tavan yapıyor. Bu yüzden
  sonuçlar "bu veri setinde" geçerlidir, gerçek öğrenci nüfusuna
  genellenemez.
- **Kesitsel veri.** Her öğrenci tek bir zaman noktasında ölçülmüş; zaman
  içindeki değişim gözlenemiyor.
- **Eksik değerler ortalama ile dolduruldu.** Bu yöntem değişkenliği biraz
  azaltır ve korelasyonları hafifçe etkileyebilir.
- **Kategorik değişkenler henüz analiz edilmedi** (platform, cinsiyet,
  akademik seviye, gece kullanımı).

## Çalıştırma

Repo'nun ana klasöründeki kurulum adımlarından sonra:

```bash
cd lesson-3
python social_media_life.py
```

Script CSV'yi göreli yoldan okuduğu için `lesson-3` klasörünün içinden
çalıştırılmalıdır. Şu an ekrana korelasyon matrisini ve günlük kullanım ile
beş değişken arasındaki Pearson sonuçlarını yazdırır. Diğer analiz adımları
ve grafik kodları scriptte yorum satırı olarak duruyor; bir notebook'a
taşınacak.

## Yapılacaklar

- [ ] Analizi Jupyter notebook'a taşımak (kod ve kendi yorumlarım bir arada)
- [ ] `groupby().agg()` ve `pivot_table` ile platform, akademik seviye ve
      `Late_Night_Usage` gruplarını karşılaştırmak
- [ ] Eksik değerleri doldurmadan hesaplanan korelasyonları doldurulmuş
      olanlarla karşılaştırmak
- [ ] Karıştırıcı değişken (confounding) analizi ve çoklu doğrusal regresyon
- [ ] Scatter grafiğinde `alpha` kullanarak üst üste binen noktaları görünür
      yapmak

## Dosyalar

| Dosya                                                          | Açıklama                                                            |
| -------------------------------------------------------------- | ------------------------------------------------------------------- |
| `social_media_life.py`                                         | Ana analiz scripti                                                  |
| `Social_media_impact_on_life.csv`                              | Veri seti                                                           |
| `graphs/`                                                      | Üretilen grafikler                                                  |
| `pandas_1.py`, `pandas_2.py`, `pandas_ex.py`, `pandas_ex_2.py` | pandas temel alıştırmaları (Pokémon verisi ve küçük örnek tablolar) |
| `data.csv`, `data.json`                                        | Pokémon alıştırma verisi                                            |
