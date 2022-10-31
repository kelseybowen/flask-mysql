from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author, favorite

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(book)
        return books
    
    @classmethod
    def get_one_book(cls, book_id):
        data = {
            "book_id": book_id
        }
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(book_id)s;"
        result = connectToMySQL('books_schema').query_db(query, data)
        return result
    
    @classmethod
    def add_new_book(cls, data):
        data = {
            "title": data['title'],
            "num_of_pages": data['num_of_pages']
        }
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        result = connectToMySQL('books_schema').query_db(query, data)
        return result