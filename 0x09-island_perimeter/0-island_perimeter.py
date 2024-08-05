#!/usr/bin/python3
""" ALX Interview - Island perimeter
"""


def island_perimter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                # Check UP
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check DOWN
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check LEFT
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check RIGHT
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1
    return perimeter