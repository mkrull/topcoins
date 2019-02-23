import json
import os
import unittest

import responses

import ranking.client as client


class CryptocompareTest(unittest.TestCase):
    def setUp(self):
        with open('ranking/client/test/cryptocompare_success.json') as fd:
            self.res_success = json.load(fd)

    def test_load_config(self):
        expected = 'some_api_token'
        os.environ['CYPTOCOMPARE_API_TOKEN'] = expected
        config = client.load_config()

        assert config['api_token'] == expected

    @responses.activate
    def test_get_ranking_by_marketcap(self):
        config = {'url': 'http://localhost/',
                  'api_token': 'sometoken'}
        responses.add(
            responses.GET,
            config['url'],
            json=self.res_success)

        result = client.get_ranking_by_marketcap(config, limit=100)
        assert len(responses.calls) == 1
        assert len(result) == 100

        assert responses.calls[0].request.url == config['url'] + '?limit=100&page=0&tsym=USD'
        assert responses.calls[0].request.headers['authorization'] == config['api_token']

        result = client.get_ranking_by_marketcap(config)
        # default limit is 200 and requires to pages, thus two more calls
        assert len(responses.calls) == 3
        assert len(result) == 200


    def test_parse_api_response(self):
        result = client.parse_api_response(self.res_success)
        expected = [{'name': 'BTC'},
                    {'name': 'XRP'},
                    {'name': 'ETH'},
                    {'name': 'EOS'},
                    {'name': 'LTC'},
                    {'name': 'BCH'},
                    {'name': 'BNB'},
                    {'name': 'USDT'},
                    {'name': 'XLM'},
                    {'name': 'TRX'},
                    {'name': 'ADA'},
                    {'name': 'BSV'},
                    {'name': 'XMR'},
                    {'name': 'IOT'},
                    {'name': 'DASH'},
                    {'name': 'MKR'},
                    {'name': 'HT'},
                    {'name': 'NEO'},
                    {'name': 'DCN'},
                    {'name': 'ONT'},
                    {'name': 'ETC'},
                    {'name': 'LINK'},
                    {'name': 'XEM'},
                    {'name': 'KBC'},
                    {'name': 'QKC'},
                    {'name': 'ZEC'},
                    {'name': 'WAVES'},
                    {'name': 'VET'},
                    {'name': 'ZRX'},
                    {'name': 'HOT*'},
                    {'name': 'DOGE'},
                    {'name': 'USDC'},
                    {'name': 'BEC'},
                    {'name': 'ZIL'},
                    {'name': 'QTUM'},
                    {'name': 'BTG'},
                    {'name': 'TUSD'},
                    {'name': 'BAT'},
                    {'name': 'NPXS'},
                    {'name': 'QNT'},
                    {'name': 'OMG'},
                    {'name': 'IOST'},
                    {'name': 'DCR'},
                    {'name': 'REP'},
                    {'name': 'SNT'},
                    {'name': 'LSK'},
                    {'name': 'XET'},
                    {'name': 'GNO'},
                    {'name': 'BCD'},
                    {'name': 'R'},
                    {'name': 'BTM*'},
                    {'name': 'NANO'},
                    {'name': 'DGB'},
                    {'name': 'BTS'},
                    {'name': 'PAX'},
                    {'name': 'QASH'},
                    {'name': 'STORJ'},
                    {'name': 'KMD'},
                    {'name': 'FTO'},
                    {'name': 'XVG'},
                    {'name': 'ICX'},
                    {'name': 'MANA'},
                    {'name': 'ABBC'},
                    {'name': 'DENT'},
                    {'name': 'THETA'},
                    {'name': 'MCO'},
                    {'name': 'POWR'},
                    {'name': 'BZ'},
                    {'name': 'STRAT'},
                    {'name': 'POLY*'},
                    {'name': 'SC'},
                    {'name': 'KCS'},
                    {'name': 'WAX'},
                    {'name': 'LRC'},
                    {'name': 'AOA'},
                    {'name': 'IOTX'},
                    {'name': 'WTC'},
                    {'name': 'EDO'},
                    {'name': 'ARK'},
                    {'name': 'GNT'},
                    {'name': 'PPT'},
                    {'name': 'DYN'},
                    {'name': 'PAI*'},
                    {'name': 'NAS'},
                    {'name': 'CVC'},
                    {'name': 'TOMO'},
                    {'name': 'FCT'},
                    {'name': 'MAID'},
                    {'name': 'ARDR'},
                    {'name': 'ENG'},
                    {'name': 'HC'},
                    {'name': 'HSR'},
                    {'name': 'PAY'},
                    {'name': 'LOOM'},
                    {'name': 'AGI'},
                    {'name': 'PIVX'},
                    {'name': 'ELF'},
                    {'name': 'EDR*'},
                    {'name': 'SAN'},
                    {'name': 'PRG'}]

        assert result == expected
