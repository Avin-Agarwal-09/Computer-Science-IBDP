class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)



lib = Library()

lib.add_book("Harry Potter")
lib.add_book("1984")
lib.remove_book("1984")

print("Books in library:", lib.books)
