class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name)
        print(self.age)

students = []

for i in range(3):
    ism = input("Ism: ")
    yosh = int(input("Yosh: "))

    s = Student(ism, yosh)
    students.append(s)

for student in students:
    student.info()
