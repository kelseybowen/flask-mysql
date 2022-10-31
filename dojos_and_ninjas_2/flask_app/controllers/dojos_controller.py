from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, request, redirect
from pprint import pprint

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos=all_dojos)

@app.route('/add_new_dojo', methods=["POST"]) 
def add_new_dojo():
    data = {
        "name": request.form["new_dojo_name"]
    }
    Dojo.add_new_dojo(data)
    return redirect('/')

@app.route('/dojos/<int:id>')
def dojo_show(id):
    dojo_info = Dojo.show_dojo(id)
    dojo_name = Dojo.get_single_dojo(id)
    print(f"   DOJO INFO = {dojo_info}")
    return render_template("dojo_show.html", dojo_name=dojo_name.name, dojo_info=dojo_info)

