#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
import sys


if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    old_data = load_json(file)

except (ValueError, FileNotFoundError):
    old_data = []
for args in sys.argv[1:]:
    old_data.append(args)
save_json(old_data, 'add_item.json')
