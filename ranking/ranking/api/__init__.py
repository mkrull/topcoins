import json

import ranking.client as client

from flask import Flask, request

app = Flask(__name__)

@app.route('/ranking')
def ranking():
    '''
    ranking returns a list of top coins.
    '''

    limit = request.args.get('limit', 200)
    ranking = client.get_ranking_by_marketcap(client.load_config(), limit)

    return json.dumps(ranking)


def run():
    '''
    run the flask app.
    '''
    app.run(host='0.0.0.0', port=3000, debug=False)
