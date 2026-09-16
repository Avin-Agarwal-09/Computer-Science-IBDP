class Employee:
    def __init__(self, name, salary, hire_year):
        self.name = name
        self.salary = salary
        self.hire_year = hire_year

    def years_of_service(self, current_year):
        return current_year - self.hire_year


emp = Employee("John", 4000, 2018)

print(emp.name)
print("Years of service:", emp.years_of_service(2025))
