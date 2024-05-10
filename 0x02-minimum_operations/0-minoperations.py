#!/usr/bin/python3
""" min opeerations"""


def minOperations(n: int) -> int:
    """ minmum operations"""
    p = 2
    op = 0
    while n > 1:
        while n % p == 0:
            op += p
            n /= p
        p += 1
    return op
