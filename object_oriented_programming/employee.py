class Employee:
    def __init__(self,name):
        self.name = name

    def calculate_salary(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
        
    def calculate_salary(self):
        return self.salary
        
        
class PartTimeEmployee(Employee):
    def __init__(self,name,salary,hours):
        super().__init__(name)
        self.salary = salary
        self.hours = hours
    def calculate_salary(self):
        return self.hours*self.salary
            


e1 = FullTimeEmployee("Sarah", 4000)
print(e1.calculate_salary())    # 4000

e2 = PartTimeEmployee("Tom", 20, 80)
print(e2.calculate_salary())    # 1600

employees = [e1, e2]
for e in employees:
    print(e.calculate_salary())
# Expected: 4000, 1600