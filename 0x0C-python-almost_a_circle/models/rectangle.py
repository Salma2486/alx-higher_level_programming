#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
from models.base import Base


class Rectangle(Base):
    """ rydh dut edru duyt"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ 6ue5 7yujrt 7ujrt """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """oijki uhi"""
        return self.__width

    @width.setter
    def width(self, value):
        """ui hi gu igu"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ilj yui tiyg"""
        return self.__height

    @height.setter
    def height(self, value):
        """uoh 7uig yu"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """iuh ygi ygyuf"""
        return self.__x

    @x.setter
    def x(self, value):
        """oiuj yoh gyui"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """uih igu 7guy guy"""
        return self.__y

    @y.setter
    def y(self, value):
        """97 7yi g7oog8 y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ yw4r4 e56u u65we u5e"""
        return self.width * self.height

    def display(self):
        """ erh eu5e 5u"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """ wth4joiw hyropkw rh"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ wrytw y6re y6r"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
