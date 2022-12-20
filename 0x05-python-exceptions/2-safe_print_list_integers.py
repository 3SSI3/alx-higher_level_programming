#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
  count = 0
  for i in range (0, x):
    try:
      int(my_list[i])
    except (ValueError, TypeError):
      print(end='')
    else:
      count += 1
      print("{:d}".format(my_list[i]), end='')
  print()
  return count
