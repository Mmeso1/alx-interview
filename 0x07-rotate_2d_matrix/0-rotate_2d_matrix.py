#!/usr/bin/python3
'''
    ALX Interview - Rotating a 2D Matrix
'''


def rotate_2d_matrix(matrix):
    """ Roatate a 2D Matrix
    """
    n = len(matrix)
    temp = [[j for j in matrix[i]] for i in range(n)]
    for i in range(n):
        for j in range(len(matrix[0])):
            matrix[i][j] = temp[n - j - 1][i]
