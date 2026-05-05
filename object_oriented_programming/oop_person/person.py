class Person:

    def __init__(self, Name, Age):
        # private instance variables
        self.__Name = Name
        self.__Age = Age

    # getters
    def getName(self):
        return self.__Name

    def getAge(self):
        return self.__Age

    # string method (like toString in Java)
    def __str__(self):
        return (
            f"Name: {self.__Name}, "
            f"Age: {self.__Age}"
        )