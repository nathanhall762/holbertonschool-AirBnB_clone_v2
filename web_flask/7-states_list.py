#!/usr/bin/python3
"""documentation"""
from flask import Flask
from flask import render_template
from models import storage


flask_app = Flask(__name__)


@flask_app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page of the States
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', db=storage.all(State))


@flask_app.teardown_appcontext
def teardown_db(error):
    """Closes the database again at the end of the request.
    """
    storage.close()


if __name__ == '__main__':
    flask_app.run('0.0.0.0')
