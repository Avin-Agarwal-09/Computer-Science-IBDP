class RectanglePlot:
    def __init__(self,length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Invalid Plot")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        if self.width == self.length:
            return True
        else:
            return False

    def resize(self,factor):
        self.width = factor * self.width
        self.length = factor * self.length
    
p1 = RectanglePlot(0, 0)
print(p1.area())         # 50
print(p1.perimeter())    # 30
print(p1.is_square())    # False

p1.resize(2)
print(p1.area())    # 200

p2 = RectanglePlot(4, 4)
print(p2.is_square())    # True

try:
    p3 = RectanglePlot(-3, 5)
except ValueError:
    print("Invalid plot") 