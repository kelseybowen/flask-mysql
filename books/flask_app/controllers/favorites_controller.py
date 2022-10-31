from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite
from flask_app import app
from flask import render_template, request, redirect

@app.route('/add_favorite_book/<int:author_id>', methods=["POST"])
def add_favorite_book(author_id):
    data = {
        "book_id": request.form['add_favorite_book']
    }
    Favorite.add_favorite(author_id, data['book_id'])
    return redirect(f"/authors/{author_id}")

@app.route('/add_favorite_author/<int:book_id>', methods=["POST"])
def add_favorite_author(book_id):
    data = {
        "author_id": request.form['add_favorite_author']
    }
    Favorite.add_favorite(int(data['author_id']), book_id)
    return redirect(f"/books/{book_id}")