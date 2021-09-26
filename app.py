import threading
import logging
from flask import Flask, request
from flask.json import jsonify
from domain.dinning_hall import DinningHall


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/distribution', methods=['POST'])
def receive_order():
    distribution = request.json

    print(distribution)

    return jsonify(distribution)


if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()

    dinning_hall = DinningHall()
    dinning_hall.run_simulation()