#!/usr/bin/python3
""" ysrthrs6t hyer6 hyed6hy"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
