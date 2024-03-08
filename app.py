from flask import Flask, render_template, json
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


@app.route('/tasks/<task_num>/')
def tasks(task_num):
    get_tasks = session.query(Task).all()
    task = get_tasks[int(task_num)-1]
    return render_template('tasks.html', task = task)


def app_run():
    app.run(port=8081, host='127.0.0.1')

def game_run():
        os.system('C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts\\pygbag.exe C:\\Users\\User\\Desktop\\Petri_nets')



if __name__ == '__main__':
    process1 = multiprocessing.Process(target = app_run)
    process2 = multiprocessing.Process(target = game_run)
    process1.start()
    # process2.start()