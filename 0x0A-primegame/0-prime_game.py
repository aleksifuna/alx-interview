#!/usr/bin/python3
"""
Module contains isWinner function
"""


def isWinner(x, nums):
    """
    computes and returns winner of most rounds
    """
    Maria = 0
    Ben = 0

    for n in nums:
        primes = SieveOfEratosthenes(n)
        if primes == 0:
            Ben += 1
        elif primes % 2 == 0:
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        return 'Maria'
    if Ben > Maria:
        return 'Ben'
    if Ben == Maria:
        return None


def SieveOfEratosthenes(n):
    """
    Counts the number of prime numbers upto including n
    """
    prime = [True for i in range(n + 1)]
    count = 0
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n + 1):
        if prime[p]:
            count += 1
    return count
