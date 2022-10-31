from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, created_at, dojo_id ) VALUES ( %(first_name)s , %(last_name)s , %(age)s, NOW(), %(dojo_id)s );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def show_ninja(cls,id):
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.id = %(id)s;"
        data = {
            "id": id
        }
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update_ninja(cls,data):
        query = "UPDATE ninjas SET first_name = (%(first_name)s), last_name = (%(last_name)s), age = (%(age)s), updated_at = NOW() WHERE id = (%(id)s);"
        data = {
            "id": data['id'],
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "age": data['age'],
        }
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data) 
    
    @classmethod
    def delete_ninja(cls, id):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {
            "id": id
        }
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
