#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 1
    if len(argv) == 0:
        print("{} arguments." .format(len(argv)))
    elif len(argv) == 1:
        print("{} argument:" .format(len(argv)))
    else:
        print("{} arguments:" .format(len(argv)))
    for argument in argv:
        print("{}: {}" .format(n, argument))
        n += 1
