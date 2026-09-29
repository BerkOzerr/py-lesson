# py-lesson

Python, NumPy ve pandas öğrenirken yazdığım alıştırmalar ve mini projeler.
Her klasör bir öğrenme adımına karşılık gelir.

> Bu repo bir öğrenme günlüğüdür. Kodlar zamanla iyileştirilir, eski hatalar
> "Öğrendiklerim" bölümünde not edilir.

## İçindekiler

- [Proje yapısı](#proje-yapısı)
- [Kurulum](#kurulum)
- [Kullanım: ID üretici](#kullanım-id-üretici)
- [Testleri çalıştırma](#testleri-çalıştırma)
- [Öğrendiklerim](#öğrendiklerim)
- [Durum](#durum)

## Proje yapısı

<!-- Kendi dosya adlarına göre düzenle -->

```
py-lesson/
├── lesson-1/
│   ├── id_generator.py        # ID üretici (komut satırı + fonksiyon)
│   └── test_id_generator.py   # pytest testleri
├── lesson-2/                  # NumPy alıştırmaları
├── lesson-3/                  # pandas alıştırmaları
├── requirements.txt
├── .gitignore
└── README.md
```

## Kurulum

Python 3.10 veya üstü gerekir.

```bash
# 1. Repo'yu indir
git clone https://github.com/BerkOzerr/py-lesson.git
cd py-lesson

# 2. Sanal ortam oluştur
python -m venv .venv

# 3. Sanal ortamı etkinleştir
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux

# 4. Bağımlılıkları yükle
pip install -r requirements.txt
```

## Kullanım: ID üretici

Belirtilen uzunlukta rastgele bir ID üretir (küçük harf ve rakamlardan oluşur).

```bash
# Uzunluğu argüman olarak ver
python lesson-1/id_generator.py 8

# Argüman vermezsen uzunluk sorulur
python lesson-1/id_generator.py
```

Örnek çıktı (her çalıştırmada değişir):

```
o18xum59
```

Kurallar:

- Uzunluk **tam sayı** olmalı.
- Uzunluk **en az 1** olmalı.
- Geçersiz girdide program anlamlı bir hata mesajı verir.

Python içinden de kullanılabilir:

```python
from id_generator import generate_id

generate_id(8)       # "o18xum59"
generate_id(0)       # ValueError
generate_id("8")     # TypeError
```

## Testleri çalıştırma

Testler [pytest](https://docs.pytest.org/) ile yazıldı.

```bash
# Tüm testleri çalıştır
pytest

# Ayrıntılı çıktı (hangi test geçti / kaldı)
pytest -v

# Yalnızca adında "zero" geçen testleri çalıştır
pytest -k zero
```

Örnek çıktı (kendi çıktınla değiştir):

```
lesson-1/test_id_generator.py::test_valid_length PASSED        [ 25%]
lesson-1/test_id_generator.py::test_only_allowed_characters PASSED [ 50%]
lesson-1/test_id_generator.py::test_zero_raises PASSED         [ 75%]
lesson-1/test_id_generator.py::test_str_raises PASSED          [100%]

==================== 4 passed in 0.03s ====================
```

### Neyi test ediyoruz?

| Test                           | Kontrol ettiği şey                                               |
| ------------------------------ | ---------------------------------------------------------------- |
| `test_valid_length`            | Geçerli uzunluklarda (1, 2, 7, 8, 1000) sonuç uzunluğu doğru mu? |
| `test_only_allowed_characters` | Sonuç yalnızca küçük harf ve rakam içeriyor mu?                  |
| `test_zero_raises`             | `0` ve negatif sayılar `ValueError` fırlatıyor mu?               |
| `test_str_raises`              | Metin veya ondalık sayı `TypeError` fırlatıyor mu?               |

ID'ler rastgele üretildiği için testler sonucun _değerini_ değil, _özelliklerini_
(uzunluk, izin verilen karakterler, hata durumları) kontrol eder.

## Öğrendiklerim

Bu bölüm yaptığım hataları ve onlardan çıkardığım dersleri içerir.

- **`return` ile `raise` farkı:** `return ValueError(...)` hata fırlatmaz, sadece
  bir hata nesnesi döndürür. Hata durumunda `raise` kullanılır.
- **Sınır değerleri:** `x < 1` ile `x <= 1` farkı, 1 geçerli mi geçersiz mi
  sorusunu değiştirir. Sınır değerleri (0, 1, -1) her zaman test edilir.
- **`input()` ve `sys.argv` her zaman metin döndürür:** Sayı gerekiyorsa `int()`
  ile çevirmek ve çeviri hatasını ayrıca yakalamak gerekir.
- **Geniş `try` bloğu yanlış mesaj verebilir:** `try` içine yalnızca hata
  beklenen satırı koy.
- **pandas metodları çoğunlukla yeni nesne döndürür:** `df.fillna(...)` sonucu
  bir değişkene atanmazsa hiçbir şey değişmez.

## Durum

- [x] Python temelleri
- [x] NumPy temelleri
- [x] pandas temelleri
- [ ] ID üretici: testler ve README (devam ediyor)
- [ ] Sınıflar, dataclass, dosya işleme
- [ ] API ve hata yönetimi
- [ ] NumPy: matris çarpımı ve vektörizasyon
- [ ] pandas: kirli gerçek veri temizleme
