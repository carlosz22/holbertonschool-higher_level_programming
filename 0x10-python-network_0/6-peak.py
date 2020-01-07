#!/usr/bin/python3
"""
Algorithm to find peak element in an unsorted array
"""


def find_peak(list_of_integers):
    """
    Algorithm to find peak element in an unsorted array
    """

    if not list_of_integers:
        return None

    middle = int((len(list_of_integers) - 1) / 2)

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]

    if list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle + 1:])
    else:
        return find_peak(list_of_integers[:middle + 1])
