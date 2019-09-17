#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    result = my_list[0]
    if len_list == 0:
        return None
    for i in my_list:
        if i > result:
            result = i
    return result
