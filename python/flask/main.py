# %%
# from expression.server import app
from expression import app

# from expression import app
# import flask
# from werkzeug.wrappers import request
# from expression import Kazu
# import logging
# 
# # %%
# app = flask.Flask(__name__)
# 
# @app.route('/abc')
# def cde():
#     return '123'
# 
# @app.route('/<exp>', methods=['GET'])
# def calc(exp):
#     nm = flask.request.args.to_dict()
#     if exp == 'add':
#         # return str(5)
#         return str(Kazu(int(nm['n'])).add(int(nm['m'])).to_int())
#     if exp == 'sabtract':
#         # return str(10)
#         return str(Kazu(int(nm['n'])).sabtract(int(nm['m'])).to_int())
#     return str(111)
# 
# @app.route('/dic')
# def dic():
#     return {'one': 1, 'two': 2}

if __name__ == '__main__':
    print('ddddddddd')
    app.run('127.0.0.1', port=3334, debug=True )
# %%
