#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ validUTF8 """
    byte = 0

    for i in data:
        if byte == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte = 1
            elif i >> 4 == 0b1110:
                byte = 2
            elif i >> 3 == 0b11110:
                byte = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte -= 1
    return byte == 0
