#!/usr/bin/python3
""" rth er heyt hety het y"""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers['X-Request-Id'])
