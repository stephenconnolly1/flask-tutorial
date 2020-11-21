from flask import Flask
app = Flask(__name__)

@app.route('/hiya')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Indexor Home Page'
