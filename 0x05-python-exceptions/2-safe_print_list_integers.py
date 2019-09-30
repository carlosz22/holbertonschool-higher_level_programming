#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_printed = 0
    for i in range(x + 1):
        try:
            print("{:d}".format(my_list[i]), end='')
            int_printed += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return int_printed
