#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for item1, item2 in sorted(a_dictionary.items()):
        print("{}: {}" .format(item1, item2))
