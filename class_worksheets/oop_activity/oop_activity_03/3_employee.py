class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def update_salary(self, increase):
        self.salary += increase



emp = Employee("Alice", "Developer", 4000)

print("Salary:", emp.calculate_salary())
emp.update_salary(1000)
print("Updated Salary:", emp.calculate_salary())
