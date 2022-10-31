from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, request, redirect

@app.route('/add_new_ninja')
def add_new_ninja():
    print(f"  # Trying to add new ninja")
    all_dojos = Dojo.get_all_dojos()
    print(f"    add_new_ninja - all_dojos = {all_dojos}")
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