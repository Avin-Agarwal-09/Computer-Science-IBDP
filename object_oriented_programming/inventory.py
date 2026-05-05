class Product:
    def __init__(self,name,price,quantity):
        self.name =  name
        self.price = price
        self.quantity = quantity
    
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)
    
    def search_by_name(self,name):
        for i in self.products:
            if i.name == name:
                return i
            else:
                return None
            
    def sort_by_price(self):
        self.products.sort(key=lambda p: p.price)
    
    def total_inventory_value(self):
        total = 0
        for i in self.products:
            total += i.price * i.quantity
        return total
    
p1 = Product("Pen", 2, 100)
p2 = Product("Book", 5, 50)

inv = Inventory()
inv.add_product(p1)
inv.add_product(p2)

print(inv.search_by_name("Pen").price)  # 2

inv.sort_by_price()
print([p.name for p in inv.products])   # ['Pen','Book']

print(inv.total_inventory_value())      # 2*100 + 5*50 = 450