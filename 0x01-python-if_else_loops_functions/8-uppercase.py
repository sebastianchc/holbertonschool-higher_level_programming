#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        mayus = ord(letter)
        if mayus > 96 and mayus < 123:
            mayus = ord(letter) - 32
        print("{}" .format(chr(mayus)), end='')
    print("")
