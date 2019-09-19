#!/usr/bin/python3
def uniq_add(my_list=[]):
    clean_list = list(dict.fromkeys(my_list))
    result = 0
    for i in clean_list:
        result += i
    return result
