from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name='Eduardo'
    my_list=[1,2,3,4]
    return render_template('index.html', name=name)


@app.route('/client')
def client():
    list_name = ['Test1', 'Test2', 'Test3']
    return render_template('client.html', list=list_name)

if __name__ == '__main__':
    app.run(debug = True, port=8000, host='0.0.0.0')