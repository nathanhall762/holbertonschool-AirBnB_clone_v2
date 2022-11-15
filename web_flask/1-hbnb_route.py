#!/usr/bin/python3
"""documentation"""
from flask import Flask


flask_app = Flask(__name__)


@flask_app.route('/', strict_slashes=False)
def index():
    """documentation"""
    return 'Hello HBNB!'


@flask_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """documentation"""
    return 'HBNB'


if __name__ == '__main__':
    flask_app.run('0.0.0.0')
