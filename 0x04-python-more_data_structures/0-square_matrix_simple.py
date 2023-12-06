#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for r_index, row in enumerate(new_matrix):
        for c_index, col in enumerate(new_matrix):
            new_matrix[r_index][c_index] = row[c_index] ** 2
    return new_matrix 
