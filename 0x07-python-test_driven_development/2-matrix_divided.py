#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
    Matrix must be a list of list of integers or floats,
    otherwise a TypeError is raised"""
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for row in matrix:
        new_list = []
        for integer in row:
            if type(integer) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            try:
                division = integer / div
                result = round(division, 2)
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
            except IndexError:
                raise TypeError("Each row of the matrix must have the same size")
            new_list.append(result)
        new_matrix.append(new_list)
    return new_matrix
