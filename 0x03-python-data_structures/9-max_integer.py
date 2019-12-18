#!/usr/bin/python3
def max_integer(my_list=[]):
    max_in = my_list[0]
    if my_list:
        for integer in my_list:
            if integer > max_in:
                max_in = integer
        return max_in
    return None
