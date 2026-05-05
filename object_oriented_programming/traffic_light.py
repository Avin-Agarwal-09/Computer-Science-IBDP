class TrafficLight:
    def __init__(self,state):
        self.state = ["Red", "Green", "Yellow"]
        self.current_state = 0

    def next(self):
        self.current_state = (self.current_state + 1) % 3
        
        # if self.current_state == "Red":
        #     self.current_state = "Green"
        # elif self.current_state == "Green":
        #     self.current_state = "Yellow"
        # elif self.current_state == "Yellow":
        #     self.current_state = "Red"
    
    def get_state(self):
        return (self.state[self.current_state])
        
    def is_safe_to_cross(self):
        if self.state[self.current_state] == "Red":
            return ("Safe to cross")
        elif self.state[self.current_state] == "Yellow":
            return ("Cross with Caution")
        elif self.state[self.current_state] == "Green":
            return ("DO NOT CROSS!!!!!")

t = TrafficLight("Red")

print(t.get_state())          # Red
print(t.is_safe_to_cross())   # False

t.next()
print(t.get_state())          # Green
print(t.is_safe_to_cross())   # True

t.next()
print(t.get_state())          # Yellow

t.next()
print(t.get_state())          # Red