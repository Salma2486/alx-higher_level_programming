#!/usr/bin/python3
"""ri lsytilrjd hylos htr"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """oijrs tyoijh dryio duyr"""

    def __init__(self, size, x=0, y=0, id=None):
        """oihrs tyluhrsoi ytols rt"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ rht wtyh yher"""
        return self.width

    @size.setter
    def size(self, value):
        """ wrhe yrhe yhr"""
        self.width = value
        self.height = value

    def __str__(self):
        """ ey5althje asyo5i;js ryt"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
