from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, request, redirect

@app.route('/add_new_ninja')
def add_new_ninja():
    data = {
        "first_name": request.form()
    }
    Ninja.create_ninja()
    return redirect('/dojo_show/<int:id>') # redirect to dojo show