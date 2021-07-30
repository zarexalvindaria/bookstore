"""Backend of the Book Store"""
import psycopg2
from psycopg2.sql import NULL

class Database:
    # Define the backend functions
    def __init__(self, db):
        self.connection = psycopg2.connect(
            "dbname='bookstore' user='postgres' password='postgres123' host='localhost' port='5432'")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY, title VARCHAR, author VARCHAR, year INTEGER, isbn INTEGER)")
        self.connection.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES (DEFAULT, %s,%s,%s,%s);", (title, author, year, isbn))
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title, author, year, isbn):
        self.cursor.execute("SELECT * FROM books WHERE title=%s OR author=%s OR year=%s OR isbn=%s",
                            (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=%s", [id])
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE books SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",
                            (title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
