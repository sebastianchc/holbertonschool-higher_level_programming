#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.width = args[arg]
                if arg == 2:
                    self.x = args[arg]
                if arg == 3:
                    self.y = args[arg]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ to_dictionary method """
        dictionary = {"x": self.x, "y": self.y, "id": self.id,
                      "size": self.width}
        return dictionary

    def __str__(self):
        """ __str__ method """
        string = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return string.format(self.id, self.x, self.y, self.size)
