#!/usr/bin/python3
"""
This module provides one function add_integer(a, b=98).
"""

def add_integer(a, b=98):
    """
    Return the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b