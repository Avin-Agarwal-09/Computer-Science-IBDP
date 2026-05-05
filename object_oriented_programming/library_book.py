class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)

    def borrow_book(self,title):
        for i in range(len(self.books)):
            random = self.books[i]
            if random.title == title:
                if random.is_borrowed == False:
                    random.is_borrowed = True
                    return True
                else:
                    return False
            

    def return_book(self, title):
        for i in range(len(self.books)):
            random = self.books[i]
            if random.title == title:
                if random.is_borrowed == True:
                    self.books[i].is_borrowed = False
                    return True
                else:
                    return False

    def list_available_books(self):
        available = []
        for i in range(len(self.books)):
            random = self.books[i]
            if random.is_borrowed == False:
                available.append(random.title)
            else:
                continue
        return available


b1 = Book("1984", "Orwell")
b2 = Book("Dune", "Herbert")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.borrow_book("1984")
print(lib.list_available_books())  # ["Dune"]

lib.return_book("1984")
print(lib.list_available_books())  # ["1984", "Dune"