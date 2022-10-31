from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite
from flask_app import app
from flask import render_template, request, redirect

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all_authors()
    return render_template("authors.html", authors=authors)

@app.route('/create_new_author', methods=["POST"])
def save_author():
    data = request.form["new_author"]
    Author.create_new_author(data)
    return redirect('/authors')

@app.route('/authors/<int:author_id>')
def author_favorites(author_id):
    author_favorites = Author.get_one_author(author_id)
    return render_template("author_favorites.html", author_favorites=author_favorites, author_name=author_favorites[0]['name'], all_books=Book.get_all_books())
