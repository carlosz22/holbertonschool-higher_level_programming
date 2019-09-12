#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hidden_list = dir(hidden_4)

    for element in hidden_list:
        if element[0] != '_' and element[1] != '_':
            print("{}".format(element))
