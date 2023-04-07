#!/usr/bin/python3
"""flask"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route_index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_flashes=False)
def route_hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000)
