"""Island Perimeter."""

from typing import List


def island_perimeter(grid: List) -> int:
    """
    Island perimeter.

    Args:
        grid (list): list of cells
    Returns:
        Returns int, the number of the perimeter.
    """
    if not grid:
        return 0

    perimeter: int = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check adjacent cells
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
