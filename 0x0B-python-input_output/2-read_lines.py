#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as myfile:
        print(myfile.readlines(nb_lines))
