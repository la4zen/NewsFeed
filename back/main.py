from flask import Flask

app = Flask(__name__)

@app.route("/api")
def api(params):
    pass

# main router