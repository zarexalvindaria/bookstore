"""Backend of the Book Store"""
import sqlite3

class Database:
    # Define the backend functions
    def __init__():
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
        cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
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
