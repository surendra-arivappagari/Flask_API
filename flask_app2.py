from flask import Flask, jsonify

app = Flask(__name__)

# using jsonify to make output with key,value paired.
@app.route('/')
def hello_world():
    return jsonify(message="Hello world - Flask API")


# using jsonify to make output with key,value paired.
@app.route('/bye')
def bye_world():
    return jsonify(message="Bye World - Flask API")


if __name__ == '__main__':
    app.run(debug=True)