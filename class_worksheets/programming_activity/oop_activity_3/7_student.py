class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)



s = Student("Emma", "A")

s.add_course("Math")
s.add_course("Physics")
s.remove_course("Math")

print(s.name)
print("Courses:", s.courses)
