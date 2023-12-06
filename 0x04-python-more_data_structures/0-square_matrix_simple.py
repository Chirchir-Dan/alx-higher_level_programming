#!/usr/bin/python3

def calculate_squared_matrix(input_matrix=[]):
    # Generate a fresh matrix with matching values to the original matrix
    result_matrix = [row[:] for row in input_matrix]

    # Iterate through the rows and columns of the result matrix, updating each element with its square
    for row_index, row in enumerate(result_matrix):
        for col_index, col in enumerate(result_matrix):
            result_matrix[row_index][col_index] = row[col_index] ** 2

    # Offer the result matrix with squared values
    return result_matrix
