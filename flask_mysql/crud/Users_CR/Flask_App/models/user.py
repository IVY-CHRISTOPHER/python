from Flask_App.Config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

bcrypt.generate_password_hash('My Special Password')
print(bcrypt)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    # DB = 'user_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CRUD METHODS
# CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT into users (first_name, last_name, email)
                VALUES (%(fname)s , %(lname)s , %(email)s);"""
        results = connectToMySQL('user_schema').query_db(query, data)
        return results

    # READ
    @classmethod
    def get_one_user(cls, id):
        query = """SELECT * FROM users
            WHERE ID = %(id)s;"""
        results = connectToMySQL('user_schema').query_db(query, {'id': id})
        return cls(results[0])

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)

        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users
    # UPDATE
    # DELETE

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['fname']) < 3:
            flash('First Name must be at least 3 characters.')
            is_valid = False
        if len(user['lname']) < 3:
            flash('Last Name must be at least 3 characters.')
            is_valid = False
        if len(user['email']) < 3:
            flash('Email must be at least 3 characters.')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('invalid Email Address!')
            is_valid = False
        return is_valid