from flask import Flask, request
import sqlite3, re
from util import *
from hashlib import md5

app = Flask(__name__)

db = sqlite3.connect("database.sqlite3", check_same_thread=False)
db.row_factory = dict_factory
c = db.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        text TEXT,
        date DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   
        user_name TEXT,
        password TEXT,
        regtime DATETIME DEFAULT CURRENT_TIMESTAMP
    ); 
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        token TEXT
    );
""")
db.commit()

@app.route("/api/getPosts")
def getPosts():
    c.execute("SELECT * FROM posts")
    return {"response" : c.fetchall()}

@app.route("/api/getPost_<id>")
def getPost(id):
    c.execute(f"SELECT * FROM posts WHERE id={id}")
    result = c.fetchone()
    return {"response" : result} if result != None else {"error" : "id not found"}

@app.route("/api/login")
def login():
    return {"response" : 200}

@app.route("/api/register")
def register():
    login, password = request.data.get("login"), request.data.get("password")
    r = r"[A-Za-z]"
    if any([login, password]) == None:
        return {"error" : "Необходимо указать логин и пароль"}
    elif all([len(login) < 6, len(password) < 8]):
        return {"error" : "Длина логина должна быть больше 6-ти символов, а пароль должен быть больше 8-ми символов"}
    elif all([re.sub(r, "", login), re.sub(r, "", password)]):
        return {"error" : "В логине или пароле не должны использоваться спец-символы"}
    else:
        c.execute(f"SELECT * FROM users WHERE login='{login}'")
        if c.fetchone():
            return {"error" : "Пользователь с таким логином уже существует."}
        else:
            tkn = randstr()
            lastrowid = c.execute(f"INSERT INTO users(user_name, password) VALUES ('{login}', '{md5(password)}')").lastrowid
            c.execute(f"INSERT INTO sessions(user_id, token) VALUES ({lastrowid}, '{tkn}')")
            return {"response" : 200, "tkn" : tkn}

# main router
app.run()