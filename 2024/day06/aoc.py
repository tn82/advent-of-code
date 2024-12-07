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


def rotate_90_degrees_clockwise(x, y):
    return (y, -x)


def visited(sr, sc, grid):
    dr = -1
    dc = 0
    vis = set()
    vis.add((sr, sc))
    while True:
        if (sr + dr, sc + dc) not in grid:
            break
        if grid[(sr + dr, sc + dc)] == "#":
            dr, dc = rotate_90_degrees_clockwise(dr, dc)
            continue
        sr += dr
        sc += dc
        vis.add((sr, sc))
    return vis

def part_one():
    grid = {}
    sr = 0
    sc = 0
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c
            if c == "^":
                sr = row
                sc = col

    vis = visited(sr, sc, grid)

    print("Part 1: ", len(vis))
    assert len(vis) == 5129


def part_two():
    grid = {}
    sr = 0
    sc = 0
    for row, line in enumerate(input()):
        if not line:
            row -= 1
            continue
        for col, c in enumerate(line):
            grid[(row, col)] = c
            if c == "^":
                sro = row
                sco = col

    vis2 = visited(sro, sco, grid)
    sums = 0
    for r, c in vis2: # Add one wall on every distinct positions from part1
        if grid[(r, c)] == "#":
            continue
        sr, sc, dr, dc = sro, sco, -1, 0
        vis = set()
        vis.add((sr, sc, dr, dc))
        while True:
            if (sr + dr, sc + dc) not in grid:
                break
            if grid[(sr + dr, sc + dc)] == "#" or (sr + dr, sc + dc) == (r, c):
                dr, dc = rotate_90_degrees_clockwise(dr, dc)
                if (sr, sc, dr, dc) in vis:
                    sums += 1
                    break
                continue
            sr += dr
            sc += dc

            if (sr, sc, dr, dc) in vis:
                sums += 1
                break
            vis.add((sr, sc, dr, dc))

    print("Part 2: ", sums)
    assert sums == 1888


part_one()
part_two()
