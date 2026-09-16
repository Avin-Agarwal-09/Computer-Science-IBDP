class CPU:
    def __init__(self):
        self.model = "Intel Core i9"
        self.cores = 8

    def get_info(self):
        return "CPU: " + self.model + " (" + str(self.cores) + " cores)"

class RAM:
    def __init__(self):
        self.size = 16
        self.type = "DDR5"

    def get_info(self):
        return "RAM: " + str(self.size) + "GB " + self.type


class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.cpu = CPU()
        self.ram = RAM()

    def get_specs(self):
        return ("Computer: " + self.brand + "\n"
                + "  -> " + self.cpu.get_info() + "\n"
                + "  -> " + self.ram.get_info())



my_computer = Computer("Lenevo Legion")
print(my_computer.get_specs())

print("\n--- Destroying the Computer ---")
del my_computer
print("Computer deleted → CPU and RAM are gone too (no external references exist)")