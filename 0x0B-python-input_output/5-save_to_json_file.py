#!/usr/bin/python3
""" seohg liaj ye5opk 6sr,s uo;r """


import json


def save_to_json_file(my_obj, filename):
    """oishet yoihsr tliyjs ytlihja tsya"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
