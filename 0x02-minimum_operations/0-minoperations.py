#!/usr/bin/python3
"""Minimum Operations challenge"""


def minOperations(n):
    """calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
        """
    if n <= 1:
        return

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
