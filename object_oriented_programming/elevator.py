class Elevator:
    def __init__(self,min_floor,max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor =min_floor

    def move_up(self):
        if self.current_floor < self.max_floor:
            self.current_floor += 1
        
    def move_down(self):
        if self.current_floor > self.min_floor:
            self.current_floor -= 1
    
    def go_to_floor(self,floor):
        if floor < self.min_floor or floor > self.max_floor:
            raise ValueError
        self.current_floor = floor
    
    def status(self):
        return f"Current floor is: {self.current_floor}"
    
e = Elevator(1, 10)

print(e.status())   # Floor 1

e.move_up()
e.move_up()
print(e.status())   # Floor 3

e.go_to_floor(8)
print(e.status())   # Floor 8

e.move_up()
e.move_up()

try:
    e.go_to_floor(15)
except ValueError:
    print("Invalid floor")