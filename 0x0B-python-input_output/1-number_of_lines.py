#!/usr/bin/python3
def number_of_lines(filename=""):
    num_lines = 0
    with open(filename, 'r') as myfile:
        return len(myfile.readlines())
