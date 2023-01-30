#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialiazes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if not self.width or not self.height:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Returns a string rep of the rectangle"""
        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]
