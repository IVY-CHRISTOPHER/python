# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class Friend:
    DB = 'first_flask'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CRUD METHODS
    # CREATE
    @classmethod
    def save(cls,data):
        query = '''INSERT into friends (first_name, last_name, occupation, created_at, updated_at )
        VALUES (%(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );'''
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    # READ
    @classmethod
    def get_one(cls, id):
        query = '''SELECT * FROM friends
                WHERE id = %(id)s'''
        results = connectToMySQL(cls.DB).query_db(query, {'id': id})
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM friends;'
        results = connectToMySQL(cls.DB).query_db(query)

        all_friends = []
        for row in results:
            # make object
            all_friends.append(cls(row))
        return all_friends
    # UPDATE
    @classmethod
    def update(data):
        query = """ UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s , email = %(email)s 
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    # DELETE
    @classmethod
    def delete(id):
        query = """DELETE FROM friends WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,{'id': id})
        return results
