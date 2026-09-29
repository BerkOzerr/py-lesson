class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    ##__repr__ class hakkında bilgi almamızı yani geri dönüş alırken object değilde içeriği görmemizi sağlar
    def __repr__(self):
        return f"Name :{self.name} Age :{self.age} "

    def getStudent(self):
        return f"{self.name} ,{self.age} yaşinda."


def main():
    students = [Student("Berk", 28), Student("Emre", 28)]
    print(students)


if __name__ == "__main__":
    main()
