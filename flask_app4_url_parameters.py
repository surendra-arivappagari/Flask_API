from flask import Flask, jsonify, request

app = Flask(__name__)


# using jsonify, status code=200 for OK to make output with key,value paired.
@app.route('/')
def hello_world():
    return jsonify(message="Hello world - Flask API"), 200


# using jsonify, status code=200 for OK to make output with key,value paired.
@app.route('/bye')
def bye_world():
    return jsonify(message="Bye World - Flask API"), 200


# using jsonify, status code=200 for OK to make output with key,value paired.
@app.route('/bye_not_found')
def bye_not_found():
    return jsonify(message="Bye Not Found - Flask API"), 404


@app.route('/parameters')
def parameters():
    name = "surendra"
    age = "10"
    return jsonify(message="Hello "+name + ". you are "+age+" year old.")



if __name__ == '__main__':
    app.run(debug=True)