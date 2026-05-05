class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat(self):
        print("Animal is eating")
    
class Bird(Animal):
    def __init__(self,name,age,wingSpan):
        super().__init__(name,age)
        self.wingSpan = wingSpan

    def eat(self):
        print("Bird is eating")

class Fish(Animal):
    def __init__(self,name,age,finCount):
        super().__init__(name,age)
        self.finCount = finCount
    
    def eat(self):
        print("Fish is eating")

if __name__ == "__main__":
    birb1 = Bird("Julian",16,36)
    fish1 = Fish("Rayed",888888,57)

    birb1.eat()
    fish1.eat()

