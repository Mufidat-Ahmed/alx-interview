#!/usr/bin/python3
"""A function that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """grid is a list of list of integer"""

    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check for adjacent land cells to the right
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

                # Check for adjacent land cells below
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter
