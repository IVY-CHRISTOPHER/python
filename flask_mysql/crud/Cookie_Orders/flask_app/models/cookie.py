from flask_app.models import user

class Cookie():
    def __init__(self,data):
        self.id = data['id']
        self.cname = data['cookie_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CRUD

# CREATE
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO cookies (cookie_name) VALUES %(cname)s;'
        return connectToMySQL('Cookies').query_db(query,data)

# READ

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM cookies;'
        cookies_from_db = connectToMySQL('Cookies').query_db(query)
        cookies = []
        for c in cookies_from_db:
            cookies.append(cls(c))
        return cookies

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM cookies WHERE id = %(id)s;'
        cookies_from_db = connectToMySQL('Cookies').query_db(query,data)
        return cls(cookies_from_db[0])

# UPDATE

    @classmethod
    def update(cls,data):
        query = 'UPDATE cookies SET cookie_name=%(cname)s, updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('Cookies').query_db(query,data)

# DELETE

    @classmethod
    def destroy(cls,data):
        query = 'DELETE FROM cookies WHERE id = %(id)s;'
        return connectToMySQL('Cookies').query_db(query,data)

    @staticmethod
    def validate_cookie(cookie):
        is_valid = True
        if len(cookie['cname']) < 2:
            flash('Cookie name must be at least 2 characters.')
            is_valid = False
        return is_valid
