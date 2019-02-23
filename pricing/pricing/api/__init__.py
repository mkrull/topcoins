import json

from flask import Flask, request

import pricing.client as client

app = Flask(__name__)

@app.route('/pricing', methods=['POST'])
def pricing():
    '''
    pricing returns a list of coins with their current prices.
    '''
    coins = request.get_json()
    prices = client.get_prices(client.load_config(), coins)
    return json.dumps(prices)


def run():
    '''
    run the flask app.
    '''
    app.run(host='0.0.0.0', port=3000, debug=False)
