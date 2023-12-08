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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

