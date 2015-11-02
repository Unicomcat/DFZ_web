from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/about')
def about():
    return "this is dfz"

if __name__ == '__main__':
    app.run()
