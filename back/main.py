from flask import Flask, Request, Response
#from .db import getConn

app = Flask(__name__)

@app.route("/api/getPosts")
def api():
    return {}

@app.route("/api/getPost<id>")
def getPost(id):
    return {}

# main router
app.start()