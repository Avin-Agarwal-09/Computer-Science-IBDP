"""Topic 11 - OOP: classes and objects.

class      - the blueprint         object - one instance built from it
attribute  - data an object holds  method - behaviour it provides

Key ideas shown here:
  __init__          the constructor, runs when an object is created
  instance vs class attributes (self.name vs Product.count)
  encapsulation     a leading _ marks an attribute as internal
  @property         read an internal value like an attribute, no setter
  __str__           how the object prints
  composition       Inventory HAS-A list of Products
  static method     belongs to the class, needs no instance
"""


class Product:
    count = 0                    # class attribute - shared by ALL products

    def __init__(self, name, price, quantity):
        self.name = name         # instance attributes - one per object
        self._price = price      # encapsulated: change it through set_price
        self.quantity = quantity
        Product.count += 1

    @property
    def price(self):
        """Read-only access to the encapsulated price."""
        return self._price

    def set_price(self, new_price):
        """A setter can validate; direct attribute assignment cannot."""
        if new_price < 0:
            print("Price cannot be negative")
            return False
        self._price = new_price
        return True

    def total_value(self):
        return self._price * self.quantity

    def __str__(self):
        return f"{self.name} (${self._price} x {self.quantity})"

    @staticmethod
    def product_count():
        return Product.count


class Inventory:
    """Composition: an Inventory is built FROM Product objects."""

    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return True
        return False

    def search_by_name(self, name):
        """Return the match, or None. The return must be OUTSIDE the loop."""
        for product in self.products:
            if product.name == name:
                return product
        return None

    def sort_by_price(self):
        self.products.sort(key=lambda product: product.price)

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.total_value()
        return total

    def most_valuable(self):
        if not self.products:
            return None
        best = self.products[0]
        for product in self.products:
            if product.total_value() > best.total_value():
                best = product
        return best

    def __str__(self):
        return f"{self.shop_name}: {len(self.products)} product lines"


class Vector2D:
    """Operator overloading lets your class work with +, == and print()."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    pen = Product("Pen", 2, 100)
    book = Product("Book", 5, 50)
    bag = Product("Bag", 25, 4)

    inventory = Inventory("School Shop")
    for product in [pen, book, bag]:
        inventory.add_product(product)

    print(inventory)
    print("Search 'Pen':   ", inventory.search_by_name("Pen"))
    print("Search 'Ruler': ", inventory.search_by_name("Ruler"))

    inventory.sort_by_price()
    print("Sorted by price:", [product.name for product in inventory.products])

    print("Total value:    ", inventory.total_inventory_value())
    print("Most valuable:  ", inventory.most_valuable())

    print("\nEncapsulation:")
    print("  price now:    ", pen.price)
    pen.set_price(-5)
    pen.set_price(3)
    print("  price after:  ", pen.price)
    print("  products made:", Product.product_count())

    print("\nOperator overloading:")
    a = Vector2D(1, 2)
    b = Vector2D(3, 4)
    print("  a + b =", a + b)
    print("  a == b:", a == b)
    print("  a == Vector2D(1, 2):", a == Vector2D(1, 2))
