#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for item1, item2 in a_dictionary.items():
        new_dictionary[item1] = item2 * 2
    return new_dictionary
