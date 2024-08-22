#!/usr/bin/python3
"""Given a pile of coins of different values, determine the fewest number 
of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # Sort coins to help with greedy approach or optimized iterations
    coins.sort(reverse=True)

    # Initialize the DP table with an arbitrarily large number (total + 1)
    # Since total + 1 is greater than any possible minimum, it’s safe.
    table = [total + 1] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                continue
            table[i] = min(table[i], table[i - coin] + 1)

    return table[total] if table[total] <= total else -1