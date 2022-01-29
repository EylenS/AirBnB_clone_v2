#!/usr/bin/python3
'''This script starts a Flask web app
   Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')