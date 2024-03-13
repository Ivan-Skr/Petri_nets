from flask import Flask, render_template, json, request
import os
import multiprocessing


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Task

app = Flask(__name__)

engine = create_engine('sqlite:///main.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/training')
def instruction():
    return render_template('instruction.html')


@app.route('/simulator')
def simulator():
    return render_template('simulator.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/tasks/<task_num>/', methods=['POST', 'GET'])
def tasks(task_num):
    if request.method == 'POST':
        if task_num == '0':
            name = request.form['name']
            print(name)
            return render_template('tasks.html', task = 0)
        else:
            get_tasks = session.query(Task).all()
            task = get_tasks[int(task_num)-1]
            listt = list(range(0, task.iterations+1))
            
            answers = []
            for _ in range(int(task.iterations)):
                a = []
                for _1 in range(int(task.sets)):
                    a.append(int(request.form[f'class{_+2}-{_1+1}']))
                answers.append(a)

            print(answers)
            return render_template('tasks.html', task = task, listt=listt)
    elif request.method == 'GET':
        if task_num == '0':
            return render_template('tasks.html', task = 0)
        else:
            get_tasks = session.query(Task).all()
            try:
                task = get_tasks[int(task_num)-1]
                listt = list(range(0, task.iterations+1))
                return render_template('tasks.html', task = task, listt=listt)
            except Exception:
                return render_template('tasks.html', task = 100)



def app_run():
    app.run(port=8081, host='127.0.0.1')

def game_run():
    os.system('C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts\\pygbag.exe C:\\Users\\User\\Desktop\\Petri_nets')



if __name__ == '__main__':
    process1 = multiprocessing.Process(target = app_run)
    process2 = multiprocessing.Process(target = game_run)
    process1.start()
    # process2.start()