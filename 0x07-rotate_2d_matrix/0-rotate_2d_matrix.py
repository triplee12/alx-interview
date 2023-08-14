#!/usr/bin/python3
"""Rotate 2D matrix."""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D matrix.

    Args:
        matrix (list): A 2D matrix. A list of lists

    Returns:
        list: A list of lists
    """
    length = len(matrix)

    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the matrix
    for i in range(length):
        matrix[i] = matrix[i][::-1]
    return matrix
