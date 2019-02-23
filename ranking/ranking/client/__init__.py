import json
import math
import os

import requests


def load_config():
    config = {}
    config['api_token'] = os.environ['CRYPTOCOMPARE_API_TOKEN']
    config['url'] = os.environ.get('CRYPTOCOMPARE_URL', default='https://min-api.cryptocompare.com/data/top/mktcapfull')

    return config


def get_ranking_by_marketcap(config, limit=200):
    # As of the time of this writing the cryptocompare api supports a limit of
    # 100 elements thus multiple pages have to be fetched if limit is > 100.
    max_api_limit = 100
    limit = int(limit)
    pages = range(int(limit/max_api_limit))

    result = []
    for page in pages:
        params = {
            'limit': 100,
            'page': page,
            'tsym': 'USD' # required by cryptocompare api
        }
        headers = {
            'authorization': config['api_token']
        }
        resp = requests.get(config['url'], params=params, headers=headers)

        if resp.status_code == 200:
            result.extend(parse_api_response(resp.json()))

    return result


def parse_api_response(data):
    coins = []

    # scrub off everything we don't need for the ranking
    data = data['Data']

    for coin in data:
        info = coin['CoinInfo']
        coins.append({'name': info['Name']})

    return coins
