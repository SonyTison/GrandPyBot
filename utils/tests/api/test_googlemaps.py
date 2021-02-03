#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest, requests, json

from utils.api.googlemaps import GoogleMap

from utils.constante import API_KEY, GEOCODE_BASE_URL

from .constante_api_test import MockRequestsGet1

EXPECTED_RESULT_8 = (200, "5 Rue St. John Perse, Pointe-à-Pitre, Guadeloupe", 16.2365431, -61.5344845)


@pytest.fixture
def init_GoogleMap():
    '''Returns a GoogleMap instance'''
    return GoogleMap()

def test_geocode_get_response_success(monkeypatch, init_GoogleMap):
    monkeypatch.setattr('requests.get', MockRequestsGet1)
    assert init_GoogleMap.geocode("place+victoire+guadeloupe") == EXPECTED_RESULT_8
    # assert init_GoogleMap.geocode("place+victoire+guadeloupe")[0] == EXPECTED_RESULT_8[0]
    # assert type(init_GoogleMap.geocode("place+victoire+guadeloupe")[3]) == type(EXPECTED_RESULT_8[3])
    # assert init_GoogleMap.geocode("place+victoire+guadeloupe")[2] == EXPECTED_RESULT_8[2]
    # assert init_GoogleMap.geocode("place+victoire+guadeloupe")[3] == EXPECTED_RESULT_8[3]

def test_geocode_get_response_failure(monkeypatch, init_GoogleMap):
    class MockRequestsGet2:
        def __init__(self, url, params=None):
            self.status_code = 404
    monkeypatch.setattr('requests.get', MockRequestsGet2)
    assert init_GoogleMap.geocode("") == 404
