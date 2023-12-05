#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    old_data = load_from_json_file('add_item.json')
except(ValueError, FileNotFoundError):
    old_data = []
for args in sys.argv[1:]
old_data.append(args)
save_to_json_file(old_data, 'add_item.json')
