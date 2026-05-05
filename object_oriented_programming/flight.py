class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

class Flight:
    def __init__(self,flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.list_passengers = []

    def add_passenger(self, passenger):
        if self.capacity > 0:
            self.list_passengers.append(passenger)
            self.capacity -= 1
            return True
        else:
            return False
    
    def remove_passenger(self,passport_number):
        for i in self.list_passengers:
            if i.passport_number == passport_number:
                self.list_passengers.remove(i)
                self.capacity += 1


    def available_seats(self):
        return self.capacity
    
    def list_passengers(self):
        return self.list_passengers

p1 = Passenger("Alice", "A123")
p2 = Passenger("Bob", "B456")

f = Flight("SQ001", 1)

print(f.add_passenger(p1))   # True
print(f.add_passenger(p2))   # False (full)

print(f.available_seats())   # 0

f.remove_passenger("A123")
print(f.available_seats())   # 1
