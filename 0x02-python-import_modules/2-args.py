#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 1
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
    else:
        print("{} arguments:" .format(len(argv)))
    for argument in argv:
        print("{}: {}" .format(n, argument))
        n += 1
