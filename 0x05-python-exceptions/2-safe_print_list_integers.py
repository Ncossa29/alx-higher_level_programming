#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
            for x in range(c):
                print("", end="")
        except (ValueError, TypeError):
            print("", end="")
    print()
    return c
