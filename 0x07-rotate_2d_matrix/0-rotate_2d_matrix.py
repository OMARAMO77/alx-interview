#!/usr/bin/python3
"""2D matrix rotation module.
"""


def transpose_matrix(m):
    """Transposes a two dimension matrix
    """
    for i in range(len(m)):
        for j in range(i, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]


def reverse_matrix(matrix):
    """Reverses a two dimension matrix
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """Rotates a two dimension matrix 90 degrees clockwise
    """
    transpose_matrix(matrix)
    reverse_matrix(matrix)
