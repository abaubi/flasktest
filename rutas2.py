from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return 'hola mundo with flask and python by Agusti B'

@app.route('/saluda')
def saluda():
	return 'otro mensaje desde saluda'

#http://192.168.0.154:8000/params/hola
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>') #num debe ser entero
def params(name = 'este es un valor por default', num = 'nada'):
    return 'El parametro es : {} {}'.format(name, num)

if __name__ == '__main__':
    app.run(debug = True, port=8000, host='0.0.0.0')