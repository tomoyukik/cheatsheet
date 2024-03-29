import flask
from expression import Kazu

CONFIGS = {
    'production': 'config.Config',
    'development': 'config.DevelopmentConfig',
    'test': 'config.TestConfig',
}

app = flask.Flask(__name__, instance_relative_config=True)

@app.route('/abc')
def cde():
    return '123'

@app.route('/<exp>', methods=['GET'])
def calc(exp):
    nm = flask.request.args.to_dict()
    if exp == 'add':
        return str(Kazu(int(nm['n'])).add(int(nm['m'])).to_int())
    if exp == 'sabtract':
        return str(Kazu(int(nm['n'])).sabtract(int(nm['m'])).to_int())
    return str(111)

@app.route('/dic')
def dic():
    return {'one': 1, 'two': 2}

@app.route('/history/add')
def add_history():
    pass

@app.route('work/<year>/<month>/<day>')
def work(year, month, day):
    return f'{year}-{month}-{day}'

if __name__ == '__main__':
    app.run('127.0.0.1', port=3334, debug=True )
