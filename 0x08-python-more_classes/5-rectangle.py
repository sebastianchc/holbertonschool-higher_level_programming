#!/usr/bin/python3
class Rectangle:

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ""
        if not self.__width or not self.__height:
            return string
        else:
            for row in range(self.__height):
                string += "#" * self.__width
                if row != self.__height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        return "Rectangle(" + str(self.__width)\
            + ", " + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
