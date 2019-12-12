#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 1
    if len(argv) == 1:
        print("{} arguments." .format(len(argv)))
    elif len(argv) == 2:
        print("{} argument:" .format(len(argv)))
        print("{}: {}" .format(n, argv[1]))
    else:
        print("{} arguments:" .format(len(argv)))
        for argument in argv:
            print("{}: {}" .format(n, argument))
            n += 1
