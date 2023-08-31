#!/usr/bin/python3
"""Island Perimeter."""

from typing import List


def island_perimeter(grid: List) -> int:
    """
    Island perimeter.

    Args:
        grid (list): 2D list containing 0(water) or 1(land)
    Returns:
        Returns int, the number of the perimeter of the island.
    """
    perimeter: int = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    perimeter += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    perimeter += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    perimeter += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    perimeter += 1

    return perimeter
