from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

# CRUD
# CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (dojo_name) VALUES (%(dojo_name)s);"
        return connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
# READ

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for x in dojos_from_db:
            dojos.append(cls(x))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos WHERE dojos.id = %(id)s;'
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# UPDATE

    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET dojo_name=%(dojo_name)s updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# DELETE

    @classmethod
    def destroy(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    # CRUD

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_at' : row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        print("dojo ---->" , dojo)
        return dojo
