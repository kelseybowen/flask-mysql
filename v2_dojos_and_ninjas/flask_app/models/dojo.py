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
    def get_one_dojo(cls, id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {
            "id": id
        }
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result
    
    @classmethod
    def get_dojo_info(cls, id):
        query = "SELECT * FROM ninjas WHERE dojo_id=%(id)s;"
        data = {
            "id": id
        }
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results
    
