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

def part_one():
    sums = 0
    grid = {}
    sr, sc = 0, 0
    for r, line in enumerate(input()):
        for c, col in enumerate(line):
            grid[(r, c)] = col
            if col == "S":
                sr, sc = r, c

    beams = set()
    beams.add((sr, sc))
    splits = set()
    ok = True
    while ok:
        beams_copy = copy.copy(beams)
        for br, bc in beams_copy:
            down = (br + 1, bc)
            if down not in grid:
                ok = False
                break
            if grid[down] == ".":
                beams.add(down)
            else:
                beams.add((br + 1, bc + 1))
                beams.add((br + 1, bc - 1))
                splits.add(down)

    

    sums = len(splits)

    print("Part 1: ", sums)
    assert(sums == 1533)


def part_two():
    sums = 1
    grid = {}
    sr, sc = 0, 0
    rmax = 0
    cmax = 0
    for r, line in enumerate(input()):
        for c, col in enumerate(line):
            grid[(r, c)] = col
            if col == "S":
                sr, sc = r, c
            if r > rmax:
                rmax = r
            if c > cmax:
                cmax = c


    splits = [0] * (cmax + 1)
    splits[sc] = 1
    for r in range(rmax):
        splits_next = [0] * (cmax + 1)
        for c, s in enumerate(splits):
            down = (r + 1, c)
            if grid[down] == ".":
                splits_next[c] += splits[c]
            else:
                splits_next[c - 1] += splits[c]
                splits_next[c + 1] += splits[c]
        splits = splits_next

    sums = sum(splits)

    print("Part 2: ", sums)
    assert(sums == 10733529153890)


part_one()
part_two()