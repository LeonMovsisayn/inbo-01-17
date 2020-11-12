from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v2')
def hello_world_v2():
    return 'Hello, World! v2'

@app.route('/alekseev_4')
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
def issue9():
    return 'Alekseev issue9'

@app.route('/IF0XI')
def IF0XI():
    return 'Полещук Е.С. выполнил практику'

@app.route('/migunoffm')
def migunoffm():
    return 'Мигунов коммит номер 2'

@app.route('/sivashova3pr')
def sivashova3pr():
    return 'Сивашова Людмила 3 практика'

@app.route('/minachev3pr')
def minachev3pr():
    return 'Миначёв Артём Шамилевич практика 3'

@app.route('/Drozhzhin')
def VegetableX():
    return 'Дрожжин А.В. выполнение практики 20:46'

    @app.route('/astakhov')
def astakhov():
    return 'Астахов К.А. ИНБО-01-17'

    @app.route('/LeonMovsisyan')
def LeonMovsisyan():
    return 'Леон Мовсисян INBO-01-17'
