def square_matrix_alternative(matrix=[]):
    # Create a new matrix with the same values as the original matrix
    new_result_matrix = [row[:] for row in matrix]

    # Iterate through the rows and columns of the new matrix, replacing each element with its square
    for row_idx, row in enumerate(new_result_matrix):
        for col_idx, col in enumerate(new_result_matrix):
            new_result_matrix[row_idx][col_idx] = row[col_idx] ** 2

    # Return the new matrix with squared values
    return new_result_matrix
