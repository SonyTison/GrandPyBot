#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module manage the answer to the user question"""

import json

from pprint import pprint

from utils.api.googlemaps import GoogleMap

from utils.api.wikipedia import Wikipedia

from utils.parsers import Parser

class AnswerManager:

    def __init__(self):
        pass

    def answer(self, user_entry):
        self.user_entry = user_entry

        """
        Manage the user's question and returns a dictionary
        containing grandpy's answer, address, coordinates (lat, long), wiki article
        and the url for more information.
        """
        address = ""
        latitude = None
        longitude = None
        wiki_article = ""
        url = ""

        result = Parser()
        res_low = result.lower_user_entry(self.user_entry)
        res_acc = result.remove_accents(res_low)
        res_punc = result.remove_punctuation(res_acc)
        keywords = result.get_keywords(res_punc)

        if keywords is None:
            return("Peux-tu poser une autre question? Là c'est compliqué 1...")

        response = GoogleMap()
        result1 = response.geocode(keywords)
        if result1 == 400:
            return("Peux-tu poser une autre question? Là c'est compliqué 2...")

        address, latitude, longitude = result1[1], result1[2], result1[3]

        places_list = Wikipedia(latitude, longitude, address)
        result2 = places_list.get_places_list()
 
        if result2 == 400:
            return("Peux-tu poser une autre question? Là c'est compliqué 3...")
        result3 = places_list.get_pageid(result2)
        result4 = places_list.get_story_cleaned_and_url_link(result3)

        if result4 == 400:
            return("Peux-tu poser une autre question? Là c'est compliqué 4...")
        wiki_article, url = result4[1], result4[2]

        return {"sentence": "Voici la réponse à ta question: ",
                "address": address,
                "latitude": latitude,
                "longitude": longitude,
                "story": wiki_article,
                "url link": url
                }

if __name__ == "__main__":
    print("")
    print("")
    user_entry = input("Pose ici ta question Geographique ?: ")
    answer = AnswerManager()
    result_final = answer.answer(user_entry)
    pprint(result_final)
