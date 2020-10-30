from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v2')
def hello_world_v2():
    return 'Hello, World! v2'

@app.route('/alekseev')
def alekseev():
    return 'Alekseev Andrey INBO-01-17'

@app.route('/v2')
def another_text():
    return 'Another Text'

@app.route('/trm')
def hello_world_trm():
    return 'Hello, my name is Alexandr'

@app.route('/trm')
def hello_world_test():
    return 'test complite!'

@app.route('/KretOFF')
def KretOFF():
    return 'Кретов Валерий Витальевич выполнил практику'
  
@app.route('/capchik')
def capchik():
    return 'Макущенко Максим'

@app.route('/danilkashtan')
def danilkashtan():
    return 'Асоян Данила'

@app.route('/issue9')
def danilkashtan():
    return 'Alekseev issue9'

@app.route('/IF0XI')
def IF0XI():
    return 'Полещук Е.С. выполнил практику'