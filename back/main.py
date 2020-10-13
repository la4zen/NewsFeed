from flask import Flask, Request, Response
#from .db import getConn

app = Flask(__name__)

@app.route("/api")
def api():
    pass

# main router
app.start()