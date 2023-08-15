#!/usr/bin/env python3
"""rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    """rotate a 2d matrix"""
    matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
