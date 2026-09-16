class Staff:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def display(self):
        print(f"Name of staff member: {self.name}, ID of staff member: {self.ID}")

class Professor(Staff):
    def __init__(self, name, ID, specialization):
        super().__init__(name,ID)
        self.specialization = specialization
    
    def display(self):
        print(f"Name of staff member: {self.name}, ID of staff member: {self.ID}, Specialization of staff member: {self.specialization}")
    
class TeachingAssistant(Staff):
    def __init__(self, name, ID, courseAssigned):
        super().__init__(name,ID)
        self.courseAssigned =  courseAssigned
    
    def display(self):
        print(f"Name of staff member: {self.name}, ID of staff member: {self.ID}, course of staff member: {self.courseAssigned}")
    
    
professor1 = Professor("Julian", "1JFUSD37","Computer science")
professor1.display()

assistant1 = TeachingAssistant("Rayed","237DFJ","Physics HL")
assistant1.display()