"""Backend of the Bookstore"""
import sqlite3


# Define the backend functions
def connect():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()


def insert(title, author, year, isbn):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    connection.close()
    return rows


def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=? AND (title IS NOT NULL AND author IS NOT NULL AND year IS NOT NULL AND isbn IS NOT NULL)", (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    connection.commit()
    connection.close()


def update(id, title, author, year, isbn):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()


connect()
# insert("Mathematics","John Doe",1993,12345)
# insert("Science","John Doe",1993,12345)
# insert("English","John Doe",1993,12345)
# print(search("","",1993))
# delete(1)
# print(view())
# update(3, "English", "John Smith", 1990, 646646)
# print(view())
