import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from contextlib import closing

#configuration
DATABASE =r'E:\project\flask_project\learn_project\flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app=Flask(__name__)
app.config.from_object(__name__) #寻找当前文件所有大写变量并导入它
# app.config.from_envvar('FLASKR_SETTINGS',silent=True) #允许你导入多份配置，并且使用最后的导入中定义的设置。

def connect_db():
    return  sqlite3.connect(app.config['DATABASE'])



def init_db():
   with closing(connect_db()) as db:  #保持持续连接
       with app.open_resource('schemal.sql',mode='r') as f:#打开文件并加载内容
           db.cursor().executescript(f.read())
       db.commit()

@app.before_request
def before_request():
    g.db  = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title,text from entries order by id DESC ')
    entries = [dict(title = row[0],text = row[1]) for row in cur.fetchall()]
    return  render_template('show_entries.html',entries= entries)

@app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        

if __name__ == '__main__':
    app.run()