#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    else:
        rev = my_list.reverse()
        for rev in my_list:
            print("{:d}".format(rev))

