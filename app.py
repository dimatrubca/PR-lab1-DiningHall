from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)


@app.route('/distribution', methods=['POST'])
def receive_order():
    distribution = request.json

    print(distribution)

    return jsonify(distribution)