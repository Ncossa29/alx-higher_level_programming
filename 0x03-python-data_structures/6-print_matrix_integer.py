#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for col in range(len(lst)):
            print(
                "{:d}".format(lst[col]),
                end="" if col == len(lst) - 1 else " ")
        print("")
