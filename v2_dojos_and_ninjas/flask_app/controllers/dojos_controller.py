from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, request, redirect

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos=all_dojos)

@app.route(f'/dojos/<int:id>')
def show_one_dojo(id):
    dojo = Dojo.get_one_dojo(id)
    print(f"       SHOW ONE DOJO = {dojo}")
    ninjas_at_dojo = Dojo.get_dojo_info(id)
    print(f"       NINJAS AT DOJO = {ninjas_at_dojo}")
    return render_template("dojo_show.html", dojo=dojo, ninjas_at_dojo=ninjas_at_dojo)

