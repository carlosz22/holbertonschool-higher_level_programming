#!/usr/bin/python3
"""
"""


def text_indentation(text):
    """
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text_cpy = text[:]

    text_cpy = text_cpy.replace("?", "?<>")
    text_cpy = text_cpy.replace(":", ":<>")
    text_cpy = text_cpy.replace(".", ".<>")

    text_split = text_cpy.split('<>')

    for i in range(len(text_split)):
        text_split[i] = text_split[i].strip()

    for i in range(len(text_split)):
        if i == len(text_split) - 1:
            print("{}".format(text_split[i]), end='')
        else:
            print("{}\n".format(text_split[i]))
