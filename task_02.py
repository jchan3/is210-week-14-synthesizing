#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import task_01


def fibo(count):
    """A function that returns a Fibonacci sequence up to count.

    Args:
        count (integer): The total number of Fibonacci numbers to return.

    Returns:
        list: A list of Fibonacci numbers.

    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
