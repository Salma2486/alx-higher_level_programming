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

    def update(self, *args, **kwargs):
        """ijijjk ijjk"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
