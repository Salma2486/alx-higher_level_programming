#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for i in matrix:
            for j in range(len(i)):
                if j == len(i) - 1:
                    print("{:d}".format(i[j]))
                else:
                    print("{:d} ".format(i[j]), end="")
            print()

