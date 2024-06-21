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
    ben_wins = 0
    maria_wins = 0

    n = max(nums)
    value_list = [True for i in range(1, n + 1)]
    value_list[0] = False
    for i, is_prime in enumerate(value_list, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            value_list[j - 1] = False

    for k, n in zip(range(x), nums):
        primes = len(list(filter(lambda x: x, value_list[0: n])))
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if ben_wins == maria_wins:
        return None
    if maria_wins > ben_wins:
        return 'Maria'
    return 'Ben'
