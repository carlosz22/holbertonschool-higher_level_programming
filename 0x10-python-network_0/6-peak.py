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

    start = 0
    end = len(list_of_integers) - 1
    middle = int(end / 2)
    arr = list_of_integers[:]

    if len(list_of_integers) == 1:
        return arr[0]
    elif len(list_of_integers) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]

    if arr[middle] < arr[middle + 1]:
        return find_peak(arr[middle + 1:])
    else:
        return find_peak(arr[:middle + 1])
