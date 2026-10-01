import pandas as pd

df = pd.read_csv("Social_media_impact_on_life.csv")
# df= pd.read_csv(r"C:\Users\berke\Desktop\py-lesson\lesson-3\Social_media_impact_on_life.csv")

# print(df.shape)
# print(df.columns)
# print(df.isna().sum())
# print(df.info())

# missing = pd.DataFrame({
#   "Missing_Count" :df.isna().sum(),
#   "Missing_Percentage" : (df.isna().sum()/len(df))*100
# })


# missing = missing[missing["Missing_Count"]>0] #missing= missing.sort_values("Missing_Count",ascending=False)

# print(missing)

# print("PSS Mean:", df["Perceived_Stress_Score"].mean())

# print("PSS Median:", df["Perceived_Stress_Score"].median())

# print("APG Mean:", df["Academic_Performance_GPA"].mean())
# print("APG Median:", df["Academic_Performance_GPA"].median())

df["Perceived_Stress_Score"] = df["Perceived_Stress_Score"].fillna(
    df["Perceived_Stress_Score"].mean()
)

df["Academic_Performance_GPA"] = df["Academic_Performance_GPA"].fillna(
    df["Academic_Performance_GPA"].mean()
)

# print(df["Perceived_Stress_Score"].mean())

# print(df.loc[df["Perceived_Stress_Score"]<= df["Perceived_Stress_Score"].mean(),["Student_ID","Perceived_Stress_Score"]])
# print(df.loc[df["Perceived_Stress_Score"].isna()])
# print("Toplam eksik değer:", df.isnull().sum())
# print("Eksik değer var mi?", df.isnull().values.any())
# print(df.loc[(df["Age"]<25) & (df["Primary_Platform"]=="LinkedIn") ,["Age", "Gender", "Daily_Usage_Hours", "Weekend_Extra_Hours"]])
# print(df.info())
# print(df.describe())
"""
Daily_Usage_Hours
mean = 5.30
min  = 0.9
max  = 14

Ortalama bir öğrenci günde yaklaşik 5.3 saat sosyal medya kullaniyor.
"""

# print(df["Gender"].value_counts())
# print(df["Academic_Level"].value_counts())
# print(df["Primary_Platform"].value_counts())
# print(df["Device_Type"].value_counts())

import matplotlib.pyplot as plt
import seaborn as sns

"""
Eksik değerler → ✅
Veri tipleri → ✅
Kategorik dağilimlar → ✅
"""


# print(df["Daily_Usage_Hours"].median())

# plt.boxplot(df["Daily_Usage_Hours"])
# plt.title("Daily Usage Hours")
# plt.ylabel("Hours")
# plt.show()

Q1 = df["Daily_Usage_Hours"].quantile(0.25)
Q3 = df["Daily_Usage_Hours"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# print("Q1:", Q1)
# print("Q3:", Q3)
# print("IQR:", IQR)
# print("Lower bound:", lower)
# print("Upper bound:", upper)

outliers= df[(df["Daily_Usage_Hours"]< lower)| (df["Daily_Usage_Hours"]>upper)]
normal = df[
    (df["Daily_Usage_Hours"] >= lower) &
    (df["Daily_Usage_Hours"] <= upper)
]
# print("Outliner sayisi :",len(outliers))
# print("Outlier orani:", len(outliers) / len(df) * 100)

# print("Outlier grubunun ortalamalari:")
# print(outliers[["Daily_Usage_Hours","Sleep_Duration_Hours",
#           "Perceived_Stress_Score", "Mental_Health_Index",
#           "Academic_Performance_GPA"]].mean()) 

# print("\nNormal grubun ortalamalari:")
# print(normal[["Daily_Usage_Hours","Sleep_Duration_Hours",
#           "Perceived_Stress_Score", "Mental_Health_Index",
#           "Academic_Performance_GPA"]].mean()) 

# plt.scatter(df["Daily_Usage_Hours"],df["Mental_Health_Index"])
# plt.title("Daily Social Media Usage vs Mental Health")
# plt.xlabel("Daily Usage Hours")
# plt.ylabel("Mental Health Index")
# plt.show()

# correlation = df["Daily_Usage_Hours"].corr(
#     df["Mental_Health_Index"]
# )
##-0.8499077942620484
# correlation = df["Daily_Usage_Hours"].corr(
#     df["Academic_Performance_GPA"]
# )
##-0.7042632866310721

"""
Kabaca:

+1 → güçlü pozitif ilişki

0 → doğrusal ilişki yok

-1 → güçlü negatif ilişki

Örneğin -0.70 çikarsa, negatif yönlü ilişkinin oldukça belirgin olduğunu söyleyebiliriz.

Ama korelasyon da nedensellik anlamina gelmez. Yani yüksek sosyal medya kullaniminin mental sağlik düşüşüne neden olduğunu tek başina kanitlamaz.
"""

corr = df.corr(numeric_only=True)

print(corr)

"""
Daily Usage ↔ Sleep Duration

r = -0.716

Yani kullanim süresi arttikça uyku süresi düşme eğiliminde.

Sleep Duration ↔ Mental Health

r = +0.774

Uyku süresi arttikça mental health index'in yükselme eğilimi var.

Stress ↔ Mental Health

r = -0.770

Stres arttikça mental health index düşme eğiliminde.

"""


# plt.figure(figsize=(10, 8))

# sns.heatmap(
#     corr,
#     annot=True,
#     cmap="coolwarm",
#     fmt=".2f"
# )

# plt.title("Correlation Matrix")
# plt.show()

"""
figsize=(10, 8)

→ grafiğin boyutunu ayarliyor.

annot=True

→ hücrelerin içine korelasyon değerlerini yaziyor.

cmap="coolwarm"

→ negatif ve pozitif korelasyonlari farkli renklerle gösteriyor.

fmt=".2f"

→ değerleri iki ondalik basamakla gösteriyor.

Ve burada önemli bir öğrenme noktasi
Şimdiye kadar:

plt.scatter() → iki sayisal değişken arasindaki ilişki

plt.boxplot() → dağilim ve olasi outlier

sns.heatmap() → birçok değişken arasindaki korelasyonlari topluca görmek
"""

from scipy.stats import pearsonr

# r, p_value = pearsonr(
#     df["Daily_Usage_Hours"],
#     df["Mental_Health_Index"]
# )

# print(f"Correlation: {r:.4f}")
# print(f"P-value: {p_value:.10e}")

# r_gpa, p_gpa = pearsonr(
#     df["Daily_Usage_Hours"],
#     df["Academic_Performance_GPA"]
# )

"""
r = -0.85
↓
İlişkinin yönü: negatif
İlişkinin gücü: güçlü

p < 0.001
↓
İstatistiksel olarak anlamli

Nedensellik?
↓
Henüz bilmiyoruz

Daily_Usage_Hours
       ↓
       │
       ├── Pearson korelasyonunu hesapla → r
       │
       └── H₀: gerçek korelasyon = 0
                       ↓
                  test yap
                       ↓
                    p-value
p < 0.001
Daily_Usage_Hours ile Mental_Health_Index arasinda istatistiksel olarak anlamli,
 güçlü ve negatif bir doğrusal ilişki gözlenmektedir.

 pearsonr() için şimdilik şu cümleyi aklinda tut:

"İki sayisal değişken arasindaki doğrusal ilişkinin katsayisini (r) ve bu ilişkinin istatistiksel anlamliliğini değerlendirmek için kullanilan Pearson korelasyon testini hesaplar."

Ve bizim örneğimizde:

r = -0.8499
p < 0.001

→ güçlü negatif doğrusal ilişki + istatistiksel olarak anlamli sonuç.
"""


"""
1. Daily Usage ↔ Sleep Duration
r = -0.7159
Günlük sosyal medya kullanım süresi arttıkça uyku süresinin daha düşük olma eğilimi görülüyor.
 Daily Usage ↔ Sleep Quality
r = -0.6813

Burada da negatif ilişki var.

Daha fazla günlük kullanım, daha düşük uyku kalitesi skorlarıyla birlikte görülme eğiliminde.

3. Daily Usage ↔ Perceived Stress
Burada yön değişiyor:

r = +0.7507

Pozitif.

Yani:

Günlük kullanım süresi arttıkça algılanan stres skorunun da daha yüksek olma eğilimi görülüyor.

Bu önemli çünkü Daily Usage ile stres arasındaki ilişki, uyku ve mental health'teki ilişkilerin tersine pozitif.

4. Daily Usage ↔ Mental Health
En güçlü korelasyonumuz:

r = -0.8499

Günlük kullanım süresi ile Mental Health Index arasında çok güçlü negatif doğrusal ilişki gözleniyor.

5. Daily Usage ↔ GPA
r = -0.7043

Yine negatif ve güçlü.

Günlük kullanım süresi arttıkça GPA'nın daha düşük olma eğilimi görülüyor.
"""
# variables = [
#     "Sleep_Duration_Hours",
#     "Sleep_Quality_Score",
#     "Perceived_Stress_Score",
#     "Mental_Health_Index",
#     "Academic_Performance_GPA"
# ]
# for variable in variables:
#     r,p_value = pearsonr(
#         df["Daily_Usage_Hours"],
#         df[variable]
#     )
    # print(f"Daily Usage Hours and {variable}")
    # print(f"Correlation: {r:.4f}")
    # print(f"P-value: {p_value:.10e}")

# r,p_value =pearsonr(
#   df["Perceived_Stress_Score"],
#   df["Mental_Health_Index"]
# )
# print(f"Stress and Mental Health")
# print(f"Correlation : {r:.4f}")
# print(f"P-value : {p_value:.10e}")

"""
Daily Usage ile Mental Health arasındaki güçlü ilişkiyi başka değişkenler nasıl etkiliyor?
                    ┌── Sleep Duration  (-0.716)
                    │
                    ├── Sleep Quality   (-0.681)
Daily Usage ────────┼── Stress          (+0.751)
                    │
                    ├── Mental Health   (-0.850)
                    │
                    └── GPA             (-0.704)

"""