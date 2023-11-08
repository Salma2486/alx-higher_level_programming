#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = list(map(lambda mat: list(map(lambda x : x**2, mat)), matrix))

    return sq
