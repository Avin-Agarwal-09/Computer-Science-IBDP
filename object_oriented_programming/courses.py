class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self,student_id):
        random = []
        for i in range(len(self.students)):
            if  student_id != self.students[i].id:
                random.append(self.students)
            else:
                continue
        self.students = random
    
    def find_student(self,student_id):
        for i in range(len(self.students)):
            print(self.students[i].id)
            if  student_id == self.students[i].id:
                return self.students[i]
            else:
                continue
    
    def total_students(self):
        return len(self.students)

s1 = Student(1, "Anna")
s2 = Student(2, "Ben")

c = Course("IB HL CS")
c.add_student(s1)
c.add_student(s2)

print(c.students)

print(c.total_students())      # 2
print(c.find_student(2).name)  # Ben

c.remove_student(1)
print(c.total_students())      # 1
