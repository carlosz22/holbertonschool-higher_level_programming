#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    total_weight = 0
    total_mul = 0
    for element in my_list:
        total_mul += (element[0] * element[1])
        total_weight += element[1]
    return total_mul / total_weight
