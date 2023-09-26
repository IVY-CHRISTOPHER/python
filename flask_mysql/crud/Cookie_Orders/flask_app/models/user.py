from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User(self,data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

# CRUD
# CREATE
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users (name) VALUES (%(name)s);'
        return connectToMySQL('Cookies').query_db(query,data)
# READ
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        users_from_db = connectToMySQL('Cookies').query_db(query)
        users = []
        for u in users_from_db:
            users.append(cls(u))
        return users

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        users_from_db = connectToMySQL('Cookies').query_db(query,data)
        return cls(users_from_db[0])
# UPDATE
    @classmethod
    def update(cls,data):
        query = 'UPDATE users SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;'
        return connectToMySQL('Cookies').query_db(query,data)
# DELETE
    @classmethod
    def destroy(cls,data):
        query = ' DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL('Cookies').query_db(query,data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name']) < 2:
            flash('Name Must be at least 2 characters.')
            is_valid = False
        return is_valid

