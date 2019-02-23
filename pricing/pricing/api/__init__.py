import json

from flask import Flask

app = Flask(__name__)

@app.route('/pricing')
def pricing():
    '''
    pricing returns a list of coins with their current prices.
    '''
    return json.dumps({'msg': 'hello'})


def run():
    '''
    run the flask app.
    '''
    app.run(host='0.0.0.0', port=3000, debug=False)
