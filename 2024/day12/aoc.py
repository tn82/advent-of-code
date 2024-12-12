import os
from collections import defaultdict

day_path = os.path.dirname(__file__)


def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]


def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

# 2D grid area + perimeter
'''
AAAA
BBCD
BBCC
EEEC
'''
def dfs(grid, row, col, letter, visited):
    if (row, col) in visited or (row, col) not in grid or grid[(row, col)] != letter:
        return 0, 0

    visited.add((row, col))
    area = 1
    perimeter = 4

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        new_area, new_perimeter = dfs(grid, new_row, new_col, letter, visited)
        area += new_area
        perimeter += new_perimeter

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if (new_row, new_col) in grid and grid[(new_row, new_col)] == letter:
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
    assert sums == 1452678


def other(grid, letter, row, col):
    return (row, col) not in grid or grid[(row, col)] != letter

def is_corner(grid, letter, corners, row, col, dr, dc):
    key = tuple(
        sorted([(row, col), (row + dr, col), (row + dr, col + dc), (row, col + dc)])
    )
    if key in corners and not (
        not other(grid, letter, row + dr, col + dc)
        and other(grid, letter, row, col + dc)
        and other(grid, letter, row + dr, col)
    ):
        return False
    if other(grid, letter, row + dr, col) and other(grid, letter, row, col + dc):
        corners.add(key)
        return True
    if (
        not other(grid, letter, row + dr, col)
        and not other(grid, letter, row, col + dc)
        and other(grid, letter, row + dr, col + dc)
    ):
        corners.add(key)
        return True
    if (
        other(grid, letter, row + dr, col)
        and not other(grid, letter, row, col + dc)
        and not other(grid, letter, row + dr, col + dc)
    ):
        corners.add(key)
        return True


# 2D grid area + perimeter
'''
AAAA
BBCD
BBCC
EEEC
'''
def dfs_area_perimeter_only_count_corners(grid, row, col, letter, visited, corners):
    if (row, col) in visited or (row, col) not in grid or grid[(row, col)] != letter:
        return 0, 0

    visited.add((row, col))
    area = 1
    perimeter = 4

    perimeter = 0  # Start with 0, only add for edges between regions
    if is_corner(grid, letter, corners, row, col, 1, 1):
        perimeter += 1
    if is_corner(grid, letter, corners, row, col, 1, -1):
        perimeter += 1
    if is_corner(grid, letter, corners, row, col, -1, 1):
        perimeter += 1
    if is_corner(grid, letter, corners, row, col, -1, -1):
        perimeter += 1

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        new_area, new_perimeter = dfs_area_perimeter_only_count_corners(grid, new_row, new_col, letter, visited, corners)
        area += new_area
        perimeter += new_perimeter

    return area, perimeter


def part_two():
    sums = 0
    grid = {}
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c

    visited = set()

    for row in range(row + 1):
        for col in range(col + 1):
            if (row, col) not in visited:
                corners = set()
                letter = grid[(row, col)]
                area, perimeter = dfs_area_perimeter_only_count_corners(grid, row, col, letter, visited, corners)
                sums += area * perimeter

    print("Part 2: ", sums)
    assert sums == 873584


part_one()
part_two()
