import json
import unittest

import pytest

import ranking.api as api


def client():
    api.app.config['TESTING'] = True
    return api.app.test_client()


class APITest(unittest.TestCase):
    def test_ranking_endpoint(self):
        res = client().get('/ranking')
        assert res.status_code == 200
        assert json.loads(res.data) == {'msg': 'hello'}
