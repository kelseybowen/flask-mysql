from flask_app.config.mysqlconnection import connectToMySQL

class Item:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.weight = data['weight']
        self.created_at = data['created_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM items;"
        results = connectToMySQL('items_schema').query_db(query)
        items = []
        for i in results:
            items.append(cls(i))
        return items
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO items (name,weight) VALUES (%(name)s, %(weight)s);"
        result = connectToMySQL('items_schema').query_db(query,data)
        return result