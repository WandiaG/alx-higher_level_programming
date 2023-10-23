#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.
    You have to use "{:d}".format() to print as integer.
    """
    count = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print(my_list[item], end='')
            except IndexError:
                break
        else:
            continue
        count += 1
    print()
    return count
