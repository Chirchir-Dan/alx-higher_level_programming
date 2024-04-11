#!/usr/bin/python3
"""
This module provides a matrix division function
"""


def matrix_divided(matrix, div):
    """
    This function divides all the elements of a matrix.

    Args:
        matrix (list): The original matrix to be divided.
        div (int, float): The number to divide the matrix by

    Raises:
        TypeError: If matrix is not a list of lists
                    of integers or floats, or div is not a number
        ZeroDivisionError: If div is equal to 0.

    Returns:
        returns a divided matrix.
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    # Check if all elements of the matrix are integers or floats
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(num / div, 2) for num in row] for row in matrix]
