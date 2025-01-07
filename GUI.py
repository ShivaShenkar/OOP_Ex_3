from tkinter import *

def f1():
    print("אני חרמן!!!!!!!!!!!!!")

def f2():
    print("תמצצי לי!!!!!!!!!!")

def f3():
    print("Mango")

def f4():
    print("Yesh li kaki")

window = Tk()
window.title("MANGO Library")
window.geometry('600x300')
window.configure(bg='light blue')
add_book_button = Button(window, text="Add Book", bg='light green', fg='black', font=('Arial', 16), command=f1)
remove_book_button = Button(window, text="Remove Book", bg='light green', fg='black', font=('Arial', 16) , command= f2)
search_book_button = Button(window, text="Search Book", bg='light green', fg='black', font=('Arial', 16) , command= f3)
view_books_button = Button(window, text="View Books", bg='light green', fg='black', font=('Arial', 16) , command= f4)
lend_book_button = Button(window, text="Lend Book", bg='light green', fg='black', font=('Arial', 16))
return_book_button = Button(window, text="Return Book", bg='light green', fg='black', font=('Arial', 16))
logout_button = Button(window, text="Logout", bg='light green', fg='black', font=('Arial', 16))
login_button = Button(window, text="Login", bg='light green', fg='black', font=('Arial', 16))
register_button = Button(window, text="Register", bg='light green', fg='black', font=('Arial', 16))
add_book_button.grid(row=0, column=0, padx=20, pady=20)
remove_book_button.grid(row=0, column=1, padx=20, pady=20)
search_book_button.grid(row=0, column=2, padx=20, pady=20)
view_books_button.grid(row=1, column=0, padx=20, pady=20)
lend_book_button.grid(row=1, column=1, padx=20, pady=20)
return_book_button.grid(row=1, column=2, padx=20, pady=20)
logout_button.grid(row=2, column=0, padx=20, pady=20)
login_button.grid(row=2, column=1, padx=20, pady=20)
register_button.grid(row=2, column=2, padx=20, pady=20)
window.mainloop()
