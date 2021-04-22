from flask import Flask, render_template,request
from flask_script import Manager, Command, Shell
import datetime
now = datetime.datetime.now()-datetime.timedelta(hours=12)
now = datetime.datetime.strftime(now, '%Y%m%d%H')
print(now)
app = Flask(__name__)
manager = Manager(app)

# class Faker(Command):
#     'Команда для добавления поддельных данных в таблицы'
#     def run(self):
#         # логика функции
#         print("Fake data entered")
# manager.add_command("faker", Faker())

# @manager.command
# def foo():
#     "Это созданная команда"
#     print("foo command executed")

def shell_context():
    import os, sys
    return dict(app=app, os=os, sys=sys)

manager.add_command("shell", Shell(make_context=shell_context))


#@app.route('/')
# def index():
#     return render_template('index.html', name='Jerry')

# @app.route('/user/<int:user_id>/')
# def user_profile(user_id):
#     return "Profile page of user #{}".format(user_id)

# @app.route('/books/<genre>/')
# def books(genre):
#     return "All Books in {} category".format(genre)

@app.route('/', methods=['post', 'get'])
def query_date():
    message = ''
    startdate = '2020071500'
    enddate = now
    if request.method == 'POST':
	    startdate = request.form.get('startdate')  # запрос к данным формы
	    enddate = request.form.get('enddate')

    if datetime.datetime.strptime(startdate, '%Y%m%d%H') < datetime.datetime.strptime(enddate, '%Y%m%d%H'):
	    message = "Введите дату в формате ГГГГММДДЧЧ"
    else:
	    message = "Дата  не корректна"

    return render_template('query.html', message=message)

if __name__ == "__main__":
#    app.run()
    manager.run()