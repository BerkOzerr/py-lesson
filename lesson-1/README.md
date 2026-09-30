Python Practice Projects

Python öğrenme sürecimde geliştirdiğim küçük uygulamalar ve çalışmalar.

Bu repository; Python'da temel programlama konularını, veri yapılarını, hata yönetimini, dosya işlemlerini, dataclass kullanımını ve command-line argument işlemlerini pratik etmek amacıyla oluşturulmuştur.

Projeler
Student Management System

Öğrenci, ders ve not bilgilerini yönetmek için geliştirilmiş basit bir CLI uygulaması.

Kullanılan yapılar:

dataclass

dict ve list

JSON dosyası ile veri saklama

Öğrenci ekleme ve silme

Ders ekleme

Bir ders için birden fazla not saklama

Notların 0-100 arasında doğrulanması

Ders ortalaması hesaplama

Harf notu hesaplama

try/except ile hata yönetimi

Veriler student_1.json dosyasında saklanır.

Örnek veri yapısı:

[
{
"name": "Ali",
"Nots": {
"Almanca": [100, 90, 45],
"İngilizce": [80, 75]
}
}
]

Random ID Generator

Belirtilen uzunlukta rastgele ID oluşturan command-line uygulaması.

ID içerisinde:

Küçük harfler

Rakamlar

kullanılır.

Örneğin:

a72k039xq1

ID uzunluğu terminal argument'i olarak verilebilir:

python generate_id.py 10

Eğer argument verilmezse program kullanıcıdan uzunluğu ister:

python generate_id.py

Örnek:

Enter your id size: 10
a72k039xq1

Geçersiz bir değer girildiğinde hata kontrolü yapılır.

Kullanılan Python Konuları

Bu repository içerisinde aşağıdaki Python konuları üzerinde çalışıyorum:

Variables ve data types

if / elif / else

for ve while döngüleri

Functions

Exception handling

try / except

list

dict

Nested data structures

dataclass

field(default_factory=...)

JSON

File I/O

sys.argv

Command-line arguments

random

string

Type checking

Input validation

Amaç

Bu repository'nin amacı büyük bir proje geliştirmekten ziyade Python'un temel ve orta seviye özelliklerini küçük projeler üzerinden öğrenmek ve pratik etmektir.

Projeler geliştikçe yeni özellikler ve yeni Python konuları eklenecektir.

Çalıştırma

Python 3 yüklü olduğundan emin olun.

Örneğin:

python generate_id.py 10

veya:

python generate_id.py

Student Management System için:

python student.py

Git Commit Yapısı

Projede değişiklikleri mümkün olduğunca anlamlı commit mesajlarıyla takip etmeye çalışıyorum.

Örnek:

feat: add grade validation and average calculation
feat: add CLI support for random ID generation
fix: prevent invalid grades from being saved
