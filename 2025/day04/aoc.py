import os
from collections import defaultdict
import heapq
import copy
from functools import cache

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]

def in_grid(grid, r, c):
    shifts = ((1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1))
    n = 0
    for shift in shifts:
        coo = (r + shift[0], c + shift[1])
        if coo in grid and grid[coo] == "@":  # Add conditions
            n += 1
    return n < 4

def part_one():
    sums = 0
    grid = {}
    for r, line in enumerate(input()):
        for c, col in enumerate(line):
            grid[(r, c)] = col

    for coo, v in grid.items():
        r, c = coo
        if v == "@":
            if in_grid(grid, r, c):
                sums += 1
            
    print("Part 1: ", sums)
    assert(sums == 1543)


def part_two():
    sums = 0
    grid = {}
    for r, line in enumerate(input()):
        for c, col in enumerate(line):
            grid[(r, c)] = col

    while (True):
        n = 0
        for coo, v in grid.items():
            r, c = coo
            if v == "@":
                if in_grid(grid, r, c):
                    sums += 1
                    n += 1
                    grid[coo] = "."
        if not n:
            break

    print("Part 2: ", sums)
    assert(sums == 9038)


part_one()
part_two()