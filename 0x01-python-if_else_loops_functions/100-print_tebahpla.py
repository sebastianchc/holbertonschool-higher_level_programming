#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    if alphabet % 2:
        alphabet -= 32
    print("{}" .format(chr(alphabet)), end='')
