from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def add_new_dojo(cls, name):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW());"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,name)
        return result
    
    @classmethod
    def get_single_dojo(cls,id):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        data = {
            "id": id
        }
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_dojo_id(cls,name):
        query = "SELECT id FROM dojos WHERE name=%(name)s;"
        data = {
            "name": name
        }
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def show_dojo(cls,id):
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        data = {
            "id": id
        }
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        ninjas_at_dojo = []
        for i in results:
            ninjas_at_dojo.append(i)
            
        return ninjas_at_dojo
