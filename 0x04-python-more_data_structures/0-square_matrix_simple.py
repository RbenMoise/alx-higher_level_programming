#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()

    for row in matrix:
        newrow = [x**2 for x in row]
        new.append(newrow)
    return (new)
