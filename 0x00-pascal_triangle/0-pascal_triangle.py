#!/usr/bin/python3
"""alx interview 0x00"""


def pascal_triangle(n):
    """return pascal trinagle of n"""
    p = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            p.append([1])
        else:
            c = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    c.append(1)
                else:
                    c.append(p[i - 1][j - 1] + p[i - 1][j])

            p.append(c)

    return (p)
