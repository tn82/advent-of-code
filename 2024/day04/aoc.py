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


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def se(grid, row, col, dir):
    row1 = row
    col1 = col
    rd, cd = dir
    if (row1, col1) in grid and grid[(row1, col1)] == "X":
        row1 += rd
        col1 += cd
        if (row1, col1) in grid and grid[(row1, col1)] == "M":
            row1 += rd
            col1 += cd
            if (row1, col1) in grid and grid[(row1, col1)] == "A":
                row1 += rd
                col1 += cd
                if (row1, col1) in grid and grid[(row1, col1)] == "S":
                    return True
    return False

def part_one():
    sums = 0
    grid = {}
    cols = 0
    rows = 0
    for row, line in enumerate(test()):
        for col, c in enumerate(line):
            grid[(row, col)] = c
            if row > rows:
                rows = row
            if col > cols:
                cols = col

    xmas = "XMAS"
    for row in range(rows+1):
        for col in range(cols+1):
            for dir in dirs:
                if se(grid, col, row, dir):
                    sums += 1

    print("Part 1: ", sums)
    # assert(sums == 0)


def part_two():
    sums = 0
    for i, line in enumerate(test()):
        sums += int(line)

    print("Part 2: ", sums)
    # assert(sums == 0)


part_one()
# part_two()
