from flask import *
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    return "200 OK"
