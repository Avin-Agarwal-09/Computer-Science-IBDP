class Vehicle:
    def __init__(self,brand,max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def describe(self):
        return f"{self.brand}, Max Speed: {self.max_speed}"

class ElectricCar(Vehicle):
    def __init__(self,brand,max_speed,battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(brand,max_speed)
        
    def describe(self):
        return f"{self.brand}, Max Speed: {self.max_speed}, Battery: {self.battery_capacity}"

        

class PetrolCar(Vehicle):
    def __init__(self,brand,max_speed,Fuel_capacity):
        self.Fuel_capacity = Fuel_capacity
        super().__init__(brand,max_speed)
        
    def describe(self):
        return f"{self.brand}, Max Speed: {self.max_speed}, Fuel: {self.Fuel_capacity}"
    
v1 = ElectricCar("Tesla", 250, 75)
v2 = PetrolCar("Toyota", 180, 50)

print(v1.describe()) # Tesla EV, Max Speed: 250, Battery: 75kWh
print(v2.describe()) # Toyota Petrol, Max Speed: 180, Fuel: 50L