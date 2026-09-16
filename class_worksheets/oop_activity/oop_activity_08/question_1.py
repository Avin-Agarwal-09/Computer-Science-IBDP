class Person:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
    
    def display(self):
        print(f"Name of student {self.name}, Age of student: {self.age}")

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    
    def display(self):
        print(f"Name of student {self.name}, Age of student: {self.age}, Grade of student {self.grade}")

class GraduateStudent(Student):
    def __init__(self,name,age,grade,thesisTitle):
        super().__init__(name,age,grade)
        self.thesisTitle = thesisTitle

    def display(self):
        print(f"Name of student {self.name}, Age of student: {self.age}, Grade of student {self.grade}, Thesis Title: {self.thesisTitle}")

student1 = GraduateStudent("Alice",25,"A","AI in healthcare")
student1.display()