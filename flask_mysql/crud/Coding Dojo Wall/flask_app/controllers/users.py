from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.post import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# REDIRECTS TO THE LOGIN PAGE
@app.route('/')
def reroute_login():
    return redirect('/login/page')

# DIRECTS TO THE LOGIN PAGE
@app.route('/login/page')
def login():
    return render_template('login.html')

# VALIDATES INPUTS FOR LOGGING IN
@app.route('/login', methods=['POST'])
def login_logic():
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid email/password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email/password', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/message/board')

# CREATES/VALIDATES USER AND INFORMATION INPUT THEN REROUTES TO MESSAGE BOARD
@app.route('/create/user', methods=['POST'])
def create_user():
    # Checking for validation
    if not User.validate_user(request.form):
        return redirect('/')
    # Creating hashed password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'id':request.form['id'],
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'email':request.form['email'],
        'password': pw_hash
    }
    # saving user information by data instead of request
    # storing this is user_id
    user_id = User.save(data)
    # saving user_id is session
    session['user_id'] = user_id
    return redirect('/message/board')

# CHECKS IF USER IS IN SESSION -
# IF SO DIRECTS TO THE MESSAGE BOARD
# IF NOT REDIRECTS TO THE LOGIN PAGE
@app.route('/message/board')
def messageboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('messageboard.html')

# CLEARS SESSION AND REDIRECTS TO LOGIN PAGE (LOGOUT)
@app.route('/clear')
def clearsessions():
    session.clear()
    return redirect('/')

#CREATES A POST AND THEN RELOADS THE PAGE SO THE USER CAN SEE
@app.route('/create/post', methods=['POST'])
def createpost():
    # VALIDATES THE POST IS NOT BLANK
    if not Message.validate_message(request.form):
        redirect('/message/board')
    user_post = Message.save(request.form)
    return redirect('/message/board')
