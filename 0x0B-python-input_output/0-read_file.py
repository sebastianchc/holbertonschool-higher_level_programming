#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as myfile:
        print(myfile.read(), end='')
