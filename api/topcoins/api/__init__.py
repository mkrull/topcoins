import json

from flask import Flask

import topcoins.client as client

app = Flask(__name__)

@app.route('/topcoins')
def topcoins():
    '''
    topcoins returns a list of the top coins with their current prices.
    '''
    cfg = client.load_config()
    coins = client.get_ranking(cfg)
    pricing = client.get_pricing(cfg, coins)
    return json.dumps(pricing)


def run():
    '''
    run the flask app.
    '''
    app.run(host='0.0.0.0', port=3000, debug=False)
