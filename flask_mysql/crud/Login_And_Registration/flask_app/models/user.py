from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
import re
bcrypt = Bcrypt(app)

bcrypt.generate_password_hash('hashwordpassword')
print(bcrypt)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CRUD
# CREATE
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        return connectToMySQL('login_registration').query_db(query,data)

# READ
    @classmethod
    def get_all(cls,data):
        query = 'SELECT * FROM users;'
        users_from_db = connectToMySQL('login_registration').query_db(query)
        users = []
        for u in users_from_db:
            users.append(cls(u))
        return users
    
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        users_from_db = connectToMySQL('login_registration').query_db(query,data)
        return connectToMySQL('login_registration').query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_registration").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

# UPDATE
    @classmethod
    def update(cls,data):
        query = 'UPDATE users SET username=%(username)s, password=%(password)s, Updated_at=NOW() WHERE id = %(id)s;'
        return connectToMySQL('login_registration').query_db(query,data)

# DELETE
    @classmethod
    def destroy(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL('login_registration').query_db(query,data)

# VALIDATION
    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_registration").query_db(query,user)
        if len(result) > 1:
            is_valid = False
            flash('Email is taken!', 'register')
        if len(user['fname']) < 2:
            flash('First name must be at least 2 characters long!','register')
            is_valid = False
        if not user['fname'].isalpha():
            flash('First name may not include numerical characters!','register')
            is_valid = False
        if len(user['lname']) < 2:
            flash('Last name must be at least 2 characters long!','register')
            is_valid = False
        if not user['lname'].isalpha():
            flash('Last name may not include numerical characters!','register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!', 'register')
            is_valid = False
        if len(user['email']) < 2:
            flash('Email must be longer then 2 characters', 'register')
        if len(user['password']) < 2:
            flash('Password must be longer then 2 characters','register')
            is_valid = False
        if user['password'] != user['cpassword']:
            flash('Passwords do not match', 'register')
            is_valid = False
        return is_valid

