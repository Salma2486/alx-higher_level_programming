#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Parameters:
    - text (str): The input text.

    Raises:
    TypeError: If text is not a string.

    """
        if not isinstance(text, str):
            raise TypeError("text must be a string")
    line = []
    for i in text:
        line.append(i)
        if i == '.' or i == '?' or i == ':':
            print(''.join(line))
            print()
            line = []
    if line:
        print(''.join(line))
