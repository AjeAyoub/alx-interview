#!/usr/bin/python3
"""
Minimum  Operations
Given num n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file
Prototype: def minOperations(n)
Returns an integer
if n impossible to achieve, return 0
"""


def minOperations(n):
    """
    Function minOperations
    Returns  integer
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
