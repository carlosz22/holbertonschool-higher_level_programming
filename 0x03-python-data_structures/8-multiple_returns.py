#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    my_tuple = ()
    my_tuple += (len_s,)
    if len_s == 0:
        my_tuple += (None,)
    else:
        my_tuple += (sentence[0],)
    return my_tuple
