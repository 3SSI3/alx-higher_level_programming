#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    result = 0
    for i in range(0, x):
        try:
            my_list[i]
        except IndexError:
            print(end='')
        else:
            result += 1
            print(my_list[i], end='')
    print()
    return result
