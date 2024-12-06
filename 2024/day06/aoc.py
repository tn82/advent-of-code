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

def turn_righ(dr, dc):
    if dr == 0 and dc == 1:
        return 1, 0
    if dr == 0 and dc == -1:
        return -1, 0
    if dr == 1 and dc == 0:
        return 0, -1
    if dr == -1 and dc == 0:
        return 0, 1
    
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

    dr = -1
    dc = 0
    vis = set()
    vis.add((sr, sc))
    while True:
        if (sr+dr, sc+dc) not in grid:
            break
        if grid[(sr + dr, sc + dc)] == "#":
            dr, dc = turn_righ(dr, dc)
            continue
        sr += dr
        sc += dc
        vis.add((sr, sc))

    print("Part 1: ", len(vis))
    assert(len(vis) == 5129)

import copy 
def part_two():
    grido = {}
    sr = 0
    sc = 0
    for row, line in enumerate(input()):
        if not line:
            row -= 1
            continue
        for col, c in enumerate(line):
            grido[(row, col)] = c
            if c == "^":
                sro = row
                sco = col

    dro = -1
    dco = 0
    sums = 0
    for r in range(row+1):
        for c in range(col+1):
            if grido[(r, c)] == "#":
                continue
            grid = copy.copy(grido)
            grid[(r, c)] = "#"
            sr = sro
            sc = sco
            dr = dro
            dc = dco
            vis = set()
            vis.add((sr, sc, dr, dc))
            while True:
                if (sr+dr, sc+dc) not in grid:
                    break
                
                if grid[(sr + dr, sc + dc)] == "#":
                    dr, dc = turn_righ(dr, dc)
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

part_one()
part_two()