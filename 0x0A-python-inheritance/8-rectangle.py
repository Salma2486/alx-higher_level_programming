#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


class BaseGeometry:
    """jse gr ijlher  lhuser o ;;hg"""

    def area(self):
        """ker goi raeohi"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """jke rhu oaer uhor e"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
