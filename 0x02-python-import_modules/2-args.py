#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 1
    argc = len(argv) - 1
    if len(argv) == 1:
        print("{} arguments." .format(argc))
    elif len(argv) == 2:
        print("{} argument:" .format(argc))
        print("{}: {}" .format(argc, argv[1]))
    else:
        print("{} arguments:" .format(argc))
        for argument in argv:
            print("{}: {}" .format(n, argument))
            n += 1
