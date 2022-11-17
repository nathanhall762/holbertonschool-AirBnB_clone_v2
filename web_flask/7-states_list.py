#!/usr/bin/python3
"""
documentation
"""
from flask import Flask, render_template
from models import storage
from models.state import State


flask_app = Flask(__name__)


@flask_app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html', db=storage.all(State))


@flask_app.teardown_appcontext
def teardown_db():
    storage.close()


if __name__ == '__main__':
    flask_app.run('0.0.0.0')
