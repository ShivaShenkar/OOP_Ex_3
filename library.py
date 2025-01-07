import csv
import os


class Library:
    #singelton implementation for library class.
    _instance = None
    def __new__(cls , *args , **kwargs):
        if cls._instance is None:
            cls._instance = super(Library,cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self,'book_list'):
            self.book_list = []

    def add_book(self , book):
        self.book_list.append(book)

    def remove_book(self , book):
        self.book_list.remove(book)

    def update_book(self , book,new_book):
        index = self.book_list.index(book)
        index = new_book

    def loan_book(self , book):
        if book in self.book_list:
            book.loan_copy()
            update_csv(book)

    def update_csv(self , book,filepath=None):
        file_list = ['books.csv','available_books.csv','loaned_books.csv'] if filepath is None else [filepath]
        for file_name in file_list:
            with open(file_name,'a',newline='') as file:
                writer = csv.writer(file)
                for line in file.readlines():
                    writer.writerow([book.title,book.author,book.year,book.category,book.copies,book.loaned_copies])