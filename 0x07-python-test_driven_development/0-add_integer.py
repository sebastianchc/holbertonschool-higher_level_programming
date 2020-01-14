#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that add 2 integers, a y b.
    If a or b aren't int or float, a TypeError
    is raised"""
    if type(a) in [int, float]:
        x = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) in [int, float]:
        y = int(b)
    else:
        raise TypeError("b must be an integer")
    return x + y
