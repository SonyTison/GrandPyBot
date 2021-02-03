#!/usr/bin/python
# -*- coding: utf-8 -*-
from fuzzywuzzy import fuzz

from pprint import pprint

import re

import requests

URL = "https://fr.wikipedia.org/w/api.php"

class Wikipedia:

    def __init__(self, latitude, longitude, address):
        self.latitude = latitude
        self.longitude = longitude
        self.address = address


    def get_places_list(self):
        """ Return story linked to a location """
        
        params = {
            "format": "json", # format de la réponse
            "action": "query", # action à réaliser
            "list": "geosearch", # méthode de recherche
            "gslimit": "100",
            "gsradius": "10000", # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gscoord": f"{self.latitude}|{self.longitude}", # coordonnées GPS séparées par une barre verticale
        }

        res = requests.get(URL, params=params)
        if res.status_code != 200:
            return res.status_code

        response_data = res.json()
        return res.status_code, response_data['query']['geosearch']

    def get_pageid(self, places):
        """Return relevant pageid reference"""


        result = []
        for index, place in enumerate(places[1], start=0):
            a = None
            a = fuzz.token_set_ratio(places[1][index]['title'], self.address), places[1][index]['title'], places[1][index]['pageid'],
            result.append(a)
        res = sorted(result, reverse=True)
        return str(res[0][2])

    def get_story_cleaned_and_url_link(self, pageid):
        """ Return story linked to a pageid/location """
        
        params = {
            "format": "json", # format de la réponse
            "action": "query", # action à effectuer
            "prop": "extracts|info", # Choix des propriétés pour les pages requises
            "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
            "exchars": 1200, # Nombre de caractères à retourner
            "pageids": pageid,
            }

        res = requests.get(URL, params=params)
        if res.status_code != 200:
            return res.status_code

        response_data = res.json()
        # pprint(response_data)

        # Clean story data
        story_to_clean = response_data['query']['pages'][str(pageid)]['extract']
        result = story_to_clean.replace("&#160;;"," ")
        result = result.replace("&#160;"," ")
        regex = re.compile(r'[\n\r\t]')
        result = regex.sub(" ", result)
        cleaned_story = re.sub('<[^<]+?>', '', result)

        return res.status_code, cleaned_story, response_data['query']['pages'][str(pageid)]['fullurl']

# if __name__ == "__main__":
#     result = Wikipedia(48.8524383, 2.3702035, "Place de la Bastille, 75012 Paris, France")
#     res = result.get_places_list()
#     # # print(type(res))
#     # pprint(res)
#     res1 = result.get_pageid(res)
#     # print("----------------------")
#     # pprint(res1)
#     # print("----------------------")
#     res2 = result.get_story_cleaned_and_url_link(res1)
#     pprint(res2)