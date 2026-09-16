class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius



c = Circle(5)

print("Area:", c.area())
print("Circumference:", c.circumference())

c.radius = 10 
print("New Area:", c.area())
