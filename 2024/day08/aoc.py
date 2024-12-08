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


def part_one():
    grid = {}
    gridv = defaultdict(list)
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            if c != ".":
                gridv[c].append((row, col))
            grid[(row, col)] = c

    anti_grid = {}

    for sig, coos in gridv.items():
        for coo in coos:
            for coo2 in coos:
                if coo == coo2:
                    continue
                dr = coo[0] - coo2[0]
                dc = coo[1] - coo2[1]
                if (coo[0] + dr, coo[1] + dc) in grid:
                    anti_grid[(coo[0] + dr, coo[1] + dc)] = 1
                if (coo2[0] - dr, coo2[1] - dc) in grid:
                    anti_grid[(coo2[0] - dr, coo2[1] - dc)] = 1

    print("Part 1: ", len(anti_grid))
    assert len(anti_grid) == 371


def part_two():
    grid = {}
    gridv = defaultdict(list)
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            if c != ".":
                gridv[c].append((row, col))
            grid[(row, col)] = c

    anti_grid = {}

    for _, coos in gridv.items():
        for coo in coos:
            for coo2 in coos:
                if coo == coo2:
                    continue
                for i in range(0, 100):
                    dr = coo[0] - coo2[0]
                    dc = coo[1] - coo2[1]
                    dr *= i
                    dc *= i
                    if (coo[0] + dr, coo[1] + dc) in grid:
                        anti_grid[(coo[0] + dr, coo[1] + dc)] = 1
                    if (coo2[0] - dr, coo2[1] - dc) in grid:
                        anti_grid[(coo2[0] - dr, coo2[1] - dc)] = 1

    print("Part 2: ", len(anti_grid))
    assert len(anti_grid) == 1229


part_one()
part_two()
