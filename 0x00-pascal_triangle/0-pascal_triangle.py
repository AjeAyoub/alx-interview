#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    q = []
    if n <= 0:
        return q
    q = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(q[i - 1]) - 1):
            curr = q[i - 1]
            temp.append(q[i - 1][j] + q[i - 1][j + 1])
        temp.append(1)
        q.append(temp)
    return q
