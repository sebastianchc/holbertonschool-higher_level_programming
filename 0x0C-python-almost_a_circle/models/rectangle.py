#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ area method """
        return self.width * self.height

    def display(self):
        """ display method """
        for line in range(self.y):
            print("")
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def update(self, *args, **kwargs):
        """ update method """
        if len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.width = args[arg]
                if arg == 2:
                    self.height = args[arg]
                if arg == 3:
                    self.x = args[arg]
                if arg == 4:
                    self.y = args[arg]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ to_dictionary method """
        dictionary = {"x": self.x, "y": self.y, "id": self.id,
                      "height": self.height, "width": self.width}
        return dictionary

    def __str__(self):
        """ __str__ method """
        string = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return string.format(self.id, self.x, self.y, self.width, self.height)
