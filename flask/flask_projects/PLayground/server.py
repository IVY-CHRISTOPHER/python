from flask import Flask,render_template, redirect, request

app = Flask(__name__)


@app.route('/play')
def index():
    return render_template('blocks.html', num=3, color='blue')

@app.route('/play/<int:num>')
def indexnumber(num):
    print('done')
    return render_template('blocks.html', num=num, color='blue')

@app.route('/play/<int:num>/<string:color>')
def indexnumcolor(num,color):
    return render_template('blocks.html', color = color, num=num)

if __name__ =="__main__":
    app.run(debug=True)