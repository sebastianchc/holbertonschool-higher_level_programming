#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if not self.width or not self.height:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        string = ""
        if not self.width or not self.height:
            return string
        else:
            for row in range(self.height):
                string += str(self.print_symbol) * self.width
                if row != self.height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_1) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
