#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    if l == 1:
        print("{} arguments.".format(length - 1))
    elif l == 2:
        print("{} argument:".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))
    for i in range(1, l):
        print("{}: {}".format(i, sys.argv[i]))
