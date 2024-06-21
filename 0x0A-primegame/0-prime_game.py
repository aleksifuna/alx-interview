#!/usr/bin/python3
"""
Module contains isWinner function
"""


def isWinner(x, nums):
    """
    computes and returns winner of most rounds
    """
    if x < 1 or not nums:
        return None
    if x != len(nums):
        return None
    if not isinstance(nums, list):
        return None
    Maria = 0
    Ben = 0
    value_list = SieveOfEratosthenes(max(nums))
    for _, n in zip(range(x), nums):
        primes = len(list(filter(lambda x: x, value_list[2: n])))
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
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return prime
