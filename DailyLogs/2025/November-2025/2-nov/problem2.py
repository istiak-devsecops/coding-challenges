# simple system to manage books in a library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"{self.title} written by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def show_books(self):
        for book in self.books:
            print(f"{book.info()}")


book1 = Book("amar ache jol", "humayun ahmed")
book2 = Book("House of the dragon", "Don't know")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.show_books()

        