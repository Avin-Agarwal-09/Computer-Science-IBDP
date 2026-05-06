class Person:
    def __init__(self, name, gender, height):
        self.name = name
        self.gender = gender
        self.height = height


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def display(self):
        print(f"Name    : {self.person.name}")
        print(f"Gender  : {self.person.gender}")
        print(f"Height  : {self.person.height}")
        print(f"Street  : {self.street}")
        print(f"City    : {self.city}")
        print(f"Country : {self.country}")



p = Person("Rayed", "Female", 125)

a = Address("Aljunied", "Paya Lebar", "Singapore")
a.person = p

a.display()