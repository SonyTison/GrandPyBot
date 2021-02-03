#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest, requests, json

from utils.api.wikipedia import Wikipedia

from utils.tests.api.constante_api_test import *


"""
This file (test_wikipedia.py) contains the unit tests for the wikipedia.py file.
"""

@pytest.fixture
def init_Wikipedia():
    '''Returns a Wikipedia instance'''
    return Wikipedia(48.8524383, 2.3702035, "Place de la Bastille, 75012 Paris, France")


def test_get_places_list_response_success(monkeypatch, init_Wikipedia):
    monkeypatch.setattr('requests.get', MockRequestsGet3)
    # status_code checked
    assert init_Wikipedia.get_places_list()[0] == 200
    # list of places checked
    assert init_Wikipedia.get_places_list()[1] == EXPECTED_RESULT_9[1]


def test_get_places_list_response_failure(monkeypatch, init_Wikipedia):
    class MockRequestsGet4:
        def __init__(self, url, params=None):
            self.status_code = 404
    monkeypatch.setattr('requests.get', MockRequestsGet4)
    assert init_Wikipedia.get_places_list() == 404


def test_get_story_cleaned_and_url_link_response_success(monkeypatch, init_Wikipedia):
    monkeypatch.setattr('requests.get', MockRequestsGet5)
    # status_code checked
    assert init_Wikipedia.get_story_cleaned_and_url_link(ARGUMENT_10)[0] == 200
    # story checked
    assert init_Wikipedia.get_story_cleaned_and_url_link(ARGUMENT_10)[1] == EXPECTED_RESULT_10[1]
    # url checked
    assert init_Wikipedia.get_story_cleaned_and_url_link(ARGUMENT_10)[2] == EXPECTED_RESULT_10[2]


def test_get_story_cleaned_and_url_link_response_failure(monkeypatch, init_Wikipedia):
    class MockRequestsGet6:
        def __init__(self, url, params=None):
            self.status_code = 404
    monkeypatch.setattr('requests.get', MockRequestsGet6)
    assert init_Wikipedia.get_places_list() == 404
