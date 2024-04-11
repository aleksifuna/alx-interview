#!/usr/bin/python3
""" This module contains a function pascal_triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing pascal's triangle of n
    """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result
