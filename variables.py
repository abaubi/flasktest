from flask import Flask
from flask import render_template

app = Flask(__name__)

#http://192.168.0.154:8000/user/Agusti
@app.route('/user/<name>')
def user(name='Agusti'):
    age=18
    my_list=[1,2,3,4]
    return render_template('user.html', nombre= name,edad=age,lista=my_list)

if __name__ == '__main__':
    app.run(debug = True, port=8000, host='0.0.0.0')