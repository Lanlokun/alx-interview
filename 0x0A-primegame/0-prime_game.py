#!/usr/bin/env python3
"""Prime Game"""


def isWinner(x, nums):
    """Returns: name of the player that won the most rounds"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for _ in range(n + 1)]
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] is True:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve = [i for i in range(n + 1) if sieve[i] is True]
    c = 0
    for n in nums:
        if n in sieve:
            c += 1
    if c % 2 == 0:
        return "Maria"
    return "Ben"
