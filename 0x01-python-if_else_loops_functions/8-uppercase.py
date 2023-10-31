#!/usr/bin/python3
def uppercase(str):
    result = 0
    for char in  str:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - ord('a') + ord('A'))
            result += upper
        else:
            result += char
    print(result, end='')

