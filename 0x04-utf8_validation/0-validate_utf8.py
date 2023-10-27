#!/usr/bin/env python3
"""This module has the function validUTF8"""


def count_leading_ones(byte):
    """
    counts the leading bytes
    Args:
        byte (byte): stream of bits
    Return:
        the number of leading bytes
    """
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8


def validUTF8(data):
    """
    checks if a specified data set represents a valid UTF-8 encoding
    Args:
        data [list]: a list of intehgers
    Return:
        (bool) : True if the encoding is UTF-8 and False if not
    """
    data = iter(data)
    for l_byte in data:
        leading_byte = count_leading_ones(l_byte)
        if leading_byte in [1, 7, 8]:
            return False
        for _ in range(leading_byte - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or trailing_byte >> 6 != 0b10:
                return False
    return True
