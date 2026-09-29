from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int


students = [Student("Berk", 28), Student("Berk1", 28)]

# aylin = Student("Aylin", {"Fizik": [100, 80, 99, 90]})
# beril = Student(
#     "Beril", {"Almanca": [35, 24, 33, 44], "Veri Yapilari": [88, 70, 82, 100]}
# )
# emre = Student(
#     "Emre",
#     {
#         "Almanca": [32, 24, 33, 44],
#         "Veri Yapilari": [88, 70, 82, 100],
#         "Python": [90, 85, 95, 100],
#         "Matematik": [55, 60, 70, 65],
#     },
# )
# ali = Student(
#         "Ali",
#         {
#             "Almanca": [77, 84, 83, 64],
#             "Veri Yapilari": [88, 80, 82, 100],
#             "Python": [90, 85, 95, 100],
#             "Matematik": [100, 90, 70, 65],
#         },
#     )
# students = [
#     asdict(emre),
#     asdict(aylin),
#     asdict(ali),
#     asdict(beril)

# ]
# with open("student.json", "w", encoding="utf-8") as dosya:
#     json.dump(students, dosya, ensure_ascii=False, indent=4)
# students = []
# with open("student.json", "r", encoding="utf-8") as dosya:
#     veri = json.load(dosya)
#     # print(veri)

#     students = [Student(**val) for val in veri]


print(students)
