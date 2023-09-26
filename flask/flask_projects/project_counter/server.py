from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def counter():
    if not session['num']:
        session['num']=0
    else:
        session['num']
    return render_template('counter.html')


@app.route('/add', methods=['POST'])
def addingOne():
    print('Posted')
    if not session['num']:
        session['num']=0
    session['num']+=1
    return redirect('/')

@app.route('/add2', methods=['POST'])
def addingTwo():
    print('Posted')
    if not session['num']:
        session['num']=0
    session['num']+=2
    return redirect('/')

@app.route('/delete', methods=['POST'])
def deletesession():
    session.clear()
    session['num']=0
    return redirect('/')
    #session.pop('key_name')

@app.route('/clear', methods=['POST'])
def clearsession():
    session['num']=0
    return redirect('/')

@app.route('/customamount', methods=['POST'])
def customAmount():
    print('posted')
    if not session['num']:
        session['num']=0
    session['amount'] = request.form['amount']
    session['num'] += int(session['amount'])
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
