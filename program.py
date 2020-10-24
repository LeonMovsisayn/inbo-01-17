from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v2')
def another_text():
    return 'Another Text'

@app.route('/capchik')
def capchik():
    return 'Макущенко Максим'

@app.route('/danilkashtan')
def danilkashtan():
    return 'Асоян Данила'