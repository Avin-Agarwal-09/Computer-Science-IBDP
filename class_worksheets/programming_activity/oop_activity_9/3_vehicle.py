class Vehicle:
    def __init__(self):
        self.speed = 0

    def speedUp(self):
        print("Speeding up...")

class Car(Vehicle):
    def speedUp(self):
        self.speed += 20
        print(f"Car speed: {self.speed}")

class Bicycle(Vehicle):
    def speedUp(self):
        self.speed += 5
        print(f"Bicycle speed: {self.speed}")


car = Car()
bicycle = Bicycle()

car.speedUp()
bicycle.speedUp()