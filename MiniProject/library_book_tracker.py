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
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            Book.checked_out_count += 1
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            Book.checked_out_count -= 1
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

    def display_info(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}\n Author: {self.author}\n Status: {status}")

    @classmethod
    def get_checked_out_count(cls):
        print(f"Total books checked out: {cls.checked_out_count}")
