from flask import Flask, Request, Response
import sqlite3
from util import dict_factory

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
""")
db.commit()

@app.route("/api/getPosts")
def getPosts():
    c.execute("SELECT * FROM posts")
    return {"response" : c.fetchall()}

@app.route("/api/getPost<id>")
def getPost(id):
    c.execute(f"SELECT * FROM posts WHERE id={id}")
    return {"response":c.fetchone()}

# main router
app.run()