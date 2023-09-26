from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route('/')
def index():
    all_friends = Friend.get_all()
    return render_template('index.html', all_friends = all_friends)

@app.route('/friends/<int:friend_id>')
def show(friend_id):
    one_friend = Friend.get_one(friend_id)
    return render_template('show.html', friend = one_friend)

@app.route('/friends/create', methods=['POST'])
def create():
    Friend.save(request.form)
    return redirect('/')

@app.route('/friends/update', methods=['POST'])
def update():
    Friend.update(request.form)
    redirect("/")

@app.route('/friends/delete/<int:friend_id>', methods=['POST'])
def delete(friend_id):
    Friend.delete(friend_id)
    redirect('/')

if __name__ == "__main__":
    app.run(debug=True)