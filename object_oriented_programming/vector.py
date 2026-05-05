class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return ((self.x)**2+ (self.y)**2)**0.5
    
    def __add__(self,other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
        
    def __str__(self):
        return (f"x value is: {self.x} y value is: {self.y}")
    
v1 = Vector2D(3,4)
v2 = Vector2D(1,2)

print(v1.magnitude())       # 5.0

v3 = v1 + v2
print(v3.x, v3.y)           # 4 6

print(v1 == Vector2D(3,4))  # True
print(v1 == v2)             # False

print(v3)                   # (4, 6)

v4 = Vector2D(-2,5)
v5 = v3 + v4
print(v5)                   # (2, 11)