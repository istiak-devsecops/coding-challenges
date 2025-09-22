# OOP 
# Create a Book Class
# - Attributes: title, author, year
# - Method: get_summary() returns a formatted string like "Title by Author (Year)"

class book:
    def __init__(self, title, author, year):   # constructor
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):          # method
        return f"{self.title} is written by {self.author} in {self.year}"
    
book1 = book("suvro","humayun ahmed", 2005)
print(book1)
        