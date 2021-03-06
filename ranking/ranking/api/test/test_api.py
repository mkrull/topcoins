import json
import os
import unittest
import unittest.mock as mock

import ranking.api as api


def client():
    api.app.config['TESTING'] = True
    return api.app.test_client()


class APITest(unittest.TestCase):
    def setUp(self):
        os.environ['CYPTOCOMPARE_API_TOKEN'] = 'some_token'

    @mock.patch('ranking.client.get_ranking_by_marketcap')
    def test_ranking_endpoint(self, mock_ranking):
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
        mock_ranking.return_value = expected
        res = client().get('/ranking')
        assert res.status_code == 200
        assert json.loads(res.data) == expected
