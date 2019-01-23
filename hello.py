from flask import Flask,render_template
from resp import myresp

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/kambing')
def kambing():
    return 'kambing mantap'

@app.route('/kambing/<username>')
def kambing_show(username):
    return render_template('kambing.html', username=username)