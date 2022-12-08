#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    v = 0
    for tup in my_list:
        a += tup[0] * tup [1]
        v += tup[1]
        return float(a / v)
