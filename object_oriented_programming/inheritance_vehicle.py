class Vehicle:
    def __init__(self, fuel_type, capacity):
        self.__fuel_type = fuel_type
        self.__capacity = capacity
    
    def get_fuel_type(self):
        return self.__fuel_type
    
    def get_capacity(self):
        return self.__capacity
    
    def set_fuel_type(self, new_fuel):
        self.__fuel_type = new_fuel
    
    def set_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__capacity = new_capacity
        else:
            print("Error: capacity must be positive")

    def display_info(self):
        print("Vehicle details: ")
        print("- fuel type:", self.__fuel_type)
        print("- capacity:", self.__capacity, "passengers")


class Car(Vehicle):
    def __init__(self, fuel_type, capacity, is_electric):
        super().__init__(fuel_type, capacity)
        self._is_electric = is_electric

    def display_info(self):
        super().display_info()
        print("- Electric:", self._is_electric)


my_car = Car("Petrol", 5, False)
my_car.display_info()

my_car.set_capacity(7)
print("Updated Capacity:", my_car.get_capacity())