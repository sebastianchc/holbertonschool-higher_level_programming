#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list1 = set(set_1)
    list2 = set(set_2)
    return list1 ^ list2
