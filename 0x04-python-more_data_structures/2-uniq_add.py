#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for h in my_list:
        if h not in new_list:
            new_list.append(h)
    return sum(new_list)
