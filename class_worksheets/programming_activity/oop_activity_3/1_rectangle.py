class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(5, 3)

print("Width:", r.width)
print("Height:", r.height)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
