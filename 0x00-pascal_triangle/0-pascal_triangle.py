#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's Triangle up to n rows."""
    if n <= 0:
        return []

    result = []

    for i in range(n):
        # Initialize a new row with 1's at the first and last positions
        new_row = [1] * (i + 1)

        # Fill in the interior values of the row
        for j in range(1, i):
            new_row[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(new_row)

    return result
