#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__ method """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to a JSON static method """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
