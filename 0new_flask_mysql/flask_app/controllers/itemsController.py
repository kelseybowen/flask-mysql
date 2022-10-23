from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.items import Item


@app.route('/')
def index():
    return render_template("items.html", items=Item.get_all())

@app.route('/new/item')
def newItemForm():
    return render_template("newItem.html")

@app.route('/create/item', methods=['POST'])
def addItem():
    Item.save(request.form)
    return redirect('/')