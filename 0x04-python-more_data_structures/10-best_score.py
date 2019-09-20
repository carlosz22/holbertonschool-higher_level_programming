#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    result = list(a_dictionary.keys())[0]
    first = a_dictionary[result]
    for key, value in a_dictionary.items():
        if value > first:
            result = key
            first = value
    if first <= 0:
        return None
    return result
