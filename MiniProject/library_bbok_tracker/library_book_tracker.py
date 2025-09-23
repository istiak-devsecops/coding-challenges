# Library Book Tracker
# - Create a Book class with attributes: title, author, is_checked_out
# - Methods: check_out(), return_book(), display_info()
# - Bonus: Track how many books are currently checked out

class Book:
    # Class-level attribute to track checked-out books
    checked_out_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False # Tracks whether the book is currently checked out


    def check_out(self):    # Check out the book only if it's not already checked out
        if not self.is_checked_out:
            self.is_checked_out = True
            Book.checked_out_count += 1
            print(f"{self.title} has been checked out.")
            self.log_to_file("Checked Out")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):  # Return the book only if it was previously checked out
        if self.is_checked_out:
            self.is_checked_out = False
            Book.checked_out_count -= 1
            print(f"{self.title} has been returned.")
            self.log_to_file("Returned")
        else:
            print(f"{self.title} was not checked out.")

    def display_info(self): # Show book details and current status
        status = "Checked Out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}\n Author: {self.author}\n Status: {status}")
        self.log_to_file("Displayed Info")
    
    def log_to_file(self, action, filename="library_log.txt"):
        with open(filename, "a") as file:
            file.write(f"Action: {action}\n")
            file.write(f"Title: {self.title}\n")
            file.write(f"Author: {self.author}\n")
            file.write(f"Status: {'Checked Out' if self.is_checked_out else 'Available'}\n")
            file.write("-" * 30 + "\n\n")


    @classmethod    # Class method to display total number of checked-out books
    def get_checked_out_count(cls):
        print(f"Total books checked out: {cls.checked_out_count}")


# User Interaction Loop
library = []

while True:
    print("\nLibrary Menu:")
    print("1. Add a new book")
    print("2. Check out a book")
    print("3. Return a book")
    print("4. Display book info")
    print("5. Show total checked-out count")
    print("6. Exit")

    choice = input("Choose an option (1–6): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        new_book = Book(title, author)
        library.append(new_book)
        print(f"Book '{title}' added to library.")

    elif choice == "2":
        title = input("Enter title of book to check out: ")
        found = False
        for book in library:
            if book.title.lower() == title.lower():
                book.check_out()
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "3":
        title = input("Enter title of book to return: ")
        found = False
        for book in library:
            if book.title.lower() == title.lower():
                book.return_book()
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "4":
        title = input("Enter title of book to display: ")
        found = False
        for book in library:
            if book.title.lower() == title.lower():
                book.display_info()
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "5":
        Book.get_checked_out_count()

    elif choice == "6":
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")
