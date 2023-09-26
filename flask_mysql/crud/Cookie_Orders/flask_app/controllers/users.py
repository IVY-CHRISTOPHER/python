from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')                                                                      #Create a User Creation Page

@app.route('/user/create')
def create_user():
    if not User.validate_user(request.form):
        return redirect('/users')
    user.save(request.form)
    return redirect('/')
    data = {
        'name':request.form['name']
    }
    User.save(data)
    return redirect('/users')

@app.route