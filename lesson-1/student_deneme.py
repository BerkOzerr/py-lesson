import json
from dataclasses import asdict, dataclass, field


@dataclass
class Student:
    name: str
    Nots: dict[str, list[int]] = field(default_factory=dict)

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Student name not empty")

    def lesson_avg(self, nots):
        return round(sum(nots) / len(nots), 2)

    def average_not(self):
        response = {}
        for lesson, nots in self.Nots.items():
            avg = self.lesson_avg(nots)
            # print(avg)
            response[lesson] = {
                "notes": nots,
                "ortalama": avg,
                "harf_notu": self.harf_notu(avg),
            }
            print(
                f"{self.name} in {lesson} dersin de notesi : {nots} \t ortalama :{avg} \t  harf Notu : {self.harf_notu(avg)} \n"
            )

        # print(self.name ,response , "\n")
        return response

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
            "4 -> Not Ortalamasi -Harf Notu ",
            "\n",
            "6 -> List Student",
            "\n",
        )
        try:
            x = int(input("Yapmak istediğiniz işlemi seçiniz."))
        except ValueError:
            x = None
            print("value  should be integer and 0 , 6 values only")
        try:
            if isinstance(x, int):
                if x == 0:
                    return
                if x == 1:
                    add_Student()
                if x == 2:
                    remove_student()
                if x == 3:
                    nots_add_student()
                if x == 4:
                    students = read_json()
                    for student in students:
                        student.average_not()
                if x == 6:
                    list_student()
        except UnboundLocalError:
            print("\n")


def read_json():
    try:
        with open("student_1.json", "r", encoding="utf-8") as dosya:
            data_response = json.load(dosya)
            if data_response is not None:
                students = [Student(**datas) for datas in data_response]
                return students

    except json.JSONDecodeError:
        print("Json dosyasinda bir hata mevcut parantezleri kontrol ediniz.")
        return []
    except FileNotFoundError:
        print("Json dosyasinin dosya yolunu doğru girdiğinizden emin olunuz.")
        return []
    return []


def write_json(newStudents):
    newStudents = [asdict(student) for student in newStudents]
    with open("student_1.json", "w", encoding="utf-8") as dosya:
        json.dump(newStudents, dosya, ensure_ascii=False, indent=4)


def not_Control(note_list):
    # print(notList.items())
    for lesson, nots in note_list.items():
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


def getir_input(talker):
    while True:
        x = input(talker).strip()

        if x and not x.isdigit():
            return x.title()

        print("Geçerli bir isim/değer giriniz.")
    # x = input(f"{talker}")
    # x = x.strip()
    # if isinstance(x, str) and x != "" and x not in string.digits:
    #     return x.title()
    # else:
    #     return getir_input(talker)


def list_student():
    students = read_json()
    for student in students:
        print(f"Adi : {student.name}")
        for i, val in student.Nots.items():
            print(f"{i} dersi notlari {val}")


def nots_add_student():
    students = read_json()
    if not students:
        add_Student()
    x = getir_input("Add nots Student name : ")
    exist = False

    for i, student in enumerate(students):
        if student.name == x:
            exist = True

            y = getir_input("Nots eklemek istediğiniz dersi seçiniz.")
            try:
                notes = list(map(int, input("notesi girin: ").split()))
                not_Control({y: notes})
            except (TypeError, ValueError) as e:
                print(f"Hata: {e}")
                return nots_add_student()
            if y in student.Nots:
                student.Nots[y].extend(notes)
                # for note in notes:
                #     student.Nots[y].append(note)
            # print(student.Nots[y])
            else:
                student.Nots[y] = notes
            break

    if not exist:
        print(f"Listede {x} isimli bir kayit bulunamadi.")
        return nots_add_student()
    write_json(students)
    # print(students)


def remove_student_linker(name, tempStudent):
    students = read_json()
    removeStudents = []
    for student in students:
        if student.name != name:
            removeStudents.append(student)
        else:
            print(f"{student.name} remove from list")
    removeStudents.append(tempStudent)
    # removeStudents = [asdict(student) for student in removeStudents]
    write_json(removeStudents)


def remove_student():
    x = getir_input("remove student name : ")
    students = read_json()
    removeStudents = []
    exist = False
    for student in students:
        if student.name != x:
            removeStudents.append(student)
        else:
            exist = True
            print(f"{student.name} remove from list")
    # removeStudents = [asdict(student) for student in removeStudents]
    print(f"don't find  list {x} name") if not exist else 0
    write_json(removeStudents)


def add_Student():
    x = getir_input("add student name : ")
    # print(x)
    students = read_json()
    if any(student.name == x for student in students):
        print(f"{x} kaydi zaten mevcuttur.")
        return
    else:
        print(f"{x} kaydi başariyla eklendi.")
        students.append(Student(x))
    # newStudents = [asdict(student) for student in students]
    write_json(students)
    # print(students)


if __name__ == "__main__":
    main()
