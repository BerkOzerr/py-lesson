Bir veri analizi projesi yapıyorum ve Python/Pandas/Matplotlib/Seaborn/Scipy öğreniyorum. Bana konuları hazır cevap olarak vermek yerine, proje üzerinden adım adım ve öğretici şekilde anlat.

Veri setim:

4500 satır

16 sütun

Öğrenci sosyal medya kullanımı, uyku, stres, mental sağlık ve akademik performans verileri içeriyor.

Sütunlar:
Student_ID, Age, Gender, Academic_Level, Primary_Platform, Daily_Usage_Hours, Weekend_Extra_Hours, Device_Type, Sleep_Duration_Hours, Sleep_Quality_Score, Late_Night_Usage, Social_Comparison_Frequency, Perceived_Stress_Score, Mental_Health_Index, Academic_Performance_GPA, Overall_Impact

Şu ana kadar yaptıklarımız:

CSV'yi Pandas ile okuduk ve veri setini tanıdık.

isnull() / isna() arasındaki farkı öğrendik. Pratikte ikisinin aynı işi yaptığını öğrendik.

Eksik değerleri inceledik:

Academic_Performance_GPA: 85 eksik (%1.8889)

Perceived_Stress_Score: 46 eksik (%1.0222)

Ortalama ve medyanları hesapladık:

PSS Mean: 13.512123933542883

PSS Median: 13.0

GPA Mean: 3.4292819932049827

GPA Median: 3.46

Eksik değerleri ortalama ile doldurduğumuz için bazı PSS değerlerinin 13.512124 gibi görünmesinin nedenini öğrendik.

info(), describe() ve kategorik değişkenlerde value_counts() kullandık.

Daily_Usage_Hours üzerinden outlier analizi yaptık.

Q1 = 3.4

Q3 = 6.6

IQR = 3.2

Lower bound = -1.4

Upper bound = 11.4

Outlier sayısı = 162

Outlier oranı = %3.6

Outlier'ları otomatik olarak silmemeye karar verdik. Çünkü outlier olmak veri hatası olmak zorunda değil.

Outlier grubunun ortalamalarını normal grupla karşılaştırdık:

Outlier Daily Usage: 12.921605

Normal Daily Usage: 5.011157

Outlier Sleep Duration: 4.311111

Normal Sleep Duration: 6.790595

Outlier PSS: 28.796446

Normal PSS: 12.941340

Outlier Mental Health: 47.913580

Normal Mental Health: 81.066621

Outlier GPA: 2.622831

Normal GPA: 3.459398

Matplotlib ile scatter plot yaptık ve grafiği yorumlamayı öğrendik.

Daily_Usage_Hours ile Mental_Health_Index arasında scatter plot çizdik ve negatif yönlü ilişkiyi gözlemledik.

Pearson korelasyonunu öğrendik.

df["x"].corr(df["y"]) ile korelasyon katsayısı hesapladık.

scipy.stats.pearsonr() kullanmayı öğrendik.

Pearson'ın matematiksel olarak nasıl hesaplandığını küçük bir örnekle elle öğrendik.

r değerinin ilişkinin yönünü ve gücünü, p-value değerinin ise istatistiksel anlamlılığı değerlendirmede kullanıldığını öğrendik.

Korelasyonun nedensellik olmadığını özellikle vurguladık.

Correlation matrix ve Seaborn heatmap oluşturduk.

Sayısal değişkenler arasındaki önemli korelasyonları gördük:

Daily Usage ↔ Mental Health: -0.849908

Daily Usage ↔ GPA: -0.704263

Daily Usage ↔ Sleep Duration: -0.715903

Daily Usage ↔ Sleep Quality: -0.681290

Daily Usage ↔ Perceived Stress: +0.750678

Sleep Duration ↔ Mental Health: +0.774220

Sleep Quality ↔ Mental Health: +0.662423

Perceived Stress ↔ Mental Health: -0.769570

Perceived Stress ↔ GPA: -0.641341

Mental Health ↔ GPA: +0.653173

Pearson testlerini Daily_Usage_Hours ile şu değişkenler arasında yaptık:

Sleep_Duration_Hours: r = -0.7159, p < 0.001

Sleep_Quality_Score: r = -0.6813, p < 0.001

Perceived_Stress_Score: r = +0.7507, p < 0.001

Mental_Health_Index: r = -0.8499, p < 0.001

Academic_Performance_GPA: r = -0.7043, p < 0.001

pearsonr() çıktısında p-value'nun 0.0000000000e+00 görünmesinin gerçek matematiksel olarak p=0 anlamına gelmediğini, değerin görüntüleme hassasiyetinin altında kaldığını öğrendik.

Python'da for döngüsü kullanarak aynı Pearson analizini birden fazla değişkene uygulamayı öğrendik.

ŞU ANDA TAM OLARAK KALDIĞIMIZ YER:

Pearson analizini tamamladık. Bir sonraki adım olarak Correlation vs. Causation ve özellikle confounding (karıştırıcı değişken) kavramını kendi veri setimiz üzerinden öğrenmek istiyoruz.

Özellikle şu yapıyı inceleyeceğiz:

Daily Usage
├── Sleep Duration (-0.716)
├── Sleep Quality (-0.681)
├── Stress (+0.751)
├── Mental Health (-0.850)
└── GPA (-0.704)

Ayrıca:

Sleep Duration ↔ Mental Health = +0.774

Stress ↔ Mental Health = -0.770

Mental Health ↔ GPA = +0.653

Bundan sonra ileride multiple linear regression konusuna geçebiliriz ama hemen atlama. Önce confounding kavramını ve korelasyonun nedensellik olmadığını öğretici şekilde anlat, sonra veri setimiz üzerinde bunu inceleyelim.

Önemli öğrenme tarzı:

Bana kodu sadece verip geçme; kodun ne yaptığını ve neden yaptığımızı açıkla.

Küçük örneklerle kavramları öğret.

Ben kodu çalıştırıp çıktıyı sana göndereyim, sen sonucu yorumla.

Gereksiz yere ileri konulara atlama.

"Bu değişkeni neden seçiyoruz?" sorusunu sürekli önemse.

Veri analizinde tek bir "doğru yol" olmadığını, araştırma sorusuna göre yöntemin seçildiğini öğret.

Korelasyon ile nedenselliği birbirine karıştırmamamı sağla.

Proje üzerinden Python öğrenmeye devam edelim.

Şu anda özellikle confounding → multiple regression yolunda ilerliyoruz.
