from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.book_name = data['title']
        self.num_of_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []

# CRUD
# CREATE
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO books (title) VALUES (%(title)s);'
        return connectToMySQL('Books_Erd').query_db(query,data)

# READ
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books'
        books_from_db = connectToMySQL('Books_Erd').query_db(query)
        books = []
        for i in books_from_db:
            books.append(cls(i))
        return books

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM books WHERE books.id = %(id)s;'
        books_from_db = connectToMySQL('Books_Erd').query_db(query,data)
        return connectToMySQL('Books_Erd').query_db(query,data)

# UPDATE
    @classmethod
    def update(cls,data):
        query = 'UPDATE books SET title=%(title)s updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('Books_Erd').query_db(query,data)
# DELETE

    @classmethod
    def destroy(cls,data):
        query = 'DELETE FROM books WHERE id = %(id)s'
        return connectToMySQL('Books_Erd').query_db(query,data)
