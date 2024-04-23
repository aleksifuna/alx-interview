#!/usr/bin/python3
"""
Supplies one function minOperations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
