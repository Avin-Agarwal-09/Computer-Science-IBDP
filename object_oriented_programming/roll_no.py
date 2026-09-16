class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"{self.roll_no}: {self.name}"


student = Student(1, "Avin")
print(student)

student.set_roll_no(2)
student.set_name("John")
print(student)
