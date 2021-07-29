"""Backend of the Book Store"""
import sqlite3


class Database:
    # Define the backend functions
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.connection.commit()

    def insert(self,title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def delete(self,id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()