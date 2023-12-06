def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store squared values for the current row
        squared_row = []

        # Iterate through each element in the current row and square it
        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)

        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix
