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
from tkinter import StringVar


root = tk.Tk()
root.title("Book Store")
root.geometry("400x200")
root.iconbitmap("book.ico")
root.resizable(0,0)

# Define colors and fonts




# Define function


title_label = tk.Label(root, text="Title")
title_label.grid(row=0, column=0)

author_label = tk.Label(root, text="Author")
author_label.grid(row=0, column=2)

year_label = tk.Label(root, text="Year")
year_label.grid(row=1, column=0)

isbn_label = tk.Label(root, text="ISBN")
isbn_label.grid(row=1, column=2)

title_text = StringVar()
title_entry = tk.Entry(root, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = tk.Entry(root, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = tk.Entry(root, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = tk.Entry(root, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

root.mainloop()