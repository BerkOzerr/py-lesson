# py-lesson

Python, NumPy ve pandas öğrenirken yazdığım alıştırmalar ve mini projeler.
Hedefim LLM / AI mühendisliği; bu repo o yolun ilk aşamasını (veri ve Python
temelleri) belgeliyor. Her klasör bir öğrenme adımıdır.

## Klasörler

| Klasör                  | Konu                               | Öne çıkanlar                                                                                                                |
| ----------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [`lesson-1`](lesson-1/) | Python temelleri, test yazma       | Rastgele ID üretici (`generate_id.py`) ve `pytest` testleri; `dataclass` ve JSON ile öğrenci yönetimi (`student_deneme.py`) |
| [`lesson-2`](lesson-2/) | NumPy                              | Dizi işlemleri, broadcasting, matris çarpımı (`@`, `np.dot`, `np.matmul`) ve şekil kuralları                                |
| [`lesson-3`](lesson-3/) | pandas, görselleştirme, istatistik | Sosyal medya kullanımı ve öğrenci refahı üzerine keşifsel veri analizi: [lesson-3/README.md](lesson-3/README.md)            |

## Kurulum

Python 3.11 veya üstü gerekir (3.13 ile geliştirdim).

```bash
git clone https://github.com/BerkOzerr/py-lesson.git
cd py-lesson

python -m venv .venv

.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux

pip install -r requirements.txt
```

## Testleri çalıştırma

Testler [pytest](https://docs.pytest.org/) ile yazıldı. Repo'nun ana klasöründen:

```bash
pytest lesson-1        # tüm testler
pytest lesson-1 -v     # ayrıntılı çıktı
```

Şu an `generate_id` fonksiyonu için testler var (uzunluk, izin verilen
karakterler, geçersiz girdilerde hata). Öğrenci yönetimi için testler henüz yok.

## Durum

- [x] Python temelleri, `pytest` ile test yazma
- [x] NumPy temelleri ve matris çarpımı notları
- [x] pandas: veri okuma, eksik değer, outlier analizi, korelasyon
- [x] Matplotlib / Seaborn ile ilk grafikler
- [ ] pandas: `groupby().agg()`, `pivot_table`, `merge`
- [ ] Karıştırıcı değişken (confounding) ve çoklu regresyon
- [ ] scikit-learn ile ilk makine öğrenmesi modelleri
