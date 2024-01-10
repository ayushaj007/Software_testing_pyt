from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Configure the MongoDB connection
client = MongoClient('localhost', 27017) 
db = client['mydatabase'] 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Insert the user data into the MongoDB collection
        users = db['users']
        users.insert_one({'username': username, 'password': password})

        return redirect(url_for('success')) 

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = db['users']
        user_data = users.find_one({'username': username, 'password': password})

        if user_data:
            return render_template('profile.html', username=username)
        else:
            return "Login failed. Invalid username or password."

    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
