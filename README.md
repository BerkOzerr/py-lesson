🐍 Python Learning Repository

Python öğrenme sürecimde yazdığım dersler, alıştırmalar, mini projeler ve testler.

Bu repository'yi sadece tamamlanmış projeleri göstermek için değil, öğrenme sürecimi ve zaman içinde geliştirdiğim kodları takip etmek için kullanıyorum.

Kodlar geliştikçe eski çözümler iyileştiriliyor, yeni konular ekleniyor ve karşılaştığım problemler not ediliyor.

📚 İçerik

Repository içerisinde farklı Python konularını ve küçük projeleri aşamalı olarak çalışıyorum.

🐍 Python Fundamentals

Variables ve data types

if / elif / else

for ve while

Functions

Lists

Dictionaries

Nested data structures

User input

Exception handling

try / except

🧱 Object-Oriented Python

Classes

Objects

dataclass

**post_init**

Methods

Type annotations

field(default_factory=...)

📁 File Handling

JSON

JSON'dan veri okuma

JSON'a veri yazma

Python objelerini JSON'a dönüştürme

asdict()

🧪 Testing

pytest

Unit tests

Exception testing

Edge cases

Input validation

🔢 NumPy

NumPy ile temel veri yapıları ve matematiksel işlemler üzerine alıştırmalar.

🐼 pandas

pandas kullanarak veri okuma, temizleme ve veri üzerinde işlem yapma çalışmaları.

💻 Command Line

sys.argv

Terminalden parametre alma

input() ile kullanıcıdan veri alma

CLI input validation

🚀 Mini Projects
Random ID Generator

Belirtilen uzunlukta rastgele ID oluşturan küçük bir CLI uygulaması.

ID'ler:

Küçük harfler

Rakamlar

kullanılarak oluşturulur.

Örneğin:

a72k039xq1

Terminalden uzunluk verilebilir:

python lesson-1/id_generator.py 10

Argument verilmezse program kullanıcıdan uzunluğu ister:

python lesson-1/id_generator.py

Python içerisinden de kullanılabilir:

from id_generator import generate_id

generate_id(10)

Geçersiz değerler için validation uygulanmaktadır.

Student Management System

Öğrencileri, dersleri ve notları yönetmek için geliştirdiğim CLI tabanlı uygulama.

Uygulamada:

Öğrenci ekleme

Öğrenci silme

Ders ekleme

Bir derse birden fazla not ekleme

Notları 0-100 arasında doğrulama

Ders ortalaması hesaplama

Harf notu hesaplama

Öğrenci listesini görüntüleme

JSON dosyasında veri saklama

özellikleri üzerinde çalışıyorum.

Veri yapısı temel olarak:

[
Student(
name="Ali",
Nots={
"Almanca": [100, 90, 45],
"İngilizce": [80, 75]
}
)
]

şeklindedir.

JSON'a kaydedildiğinde:

[
{
"name": "Ali",
"Nots": {
"Almanca": [100, 90, 45],
"İngilizce": [80, 75]
}
}
]

şeklinde saklanır.

🧪 Testing

Projelerde özellikle edge case'leri test etmeye çalışıyorum.

Örneğin ID generator için:

pytest

ve ayrıntılı çıktı için:

pytest -v

kullanılabilir.

Testlerde özellikle:

Geçerli input

0

Negatif değerler

String değerler

Geçersiz input

Sonuç uzunluğu

Üretilen karakterlerin geçerliliği

gibi durumları kontrol ediyorum.

📂 Repository Structure
py-lesson/
│
├── lesson-1/
│ ├── id_generator.py
│ └── test_id_generator.py
│
├── lesson-2/
│ └── ...
│
├── lesson-3/
│ └── ...
│
├── requirements.txt
├── .gitignore
└── README.md

Repository büyüdükçe yeni dersler ve projeler bu yapıya eklenecek.

⚙️ Installation

Python 3.x gereklidir.

Repository'yi klonlayın:

git clone https://github.com/BerkOzerr/py-lesson.git
cd py-lesson

Sanal ortam oluşturmak için:

python -m venv .venv

Windows:

.venv\Scripts\activate

macOS / Linux:

source .venv/bin/activate

Bağımlılıkları yüklemek için:

pip install -r requirements.txt

▶️ Running the Projects

Örneğin ID generator:

python lesson-1/id_generator.py 10

Testleri çalıştırmak için:

pytest

Ayrıntılı test çıktısı:

pytest -v

💡 Öğrendiklerim

Bu repository'nin önemli bir amacı da karşılaştığım hataları ve öğrendiğim noktaları kaydetmek.

Şu ana kadar özellikle:

input() ve sys.argv değerlerinin string olarak gelmesi

int() dönüşümü ve ValueError

raise ile return arasındaki fark

try/except kapsamının hata mesajlarına etkisi

list, dict ve iç içe veri yapıları

dataclass kullanımı

**post_init**

JSON serialization / deserialization

asdict()

default_factory

Input validation

Edge case testleri

pytest

CLI uygulamalarında kullanıcı girdisi kontrolü

üzerinde çalışıyorum.

📈 Progress

Repository aktif olarak geliştirilmektedir.

Öğrenme sırası kesin ve tamamlanmış bir müfredat değildir. Yeni konular öğrendikçe eski kodlar da yeniden düzenlenmektedir.

Python basics

Lists & dictionaries

Functions

Exception handling

JSON / file handling

CLI arguments

Basic testing

Dataclass

Student management mini project

Random ID generator

Daha kapsamlı unit tests

Daha gelişmiş OOP

API çalışmaları

Daha büyük Python projeleri

🎯 Repository Goal

Bu repository'nin amacı Python'u sadece teorik olarak öğrenmek yerine kod yazarak, hata yaparak, test ederek ve mevcut kodu geliştirerek öğrenmek.

Zaman içerisinde bu repository'nin daha büyük Python projelerine geçiş için bir öğrenme günlüğü ve referans noktası haline gelmesini hedefliyorum.

👨‍💻 Author

Berk Özer

GitHub: BerkOzerr
