"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

import tkinter as tk
from tkinter import StringVar, END
import backend

root = tk.Tk()
root.title("Book Store")
root.iconbitmap("book.ico")
root.geometry("350x230")
root.resizable(0,0)

# Define colors and fonts
black = "#280607"
light_red = "#dc1214"
dark_red = "#a80a0d"
gray = "#4b4b4b"


# Define functions

def get_selected_row(event):
    """Get the id of the selected row"""
    global selected_tuple
    index = book_list.curselection()[0]
    selected_tuple = book_list.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[4])


def view_command():
    book_list.delete(0, END)
    for row in backend.view():
        book_list.insert(END, row)


def search_command():
    book_list.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        book_list.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    clear_list()
    book_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    # clear_input()


def delete_command():
    backend.delete(selected_tuple[0])
    update_listview()


def clear_list():
    book_list.delete(0, END)


def clear_input():
    title_text.set("")
    author_text.set("")
    year_text.set("")
    isbn_text.set("")


def update_listview():
    book_list.delete(0, END)
    for row in backend.view():
        book_list.insert(END, row)


# GUI Layout
# Define frames
entry_frame = tk.LabelFrame(root)
list_frame = tk.LabelFrame(root)
entry_frame.pack(padx=1, pady=5)
list_frame.pack(ipady=5)

# Define entry frame
# First row
title_label = tk.Label(entry_frame, text="Title", padx=5)
title_label.grid(row=0, column=0)
author_label = tk.Label(entry_frame, text="Author", padx=5)
author_label.grid(row=0, column=2)
title_text = StringVar()
title_entry = tk.Entry(entry_frame, textvariable=title_text)
title_entry.grid(row=0, column=1)
author_text = StringVar()
author_entry = tk.Entry(entry_frame, textvariable=author_text)
author_entry.grid(row=0, column=3)
# Second row
year_label = tk.Label(entry_frame, text="Year", padx=5)
year_label.grid(row=1, column=0)
isbn_label = tk.Label(entry_frame, text="ISBN", padx=5)
isbn_label.grid(row=1, column=2)
year_text = StringVar()
year_entry = tk.Entry(entry_frame, textvariable=year_text)
year_entry.grid(row=1, column=1)
isbn_text = StringVar()
isbn_entry = tk.Entry(entry_frame, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

# Define display
book_list = tk.Listbox(list_frame, height=8, width=35)
book_list.grid(row=2, column=0, rowspan=8, columnspan=2, padx=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.grid(row=2, column=2, rowspan=6, sticky="NS")

book_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=book_list.yview)

# Define the binding of the Listbox and the
book_list.bind("<<ListboxSelect>>", get_selected_row)

# Define buttons
view_button = tk.Button(list_frame, text="View all", width=12, command=view_command)
view_button.grid(row=2, column=3)
search_button = tk.Button(list_frame, text="Search entry", width=12, command=search_command)
search_button.grid(row=3, column=3)
add_button = tk.Button(list_frame, text="Add entry", width=12, command=add_command)
add_button.grid(row=4, column=3)
update_button = tk.Button(list_frame, text="Update", width=12, command=backend.update)
update_button.grid(row=5, column=3)
delete_button = tk.Button(list_frame, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)
close_button = tk.Button(list_frame, text="Close", width=12, command=root.destroy)
close_button.grid(row=7, column=3)

root.mainloop()
