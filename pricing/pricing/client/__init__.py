import json
import os

import requests


def load_config():
    config = {}
    config['api_token'] = os.environ['COINMARKETCAP_API_TOKEN']
    config['url'] = os.environ.get('COINMARKETCAP_URL', default='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest')

    return config


def get_prices(config, coins):
    # coins is a list of coin short-names (structured as {'name': 'xyz'} that
    # has to be provided as comma separated list to coinmarketcap.

    # hacky as hell
    # TODO: figure out how to filter out unsupported/invalid coins
    unsupported = ['GXS', 'BEC', 'HSR', 'IOT']
    supported = []
    for c in coins:
        if not c['name'] in unsupported:
            supported.append(c['name'].strip('*'))

    params = {
        'symbol': ','.join(supported)
    }
    headers = {
        'X-CMC_PRO_API_KEY': config['api_token']
    }

    resp = requests.get(config['url'], params=params, headers=headers)

    prices = {}
    if resp.status_code == 200:
        prices = parse_api_response(resp.json())
    else:
        raise Exception(resp.content)

    return augment(coins, prices)


def augment(coins, prices):
    result = []
    for coin in coins:
        result.append({
            coin['name']: prices.get(coin['name'].strip('*'), '-')})

    return result


def parse_api_response(data):
    # scrub off everything we don't need for the ranking
    result = {}
    data = data['data']
    for coin in data.keys():
        result[coin] = data[coin]['quote']['USD']['price']

    return result
