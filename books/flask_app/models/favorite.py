from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book, author

class Favorite:
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']
    
    @classmethod
    def add_favorite(cls,author_id,book_id):
        data = {
            "author_id": author_id,
            "book_id": book_id
        }
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        result = connectToMySQL('books_schema').query_db(query, data)
        return result
    