from flask_app import app
from flask import render_template,redirect,request,session,Flask
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template('Dojo.html', all_dojos = all_dojos)

@app.route('/createdojo', methods = ['POST'])
def createdojo():
    data = {
        'dojo_name':request.form['name']
        }
    Dojo.save(data)
    return redirect('/')

@app.route('/ninja')
def ninjapage():
    all_dojos = Dojo.get_all()
    return render_template('Ninja.html', all_dojos = all_dojos)

@app.route('/createninja', methods = ['POST'])
def createninja():
    data = {
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/')

@app.route('/dojoshow/<int:id>')
def dojoshow(id):
    data = {
        'id': id
    }
    dojoninjas = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojoshow.html', dojoninjas = dojoninjas)