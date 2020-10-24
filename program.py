from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

<<<<<<< HEAD
@app.route('/v2')
def hello_world_v2():
    return 'Hello, World! v2'

@app.route('/alekseev')
def alekseev():
    return 'Alekseev Andrey INBO-01-17'
=======
@app.route('/trm')
def hello_world_trm():
    return 'Hello, my name is Alexandr'

@app.route('/v2')
def another_text():
    return 'Another Text'

@app.route('/capchik')
def capchik():
    return 'Макущенко Максим'

@app.route('/danilkashtan')
def danilkashtan():
    return 'Асоян Данила'
>>>>>>> master
