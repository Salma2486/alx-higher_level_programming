#!/usr/bin/python3
"""ohirt ijoer yijojre yoije"""


class BaseGeometry:
    """jlk skl snetgo estgoi j es"""

    def area(self):
        """i osietguh oiergoihser oig"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ jkesgt jhlesthk ewori hio er"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """oi wetsiohewroi we5yioj;e qrt"""

    def __init__(self, width, height):
        """tijose goijest rjip ew"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
