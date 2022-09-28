#!/usr/bin/python3


def square_num(num):
    return num ** 2


def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
           new_matrix[i][j] = square_num(new_matrix[i][j])
    return new_matrix
