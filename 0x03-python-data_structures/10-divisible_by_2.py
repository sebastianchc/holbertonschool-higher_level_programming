#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_list = [True if integer % 2 == 0 else False for integer in my_list]
    return mult_list
