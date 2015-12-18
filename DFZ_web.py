#coding=utf-8
from flask import Flask
from flask import request
from flask import current_app
from flask import g
from flask import session
from flask import make_response
from flask import redirect
from flask import abort
from flask.ext.bootstrap import Bootstrap
from flask import render_template
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)
#manager = Manager(app)
@app.route('/', methods=['get', 'post'])
def hello_world():
    #response = make_response("<h1>This document carries a cookie!</h1>")
    #response.set_cookie('hellosb','400')
    #response.headers['Content-Type']= "json"
    return render_template('index.html', current_time=datetime.utcnow())
@app.route('/user/<name>')
def hello_user(name):
    return render_template('user.html', name=name)

@app.route('/about')
def about():
    return "this is dfz"
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
if __name__ == '__main__':
    app.run(debug=False)
