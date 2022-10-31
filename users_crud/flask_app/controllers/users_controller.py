from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User
from flask_app.controllers import users_controller

@app.route('/')
def index():
    return redirect('/read')
    
@app.route('/read')
def read():
    users = User.get_all()
    return render_template("read.html", all_users = users)

@app.route('/new')
def new():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    id = User.save(data)
    return redirect(f'/show/{id}')

@app.route('/show/<id>')
def show(id):
    user_info = User.show_one_user(id)
    return render_template("show_user.html", user_info=user_info)

@app.route('/edit/<id>')
def edit(id):
    user_info = User.show_one_user(id)
    return render_template("edit_user.html", user_info=user_info)

@app.route('/update/<id>', methods=['POST'])
def update(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update_user(data)
    return redirect('/')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    User.delete_user(id)
    return redirect('/read')
            
