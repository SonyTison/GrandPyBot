#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The aim of this module is to extract keywords from user-entry"""

import unidecode, string

from .constante import stop_words

class Parser:
    """
    Class responsible to parse, clean user entry and return keywords
    """
    def __init__(self):
        self.user_entry = None
        
    def lower_user_entry(self, user_entry):
        """return all user_entry in lower case"""
        return user_entry.lower()
    
    def remove_accents(self, text_lower):
        """return all user_entry without any accents"""
        return unidecode.unidecode(text_lower)
    
    def remove_punctuation(self, text_acc):
        """return a given text without punctutation"""
        table = string.punctuation
        temp = " ".join(
            "".join(" " if ch in table else ch for ch in text_acc).split())
        return temp.split()
    
    def get_keywords(self, list_words_wt_punc):
        """return keywords by usisng personalized stop_words file"""
        keyword = [word for word in list_words_wt_punc if word not in stop_words]
        if not keyword:
            return None

        result = "+".join(keyword)
        filtre = [bool(item.isnumeric()) for item in result]
        if False not in filtre:
            return None
        else:
            return result


# if __name__ == "__main__":
#     """
#     Return keywords from a text provided by a user
#     >>> user_entry_parser("Dis Grandpy bot, où se trouve Kuala Lumpur, s'il te plaît !!")
#     'kuala+lumpur'
#     >>> user_entry_parser("Grandpy, ou se situe pointe-a-pitre ?")
#     ['pointe', 'pitre']
#     >>> user_entry_parser("GrandPy, connais-tu l'adresse du stade de France ?")
#     ['stade', 'france']
#     >>> user_entry_parser("")
#     Désolé. Je me fais vieux. Peux-tu me reposer ta question ?
#     """
#     result = Parser()
#     res_low = result.lower_user_entry("Dis Grandpy bot, où se trouve 2  , s'il te plaît !!")
#     print(res_low)
#     res_acc = result.remove_accents(res_low)
#     print(res_acc)
#     res_punc = result.remove_punctuation(res_acc)
#     print(res_punc)
#     res_keywords = result.get_keywords(res_punc)
#     print(res_keywords)
#     print(type(res_keywords))