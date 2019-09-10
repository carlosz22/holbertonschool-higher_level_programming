#!/usr/bin/python3
def remove_char_at(str, n):

    i = 0
    str_cpy = ""
    for letter in str[:]:
        if i != n:
            str_cpy += letter
        i += 1

    return str_cpy
