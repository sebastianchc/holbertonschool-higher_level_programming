#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = dict.fromkeys(my_list)
    result = 0
    for integer in new_list:
        result += integer
    return result
