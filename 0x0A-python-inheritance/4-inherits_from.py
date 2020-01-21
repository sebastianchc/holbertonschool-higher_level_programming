#!/usr/bin/python3
def inherits_from(obj, a_class):
    return False if type(obj) == a_class else isinstance(obj, a_class)
