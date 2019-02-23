import json
import unittest

import pytest

import pricing.api as api


def client():
    api.app.config['TESTING'] = True
    return api.app.test_client()


class APITest(unittest.TestCase):
    def test_pricing_endpoint(self):
        res = client().get('/pricing')
        assert res.status_code == 200
        assert json.loads(res.data) == {'msg': 'hello'}
