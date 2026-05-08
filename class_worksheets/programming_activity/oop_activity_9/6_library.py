class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "Book: '" + self.title + "' by " + self.author


class Library:
    def __init__(self, books):
        self.books = books   

    def __str__(self):
        book_titles = ", ".join([book.title for book in self.books])
        return "Library contains: [" + book_titles + "]"


book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")
book3 = Book("Fahrenheit 451", "Ray Bradbury")

library = Library([book1, book2, book3])
print("Before deletion:", library)


del library


print("\nLibrary deleted!")
print(book1)    
print(book2)
print(book3)