#!/usr/bin/python3
for first in range(10):
    for second in range(1, 10):
        if first != second:
            print("{:02d}, ".format(first * 10 + second), end='')
print("{:02d}".format(98))
