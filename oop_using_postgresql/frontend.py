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
from tkinter import StringVar, END, messagebox, DISABLED
from backend import Database

database = Database("bookstore.db")

root = tk.Tk()
root.title("Book Store")
root.iconbitmap("book.ico")
root.geometry("360x250")
root.resizable(0, 0)

# Define colors and fonts
black = "#280607"
light_red = "#dc1214"
dark_red = "#a80a0d"
button_color = "#e5e5e5"
label_font = ("Inter", 11)
button_font = ("Inter", 9)


# Define functions
def get_selected_row(event):
    """Get the id of the selected row"""
    global selected_tuple
    index = book_list.curselection()[0]
    selected_tuple = book_list.get(index)
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    isbn_entry.delete(0, END)

    # Check the selected row's first value in the tuple to insert the correct value to the entry field
    if isinstance(selected_tuple[0], int):
        title_entry.insert(END, selected_tuple[1])
        author_entry.insert(END, selected_tuple[2])
        year_entry.insert(END, selected_tuple[3])
        isbn_entry.insert(END, selected_tuple[4])
    else:
        title_entry.insert(END, selected_tuple[0])
        author_entry.insert(END, selected_tuple[1])
        year_entry.insert(END, selected_tuple[2])
        isbn_entry.insert(END, selected_tuple[3])


def view_command():
    """Lists all the data in the database"""
    book_list.delete(0, END)
    for row in database.view():
        book_list.insert(END, row)


def search_command():
    """Searches the database for a specific input"""
    book_list.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        book_list.insert(END, row)


def add_command():
    """Adds book"""
    if title_text.get() == "" and author_text.get() == "" and year_text.get() == "" and isbn_text.get() == "":
        warning = messagebox.showinfo("Empty inputs", "Your inputs are empty!")
        return warning
    else:
        database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        book_list.delete(0, END)
        book_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
        clear_input()
        get_selected_row(DISABLED)


def update_command():
    """Updates d specific row in the database"""
    database.update(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    update_listview()


def delete_command():
    """Deletes a specific row from the database"""
    database.delete(selected_tuple[0])
    update_listview()


def clear_input():
    """Clears the input boxes"""
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    isbn_entry.delete(0, END)


def update_listview():
    """Refreshes the listview"""
    book_list.delete(0, END)
    for row in database.view():
        book_list.insert(END, row)


# GUI Layout
# Define frames
entry_frame = tk.Frame(root)
list_frame = tk.Frame(root)
entry_frame.pack(padx=1, pady=5)
list_frame.pack(pady=(10, 0), ipady=5)

# Define entry frame
# Label First row
# Title
title_label = tk.Label(entry_frame, text="Title", padx=5, font=button_font)
title_label.grid(row=0, column=0)
title_text = StringVar()
title_entry = tk.Entry(entry_frame, textvariable=title_text)
title_entry.grid(row=0, column=1)
# Author
author_label = tk.Label(entry_frame, text="Author", padx=5, font=button_font)
author_label.grid(row=0, column=2)
author_text = StringVar()
author_entry = tk.Entry(entry_frame, textvariable=author_text)
author_entry.grid(row=0, column=3)
# Second row
# Year
year_label = tk.Label(entry_frame, text="Year", padx=5, font=button_font)
year_label.grid(row=1, column=0)
year_text = StringVar()
year_entry = tk.Entry(entry_frame, textvariable=year_text)
year_entry.grid(row=1, column=1)
# ISBN
isbn_label = tk.Label(entry_frame, text="ISBN", padx=5, font=button_font)
isbn_label.grid(row=1, column=2)
isbn_text = StringVar()
isbn_entry = tk.Entry(entry_frame, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

# List frame layout
# Define Listbox
book_list = tk.Listbox(list_frame, height=11, width=35)
book_list.grid(row=0, column=0, rowspan=11, columnspan=2)
# Scrollbar
scrollbar = tk.Scrollbar(list_frame)
scrollbar.grid(row=0, column=2, rowspan=11, padx=(0, 5), sticky="NS")
# Connect the list box and scrollbar
book_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=book_list.yview)

"""Define the binding of the Listbox and the selected row which will be used when deleting and updating"""
book_list.bind("<<ListboxSelect>>", get_selected_row)

# Define the buttons
clear_input_button = tk.Button(list_frame, text="Clear input", width=14, command=clear_input, bg=button_color,
                               font=button_font)
clear_input_button.grid(row=0, column=3)
view_button = tk.Button(list_frame, text="View all", width=14, command=view_command, bg=button_color, font=button_font)
view_button.grid(row=1, column=3)
search_button = tk.Button(list_frame, text="Search entry", width=14, command=search_command, bg=button_color,
                          font=button_font)
search_button.grid(row=2, column=3)
add_button = tk.Button(list_frame, text="Add entry", width=14, command=add_command, bg=button_color, font=button_font)
add_button.grid(row=3, column=3)
update_button = tk.Button(list_frame, text="Update selected", width=14, command=update_command, bg=button_color,
                          font=button_font)
update_button.grid(row=4, column=3)
delete_button = tk.Button(list_frame, text="Delete selected", width=14, command=delete_command, bg=button_color,
                          font=button_font)
delete_button.grid(row=5, column=3)
close_button = tk.Button(list_frame, text="Close", width=14, command=root.destroy, bg=button_color, font=button_font)
close_button.grid(row=6, column=3)

# Run the main window
root.mainloop()
