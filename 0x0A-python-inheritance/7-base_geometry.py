#!/usr/bin/python3
"""ioj ywijorysiotjrsy """


class BaseGeometry:
    """jksrt hhlsrt ihlkserykjtg o"""

    def area(self):
        """hijsdktghj ksdg fatg """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """soiruthjiosrthop,o  h toijst arht"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
