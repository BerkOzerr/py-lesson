from dataclasses import dataclass, field, asdict
import json
import string


@dataclass
class Student:
    name: str
    Nots: dict[str, list[int]] = field(default_factory=dict)

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Student name not empty")
        for lesson, nots in self.Nots.items():
            # print(lesson ,nots ,self.name)
            if not lesson.strip():
                raise ValueError("Lesson name not empty")
            for note in nots:
                # print(note)

                if not isinstance(note, int):
                    raise TypeError(f"{note} not string value")
                if note < 0 or note > 100:
                    raise ValueError(
                        f"Your note {note}  ,note should be  note > 0 and note < 100 "
                    )

    def lesson_avg(self, nots):
        return round(sum(nots) // len(nots))

    def average_not(self):
        response = {}
        for lesson, nots in self.Nots.items():
            avg = self.lesson_avg(nots)
            # print(avg)
            response[lesson] = {
                "notlar": nots,
                "ortalama": avg,
                "harf_Notu": self.harf_notu(avg),
            }
        # for lesson in self.Nots:
        #     notlar = self.Nots[lesson]
        #     avgNotlar = round(sum(notlar) // len(notlar))
        #     lessons_avg[lesson] = avgNotlar
        return response

    # def letter_grade(self):
    #     grades = self.average_not()
    #     # print(grades)
    #     sonuc = {
    #       lesson : self.harf_notu(grade)
    #       for lesson , grade in grades.items()
    #     }
    #     # for lesson, grade in grades.items():
    #     #     sonuc[lesson] = harf
    #     return sonuc

    def harf_notu(self, grade):
        if grade >= 85:
            return " AA"
        elif grade >= 75:
            return "BB"
        elif grade >= 65:
            return "CC"
        elif grade >= 57:
            return "DD"
        else:
            return "FF"


def main():

    while True:
        print(
            "0 -> Exit",
            "\n",
            "1 -> Add Student",
            "\n",
            "2 -> Remove Student",
            "\n",
            "3 -> Not Ekle",
            "\n",
            "4 -> Not Ortalamasi ",
            "\n",
            "5 -> Harf Notu",
            "\n",
            "6 -> List Student",
            "\n",
        )
        try:
            x = int(input("Yapmak istediğiniz işlemi seçiniz."))
        except ValueError:
            x = None
            print(f"value  should be integer and 0 , 6 values only")
        try:
            if isinstance(x, int):
                if x == 0:
                    return
                if x == 1:
                    add_Student()
                if x == 2:
                    remove_Student()
                if x == 6:
                    list_Student()
        except UnboundLocalError:
            print("\n")


def read_json():
    try:
        with open("student-1.json", "r", encoding="utf-8") as dosya:
            data_response = json.load(dosya)
            if data_response is not None:
                students = [Student(**datas) for datas in data_response]
                return students 

    except json.JSONDecodeError:
        print("Json dosyasinda bir hata mevcut parantezleri kontrol ediniz.")
        return []
    except FileNotFoundError:
        print("Json dosyasinin dosya yolunu doğru girdiğinizden emin olunuz.")
        return[]
    return []


def write_json(newStudents):
    with open("student-1.json", "w", encoding="utf-8") as dosya:
        json.dump(newStudents, dosya, ensure_ascii=False, indent=4)


def getir_input(talker):
    x = input(f"{talker} Student name :")
    x = x.strip()
    if isinstance(x, str) and x != "" and x not in string.digits:
        return x.title()
    else:
        return getir_input(talker)


def list_Student():
    students = read_json()
    for student in students:
        print(student)


def remove_Student():
    x = getir_input("remove")
    students = read_json()
    removeStudents = []
    for student in students:
        if student.name != x:
            removeStudents.append(student)
        else:
            print(f"{student.name} remove from list")
    removeStudents = [asdict(student) for student in removeStudents]
    write_json(removeStudents)


def add_Student():
    x = getir_input("add")
    print(x)
    students = read_json()
    if any( student.name == x for student in students):
        print(f"{x} kaydi zaten mevcuttur.")
    else :
        students.append(Student(x))
    newStudents = [asdict(student) for student in students]
    write_json(newStudents)
    print(newStudents)


if __name__ == "__main__":
    main()
