from flask_app import app
from flask import render_template,session,redirect,Flask,request
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

loginroute = '/login/page'
loginpage = 'login.html'

@app.route('/')
def reroute_login():
    return redirect(loginroute)

@app.route('/login', methods=['POST'])
def login():
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/main')

@app.route('/login/page')
def login_form():
    return render_template('login.html')

@app.route('/create/user', methods=['POST'])
def create_user():
    # Checking form validation
    if not User.validate_user(request.form):
        return redirect('/')
    # Creating hashed password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data  = {
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'email':request.form['email'],
        'password': pw_hash
    }
# Saving user information by (data) instead of (request.form)
# Storing this in 'user_id'
    user_id = User.save(data)
# Setting user_id to = session['user_id']
    session['user_id'] = user_id
    return redirect('/main')


@app.route('/clear')
def clearsessions():
    session.clear()
    return redirect('/')

@app.route('/main')
def mainpage():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('main.html')