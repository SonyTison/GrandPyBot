#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file is used to test the functions of parsers.py"""

from utils.parsers import Parser

import pytest

from utils.tests.constante_tests import *

@pytest.fixture
def init_parser():
    '''Returns a Parser instance'''
    return Parser()

def test_lower_user_entry_return_is_ok_1(init_parser):
    assert init_parser.lower_user_entry(ARGUMENT_1) == EXPECTED_RESULT_1

def test_remove_accents_from_lower_user_entry_is_ok_2(init_parser):
    assert init_parser.remove_accents(ARGUMENT_2) == EXPECTED_RESULT_2

def test_remove_punctuation_from_remove_accents_entry_return_a_list_3(init_parser):
    assert isinstance(init_parser.remove_punctuation(ARGUMENT_3), list)

def test_remove_punctuation_from_remove_accents_entry_return_a_list_of_string_4(init_parser):
    assert init_parser.remove_punctuation(ARGUMENT_4) == EXPECTED_RESULT_4

def test_get_keywords_return_string_list_from_remove_accents_by_using_stop_word_list_5(init_parser):
    assert isinstance(init_parser.get_keywords(ARGUMENT_5), str)

def test_get_keywords_raises_exception_in_case_of_no_keywords_returned_6(init_parser):
    assert init_parser.get_keywords(ARGUMENT_6) is None

def test_get_keywords_raises_exception_in_case_of_no_valid_keywords_returned_7(init_parser):
    assert init_parser.get_keywords(ARGUMENT_7) is None
