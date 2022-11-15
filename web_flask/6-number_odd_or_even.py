#!/usr/bin/python3
"""documentation"""
from flask import Flask, render_template


if __name__ == '__main__':
    flask_app = Flask(__name__)

    @flask_app.route('/', strict_slashes=False)
    def index():
        """documentation"""
        return 'Hello HBNB!'

    @flask_app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """documentation"""
        return 'HBNB'

    @flask_app.route('/c/<text>', strict_slashes=False)
    def c(text):
        """documentation"""
        return 'C' + text.replace('_', ' ')

    @flask_app.route('/python/')
    @flask_app.route('/python/<text>', strict_slashes=False)
    def python(text="is cool"):
        """documentation"""
        return 'Python' + text.replace('_', ' ')

    @flask_app.route('/number/<n>', strict_slashes=False)
    def number(n):
        """documentation"""
        return str(n) + 'is a number'

    @flask_app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n=None):
        """documentation"""
        if isinstance(n, int):
            return render_template("5-number.html", n=n)

    @flask_app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def even_or_odd(n=None):
        if isinstance(n, int):
            return render_template("6-number_odd_or_even.html")

    flask_app.run('0.0.0.0')
