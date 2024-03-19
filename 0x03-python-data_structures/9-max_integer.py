def max_integer(my_list=[]):
    if my_list is None:
        return
    if len(my_list) == 0:
        return
    mx = my_list[0]
    for i in my_list:
        if i > mx:
            mx = i
    return mx
