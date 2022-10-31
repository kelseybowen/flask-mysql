from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite
from flask_app import app
from flask import render_template, request, redirect
from pprint import pprint

@app.route('/books')
def books():
    books = Book.get_all_books()
    return render_template("books.html", books=books)

@app.route('/books/<int:book_id>')
def book_favorites(book_id):
    book_favorites = Book.get_one_book(book_id)
    all_authors=Author.get_all_authors()
    return render_template("book_favorites.html", book_favorites=book_favorites, book_title=book_favorites[0]['title'], all_authors=all_authors)

@app.route('/add_book', methods=["POST"])
def add_book():
    data = {
        "title": request.form["add_book_title"],
        "num_of_pages": request.form["add_book_pages"]
    }
    Book.add_new_book(data)
    return redirect('/books')
    