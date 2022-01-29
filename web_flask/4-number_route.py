#!/usr/bin/python3
'''This script starts a Flask web app
   Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        /python/(<text>): display Python + <text_var>
        /number/<n>: display “n is a number” only if n is an integer
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''displays Hello HBNB!'''
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''displays HBNB'''
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )'''
    newText = text.replace('_', ' ')
    return ('C {}'.format(newText))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    '''display “Python ”, followed by the value of the text variable'''
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''display “n is a number” only if n is an integer'''
    return ('{:d} is a number'.format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
