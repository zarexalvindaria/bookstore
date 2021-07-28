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
from tkinter import StringVar, LEFT


root = tk.Tk()
root.title("Book Store")
# root.geometry("400x200")
root.iconbitmap("book.ico")
root.resizable(0,0)

# Define colors and fonts
black = "#280607"
light_red = "#dc1214"
dark_red = "#a80a0d"
gray = "#4b4b4b"



# Define function


# GUI Layout
# Define frames
entry_frame = tk.LabelFrame(root)
list_frame = tk.LabelFrame(root)
# button_frame = tk.LabelFrame(root)
entry_frame.pack(padx=2)
list_frame.pack()
# button_frame.pack(padx=2)


# First row
title_label = tk.Label(entry_frame, text="Title", justify=LEFT)
title_label.grid(row=0, column=0)
author_label = tk.Label(entry_frame, text="Author", justify=LEFT)
author_label.grid(row=0, column=2)
title_text = StringVar()
title_entry = tk.Entry(entry_frame, textvariable=title_text)
title_entry.grid(row=0, column=1)
author_text = StringVar()
author_entry = tk.Entry(entry_frame, textvariable=author_text)
author_entry.grid(row=0, column=3)
# Second row
year_label = tk.Label(entry_frame, text="Year", justify=LEFT)
year_label.grid(row=1, column=0)
isbn_label = tk.Label(entry_frame, text="ISBN", justify=LEFT)
isbn_label.grid(row=1, column=2)
year_text = StringVar()
year_entry = tk.Entry(entry_frame, textvariable=year_text)
year_entry.grid(row=1, column=1)
isbn_text = StringVar()
isbn_entry = tk.Entry(entry_frame, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

book_list = tk.Listbox(list_frame, height=6, width=35)
book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.grid(row=2, column=2, rowspan=6)

book_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=book_list.yview)

# Define buttons
view_button = tk.Button(list_frame, text="View all", width=12)
view_button.grid(row=2, column=3)
search_button = tk.Button(list_frame, text="Search entry", width=12)
search_button.grid(row=3, column=3)
add_button = tk.Button(list_frame, text="Add entry", width=12)
add_button.grid(row=4, column=3)
update_button = tk.Button(list_frame, text="Update", width=12)
update_button.grid(row=5, column=3)
delete_button = tk.Button(list_frame, text="Delete", width=12)
delete_button.grid(row=6, column=3)
close_button = tk.Button(list_frame, text="Close", width=12)
close_button.grid(row=7, column=3)

root.mainloop()