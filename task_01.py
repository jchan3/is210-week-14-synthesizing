#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def xfibo(count):
    """A function that returns a Fibonacci sequence up to count.

    Args:
        count (integer): The number of Fibonacci numbers to return.

    Returns:
        integer: A sequence of Fibonacci numbers.

    Examples:
        >>> for i in xfibo(5):
                print i
        0
        1
        1
        2
        3
    """
    iterations = 0
    last = 0
    cur = 1
    while iterations < count:
        yield last
        last, cur = cur, last + cur
        iterations += 1
