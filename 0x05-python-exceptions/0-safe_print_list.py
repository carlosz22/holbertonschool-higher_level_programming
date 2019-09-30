#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            real_printed += 1
        except:
            break
    print()
    return real_printed
