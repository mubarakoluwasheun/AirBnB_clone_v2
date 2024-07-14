#!/usr/bin/python3
"""Start a Flask application.
Routes: /, /hbnb, /c/<text>, /python/<text>, /number/<n>"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Displays 'Python' followed by the value of <text>"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def num(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
