#!/usr/bin/python3

"""
A method that determines if a given data set represents
a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Count the bytes left to process in a character to determine if it re
    presents a utf-8 encoding or not
    """
    bytes_rem = 0
    for byte in data:
        byte = byte & 0xFF

        if bytes_rem == 0:
            if (byte >> 5) == 0b110:
                bytes_rem = 1
            elif (byte >> 4) == 0b1110:
                bytes_rem = 2
            elif (byte >> 3) == 0b11110:
                bytes_rem = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_rem -= 1
    return bytes_rem == 0
