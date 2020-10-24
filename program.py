from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/v2')
def hello_world_v2():
    return 'Another text'

@app.route('/trm')
def hello_world_trm():
    return 'Hello, my name is Alexandr'