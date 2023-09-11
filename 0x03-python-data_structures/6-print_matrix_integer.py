#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for column in matrix:
        i = 0
        for elem in column:
            i += 1
            print('{:d}'.format(elem), end=(" " if i < len(column) else ""))
        print()
