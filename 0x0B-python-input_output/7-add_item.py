#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""

import sys
import json


def save_to_json_file(my_obj, filename):
    """ y6re u udr u6d u"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=2)


def load_from_json_file(filename):
    """ yw54s 6w4usr yu sur"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

new_items = sys.argv[1:]
updated_items = existing_items + new_items

save_to_json_file(updated_items, "add_item.json")
