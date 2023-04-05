#!/usr/bin/python3
"Finds a peak in a list of unsorted integers"

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    capacity = len(list_of_integers)
    mid = capacity
    midd = capacity // 2

    while True:
        mid = mid // 2
        if (midd < capacity -1 and 
                list_of_integers[mid] < list_of_integers[midd + 1]):
            if mid // 2 == 0:
                mid = 2
            midd = midd + mid // 2
        elif mid > 0 and list_of_integers[mid] < list_of_integers[midd - 1]:
            if mid // 2 == 0:
                mid = 2
            midd = midd - mid // 2
        else:
            return list_of_integers[midd]
