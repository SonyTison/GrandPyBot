import json

from pprint import pprint

from utils.api import googlemaps, wikipedia

from utils import parsers

from utils.manager import AnswerManager

@pytest.fixture
def init_AnswerManager():
    '''Returns a AnswerManager instance'''
    return AnswerManager()


def test_class_AnswerManager_response_success_to_user(monkeypatch, init_AnswerManager):

    # mocker class PARSER et toutes les méthode de la classe
    # mocker class GoogleMap et toutes les méthodes de la classe
    # mocker class Wikipedia et toutes les méthodes de le classe

    pass

def test_class_AnswerManager_response_failure_due_parser_failure(monkeypatch, init_AnswerManager):

    pass

def test_class_AnswerManager_response_failure_due_google_failure(monkeypatch, init_AnswerManager):

    pass

def test_class_AnswerManager_response_failure_due_wikipedia_failure_1(monkeypatch, init_AnswerManager):

    pass

def test_class_AnswerManager_response_failure_due_wikipedia_failure_2(monkeypatch, init_AnswerManager):

    pass