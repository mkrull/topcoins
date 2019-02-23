import json
import os

import requests


def load_config():
    config = {}
    config['pricing_url'] = os.environ['PRICING_URL']
    config['ranking_url'] = os.environ['RANKING_URL']

    return config

def get_ranking(config, limit=200):
    resp = requests.get(config['ranking_url'], {'limit': limit})

    return json.loads(resp.content)


def get_pricing(config, coins):
    resp = requests.post(config['pricing_url'], json=coins)

    return json.loads(resp.content)
