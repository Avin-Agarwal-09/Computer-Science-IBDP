class Shape:
    def area(self):
        return None

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width *self.height


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

def total_area(shapes):
    total = 0
    for i in range(len(shapes)):
        total += shapes[i].area()
    return total

r = Rectangle(4, 5)
c = Circle(3)

print(r.area())     # 20
print(round(c.area(),2))  # 28.27

shapes = [r, c]
print(round(total_area(shapes),2))  # 48.27
