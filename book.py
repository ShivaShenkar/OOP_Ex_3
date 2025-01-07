import csv
class Book:
    def __init__(self, title, author,year,category,copies):
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.copies = copies
        self.loaned_copies = 0

    def loan_copy(self):
        if self.copies > 0:
            self.copies -= 1
            self.loaned_copies += 1


        else:
            print("No copies available")
    def return_copy(self):
        if self.loaned_copies > 0:
            self.copies += 1
            self.loaned_copies -= 1
        else:
            print("No copies to return")

