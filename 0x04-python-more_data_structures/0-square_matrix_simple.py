#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        tuples = list(map(lambda integer: integer**2, row))
        new_matrix.append(tuples)
    return new_matrix
