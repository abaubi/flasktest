from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return 'hola mundo with flask and python by Agusti B'

@app.route('/saluda')
def saluda():
	return 'otro mensaje desde saluda'

#http://192.168.0.154:8000/params?params1=Agusti
#http://192.168.0.154:8000/params
#http://192.168.0.154:8000/params?params1=Agusti&params2=test2
@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    param_dos = request.args.get('params2', 'no contiene este parametro')
    return 'El parametro es : {} , {}'.format(param, param_dos)
    
if __name__ == '__main__':
    app.run(debug = True, port=8000, host='0.0.0.0')