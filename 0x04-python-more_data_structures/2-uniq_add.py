#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set(my_list)
    res = 0
    for i in uniq_int:
        res += i
    return res
