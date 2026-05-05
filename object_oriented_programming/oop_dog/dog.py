class Dog:

    def __init__(self, Name, Breed):
        # private instance variables
        self.__Name = Name
        self.__Breed = Breed

    # getters
    def getName(self):
        return self.__Name

    def getAge(self):
        return self.__Breed

    # string method (like toString in Java)
    def __str__(self):
        return (
            f"Name: {self.__Name}, "
            f"Breed: {self.__Breed}"
        )