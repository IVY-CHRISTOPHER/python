from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Message:
    def __init___(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CRUD

# CREATE
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO posts (content,user_id) VALUES (%(content)s,%(user_id)s);'
        return connectToMySQL('coding_wall').query_db(query,data)
# READ
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM posts;'
        posts_from_db = connectToMySQL('coding_wall').query_db(query)
        posts=[]
        for i in posts_from_db:
            posts.append(cls(i))
        return posts

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM posts WHERE id = %(id)s;'
        posts_from_db = connectToMySQL('coding_wall').query_db(query,data)
        return connectToMySQL('coding_wall').query_db(query,data)

# UPDATED

    @classmethod
    def update(cls,data):
        query = 'UPDATE posts SET content=%(content)s, updated_at=NOW();'
        return connectToMySQL('coding_wall').query_db(query,data)

# DELETE

    @classmethod
    def destroy(cls,data):
        query = 'DELETE FROM posts WHERE id = %(id)s;'
        return connectToMySQL('coding_wall').query_db(query,data)

# VALIDATE MESSAGE
    @staticmethod
    def validate_message(post):
        is_valid = True
        if len(post['content']) == 0:
            flash('Content cannot be blank!', 'message')
            is_valid = False
        return is_valid
