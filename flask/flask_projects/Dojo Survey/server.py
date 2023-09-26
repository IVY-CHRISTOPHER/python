from flask import Flask, session, redirect, request, render_template

app=Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def create_user():
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    session['userpassword'] = request.form['password']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['fav_Language']
    session['usercomment'] = request.form['comments']
    return redirect('/Showuser')

@app.route('/Showuser')
def userpage():
    return render_template('user.html')




if __name__ =="__main__":
    app.run(debug=True)