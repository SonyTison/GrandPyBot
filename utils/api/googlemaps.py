#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Download address and coordinates for given keywords from the GoogleMaps API."""

import json

import requests

from utils.constante import API_KEY, GEOCODE_BASE_URL


class GoogleMap:
    def __init__(self):
        pass

    def geocode(self, query):
        """
        Return data location from the Google API following a given address
        """
        payload = {'address': query, 'key': API_KEY}

        api_res = requests.get(GEOCODE_BASE_URL, params=payload)
        if api_res.status_code != 200:
            return api_res.status_code

        data = api_res.json()
        return api_res.status_code, (data['results'][0]['formatted_address']), data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng']

# if __name__ == "__main__":
#     response = GoogleMap()
#     result = response.geocode(query="pointe+pitre")
#     print(type(result))
#     print(result)