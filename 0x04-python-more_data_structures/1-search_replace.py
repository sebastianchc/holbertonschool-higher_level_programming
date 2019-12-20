#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = [replace if integer == search else integer for integer in my_list]
    return n_list
