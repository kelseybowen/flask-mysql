from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, request, redirect

@app.route('/add_new_ninja')
def add_new_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", all_dojos=all_dojos)

@app.route('/create_new_ninja', methods=['POST'])
def create_new_ninja():
    data = {
        "dojo_id": request.form["dojo_name_select"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    Ninja.create_ninja(data)
    return redirect(f'/dojos/{data["dojo_id"]}')

@app.route('/edit_ninja/<int:id>') 
def edit_ninja(id):
    ninja = Ninja.show_ninja(id)
    all_dojos = Dojo.get_all_dojos()
    return render_template("edit_ninja.html", ninja=ninja, all_dojos=all_dojos)

@app.route('/update_ninja/<int:id>', methods=['POST'])
def update_ninja(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_name_select"]
    }
    Ninja.update_ninja(data)
    id = Dojo.get_dojo_id(request.form["dojo_name_select"])
    return redirect(f"/dojos/{data['dojo_id']}")

@app.route('/delete_ninja/<int:id>', methods=['POST'])
def delete_ninja(id):
    dojo_id = request.form["ninja_dojo_id"]
    Ninja.delete_ninja(id)
    return redirect(f"/dojos/{dojo_id}")

