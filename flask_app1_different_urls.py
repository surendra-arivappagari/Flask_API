from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world - Flask API"


@app.route('/bye')
def bye_world():
    return "Bye World - Flask API"


if __name__ == '__main__':
    app.run()