#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for j in i:
            if j != i:
                print("{:d}".format(j), end= ' ')
            else:
               print("{:d} ".format(j), end='')
        print()

