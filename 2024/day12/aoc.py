import os
from collections import defaultdict
from scipy.spatial import ConvexHull

day_path = os.path.dirname(__file__)


def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]


def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def dfs(grid, row, col, letter, visited):
    if ((row, col) in visited or (row, col) not in grid or grid[(row, col)] != letter):
        return 0, 0

    visited.add((row, col))
    area = 1
    perimeter = 4

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        new_area, new_perimeter = dfs(grid, new_row, new_col, letter, visited)
        area += new_area
        perimeter += new_perimeter

        if ((new_row, new_col) in grid and grid[(new_row, new_col)] == letter):
            perimeter -= 1  # Adjust perimeter for shared edges

    return area, perimeter
    
def part_one():
    sums = 0
    grid = {}
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c

    visited = set()
    for row in range(row + 1):
        for col in range(col + 1):
            if (row, col) not in visited:
                letter = grid[(row, col)]
                area, perimeter = dfs(grid, row, col, letter, visited)
                sums += area * perimeter

    print("Part 1: ", sums)
    return sums


def part_two():
    sums = 0
    for i, line in enumerate(input()):
        sums += int(line)

    print("Part 2: ", sums)
    # assert(sums == 0)

part_one()
# part_two()
