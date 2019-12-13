#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) < 2:
        print("{}" .format(len(argv) - 1))
    else:
        n = int(argv[1])
        for numbers in range(2, len(argv)):
            n += int(argv[numbers])
        print("{}" .format(n))
