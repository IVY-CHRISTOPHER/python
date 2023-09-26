from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/1')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
    # import statements, maybe some other routes
@app.route('/success')
def success():
        return "success"
    
# app.run(debug=True) should be the very last statement! 
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<string:name>')
def hi_input(name):
    print(name)
    return 'Hi ' + name

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num,word):
    print(word)
    print(num)
    return word*num

#W3L3 -----------------

@app.route('/2')
def index():
    return 'Hello World'

@app.route('/')
def HomePage():
    return render_template('index.html',paragraph='Test Words')


if __name__=="__main__":
    app.run(debug=True)

