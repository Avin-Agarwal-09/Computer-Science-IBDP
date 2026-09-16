class TrafficLight:
    def __init__(self, colour, duration):
        self.colour = colour
        self.duration = duration

    def change_colour(self, new_colour, new_duration):
        self.colour = new_colour
        self.duration = new_duration

    def is_red(self):
        return self.colour == "red"

    def is_green(self):
        return self.colour == "green"



light = TrafficLight("red", 30)

print(light.is_red())     
light.change_colour("green", 45)
print(light.is_green())    
