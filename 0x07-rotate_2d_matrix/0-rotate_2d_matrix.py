#!/usr/bin/python3
"""
2D matrix rotation.
"""

def rotate_2d_matrix(matrix):
    """
    2D matrix Rotation
    """
    i = 0
    for v in list(zip(*matrix)):
        matrix[i][:] = v[::-1]
        i += 1
