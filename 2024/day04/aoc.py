import os
from collections import defaultdict

day_path = os.path.dirname(__file__)


def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]


def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]


def int_list(char_list):
    return [int(c) for c in char_list]


def part1(grid, row, col, dir):
    rd, cd = dir
    if (row, col) in grid and grid[(row, col)] == "X":
        row += rd
        col += cd
        if (row, col) in grid and grid[(row, col)] == "M":
            row += rd
            col += cd
            if (row, col) in grid and grid[(row, col)] == "A":
                row += rd
                col += cd
                if (row, col) in grid and grid[(row, col)] == "S":
                    return True
    return False


def part2(grid, row, col, dir):
    rd, cd = dir
    row_orig = row
    col_orig = col
    if (row, col) in grid and grid[(row, col)] == "M":
        row += rd
        col += cd
        if (row, col) in grid and grid[(row, col)] == "A":
            row += rd
            col += cd
            if (row, col) in grid and grid[(row, col)] == "S":
                if (row_orig, col) in grid and grid[(row_orig, col)] == "S":
                    if (row, col_orig) in grid and grid[(row, col_orig)] == "M":
                        return True
                if (row_orig, col) in grid and grid[(row_orig, col)] == "M":
                    if (row, col_orig) in grid and grid[(row, col_orig)] == "S":
                        return True
    return False


def part_one():
    sums = 0
    grid = {}
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c

    print(row, col)
    directions8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
    for r in range(row + 1):
        for c in range(col + 1):
            for dir in directions8:
                if part1(grid, c, r, dir):
                    sums += 1

    print("Part 1: ", sums)
    assert sums == 2447


def part_two():
    sums = 0
    grid = {}
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c

    dirs_diag = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for r in range(row + 1):
        for c in range(col + 1):
            for dir in dirs_diag:
                if part2(grid, c, r, dir):
                    sums += 1

    sums = int(sums / 2)
    print("Part 2: ", sums)
    assert sums == 1868


part_one()
part_two()
