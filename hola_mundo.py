from flask import Flaskgi

app = Flask(__name__)

@app.route("/")

def index():
	return "hola mundo with flask and python"

app.run(host="0.0.0.0")

