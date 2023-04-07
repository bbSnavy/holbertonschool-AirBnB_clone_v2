#!/usr/bin/python3
"""hello flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text: str):
    return "C%s" % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
