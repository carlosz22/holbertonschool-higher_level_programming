#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    my_new_list = my_list[:]
    if idx < 0 or idx >= list_len:
        return my_new_list
    my_new_list[idx] = element
    return my_new_list
