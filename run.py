from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
	return 'hola mundo with flask and python by Agusti B'

if __name__ == '__main__':
    app.run(debug = True, port=8000, host='0.0.0.0')