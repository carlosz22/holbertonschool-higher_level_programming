#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        abs_last_digit = ((number * -1) % 10)
    else:
        abs_last_digit = number % 10

    print("{}".format(abs_last_digit), end="")
    return abs_last_digit
