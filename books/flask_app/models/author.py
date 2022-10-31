from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book, favorite
# from flask_app.models 

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(author)
        return authors
    
    @classmethod
    def get_one_author(cls, author_id):
        data = {
            "author_id": author_id
        }
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(author_id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results
    
    @classmethod
    def create_new_author(cls,name):
        data = {
            "name": name
        }
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL('books_schema').query_db(query, data)
        return result
