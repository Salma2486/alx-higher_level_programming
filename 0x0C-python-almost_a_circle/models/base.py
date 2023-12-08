#!/usr/bin/python3
""" we5t wy5e  yw4rwy 454"""


class Base:
    """ro yjeori6y woriy6 twry """

    __nb_objects = 0

    def __init__(self, id=None):
        """rts ihyker oypkwry """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
