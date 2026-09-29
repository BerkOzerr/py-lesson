🎓 Student Management System

Python ile geliştirilmiş, JSON tabanlı basit bir öğrenci yönetim sistemi.

Bu proje ile öğrencilerin kaydedilmesi, silinmesi, listelenmesi ve öğrencilerin ders notlarının yönetilmesi amaçlanmaktadır.

🚧 Proje geliştirme aşamasındadır. Bazı özellikler henüz tamamlanmamıştır.

📌 Özellikler

Mevcut özellikler:

Öğrenci ekleme

Öğrenci silme

Öğrencileri listeleme

Öğrenci isimlerinin doğrulanması

Öğrenci verilerinin JSON dosyasında saklanması

Öğrenci ve not verileri için dataclass kullanımı

Notların 0-100 arasında kontrol edilmesi

Ders ortalaması hesaplama altyapısı

Harf notu hesaplama altyapısı

Planlanan özellikler:

Öğrenciye not ekleme

Öğrencinin ders notlarını görüntüleme

Ders ortalamalarını görüntüleme

Harf notlarını görüntüleme

Daha gelişmiş input doğrulama

Daha kullanıcı dostu terminal arayüzü

Hataların daha kapsamlı yönetilmesi

🛠️ Kullanılan Teknolojiler

Python 3

dataclasses

json

string

Projede harici bir Python kütüphanesi kullanılmamaktadır.

📂 Proje Yapısı
student-management/
│
├── main.py
├── student-1.json
└── README.md

Dosya isimleri projedeki mevcut yapıya göre değiştirilebilir.

🚀 Kurulum

Projeyi bilgisayarınıza klonlayın:

git clone <repository-url>

Proje klasörüne girin:

cd student-management

Python dosyasını çalıştırın:

python main.py

Windows üzerinde gerekirse:

py main.py

🎮 Kullanım

Program çalıştırıldığında aşağıdaki menü görüntülenir:

0 -> Exit
1 -> Add Student
2 -> Remove Student
3 -> Not Ekle
4 -> Not Ortalamasi
5 -> Harf Notu
6 -> List Student

Öğrenci Ekleme

1 seçeneği kullanılarak yeni öğrenci eklenebilir.

Örnek:

Yapmak istediğiniz işlemi seçiniz: 1

add Student name: Ahmet

Öğrenci daha önce kayıtlı değilse JSON dosyasına eklenir.

Öğrenci Silme

2 seçeneği ile kayıtlı bir öğrenci silinebilir.

remove Student name: Ahmet
Ahmet remove from list

Öğrencileri Listeleme

6 seçeneği ile kayıtlı öğrenciler görüntülenebilir.

💾 Veri Saklama

Öğrenci bilgileri JSON dosyasında tutulmaktadır.

Örnek veri:

[
{
"name": "Ahmet",
"Nots": {
"Matematik": [80, 90],
"Fizik": [70]
}
}
]

Program çalışırken JSON dosyasındaki veriler Student nesnelerine dönüştürülür.

Veriler kaydedilirken dataclasses.asdict() kullanılarak tekrar JSON formatına uygun hale getirilir.

📊 Not Sistemi

Projede mevcut harf notu sistemi:

Ortalama Harf Notu
85 - 100 AA
75 - 84 BB
65 - 74 CC
57 - 64 DD
0 - 56 FF

Notların 0 ile 100 arasında olması beklenmektedir.

🧱 Kod Yapısı

Projede öğrenci modeli için Python dataclass yapısı kullanılmaktadır:

@dataclass
class Student:
name: str
Nots: dict[str, list[int]] = field(default_factory=dict)

**post_init**() metodu ile öğrenci ve not bilgilerinin temel doğrulamaları yapılmaktadır.

Ders ortalaması ve harf notu hesaplama işlemleri de Student sınıfı içerisinde gerçekleştirilmektedir.

🎯 Projenin Amacı

Bu proje, Python'da aşağıdaki konularda pratik yapmak amacıyla geliştirilmiştir:

Object-Oriented Programming

dataclass

JSON ile veri okuma/yazma

Fonksiyonlar

Exception handling

Input validation

Liste ve dictionary kullanımı

Dosya işlemleri

🔮 Gelecek Geliştirmeler

Projenin ilerleyen aşamalarında:

Not ekleme sistemi tamamlanacak.

Öğrenci notları görüntülenebilecek.

Ders ortalamaları hesaplanacak.

Harf notları görüntülenecek.

Kod daha modüler hale getirilecek.

Daha kapsamlı hata yönetimi eklenecek.

Testler eklenecek.

📄 Lisans

Bu proje eğitim ve kişisel Python geliştirme çalışması amacıyla oluşturulmuştur.
