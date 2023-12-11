#!/usr/bin/python3
"""ri lsytilrjd hylos htr"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """oijrs tyoijh dryio duyr"""

    def __init__(self, size, x=0, y=0, id=None):
        """oihrs tyluhrsoi ytols rt"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ ey5althje asyo5i;js ryt"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ rht wtyh yher"""
        return self.width

    @size.setter
    def size(self, value):
        """ wrhe yrhe yhr"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ib ui hy uhi8h8 8u"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
