def square_matrix_simple(matrix=[]):
    result_matrix = []

    for row in matrix:
        squared_row = []

        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)

        result_matrix.append(squared_row)

    return result_matrix
