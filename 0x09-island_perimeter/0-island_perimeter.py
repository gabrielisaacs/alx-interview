#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where:
            - 0 represents water
            - 1 represents land

    Returns:
        int: The perimeter of the island

    Note:
        - The grid is rectangular, width and height don't exceed 100
        - The grid is completely surrounded by water
        - There is only one island (or nothing)
        - The island doesn't have "lakes"
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4
                # Check and subtract for adjacent land cells
                # Check cell above if it exists
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # Check cell to the left if it exists
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
