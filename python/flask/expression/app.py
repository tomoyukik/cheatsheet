import flask
from . import Kazu
import logging

# %%
app = flask.Flask(__name__)

@app.route('/abc')
def cde():
    return '123'

@app.route('/<exp>', methods=['GET'])
def calc(exp):
    nm = flask.request.args.to_dict()
    if exp == 'add':
        # return str(5)
        return str(Kazu(int(nm['n'])).add(int(nm['m'])).to_int())
    if exp == 'sabtract':
        # return str(10)
        return str(Kazu(int(nm['n'])).sabtract(int(nm['m'])).to_int())
    return str(111)

@app.route('/dic')
def dic():
    return {'one': 1, 'two': 2}