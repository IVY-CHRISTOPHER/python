from Flask_App import app
from flask import render_template,redirect,request,session
from Flask_App.models.user import User


@app.route('/')
def index():
    all_users = User.get_all_users()
    return render_template('Read(ALL).html', all_users = all_users)

@app.route('/c')
def create_page():
    return render_template('Create.html')

@app.route('/create_user', methods = ['POST'])
def create():
    if not User.validate_user(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/')