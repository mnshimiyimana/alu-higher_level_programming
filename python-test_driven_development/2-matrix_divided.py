#!/usr/bin/python3
"""Function that divides all elements in a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    error_msg = "matrix must be a matrix (list of lists) integers/floats"
    new_matrix = []
    if type(matrix) is not list:
        raise TypeError(error_msg)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_msg)
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
