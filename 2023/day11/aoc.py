import copy
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

def gal_pos(grid, gal):
    for r, line in enumerate(grid):
        for c, v in enumerate(line):
            if grid[r][c] == str(gal):
                return (r, c)
            
def part_one():
    sums = 0
    grid = []
    for r, line in enumerate(input()):
        grid.append([])
        for c in line:
            grid[r].append(c)
    i = 0
    while True:
        if i > len(grid) - 1:
            break
        r = grid[i]
        if "#" in r:
            i += 1
            continue
        grid.insert(i, copy.copy(r))
        i += 2
    j = 0
    while True:
        if j > len(grid[0]) - 1:
            break
        any_gal = False
        for i, r in enumerate(grid):
            if grid[i][j] == "#":
                any_gal = True
        if not any_gal:
            l = len(grid)
            for i in range(l):
                grid[i].insert(j, ".")
            j += 2
        else:
            j += 1
    gal = 0
    for r, line in enumerate(grid):
        for c, v in enumerate(line):
            if grid[r][c] == "#":
                grid[r][c] = str(gal)
                gal += 1

    for g in range(gal):
        gr, gc = gal_pos(grid, str(g))
        for gt in range(gal):
            if g == gt:
                continue
            gtr, gtc = gal_pos(grid, str(gt))
            sums += abs(gtr - gr) + abs(gtc - gc)


    print("Part 1: ", sums/2)
    #assert(sums == 10292708)


def part_two():
    sums = 0
    grid = []
    empties_r = []
    for r, line in enumerate(input()):
        grid.append([])
        for c in line:
            grid[r].append(c)
        if "#" not in line:
            empties_r.append(r)
    empties_c = []
    j = 0
    while True:
        if j > len(grid[0]) - 1:
            break
        any_gal = False
        for i, r in enumerate(grid):
            if grid[i][j] == "#":
                any_gal = True
        if not any_gal:
            empties_c.append(j)
        j += 1


    gal = 0
    for r, line in enumerate(grid):
        for c, v in enumerate(line):
            if grid[r][c] == "#":
                grid[r][c] = str(gal)
                gal += 1

    for g in range(gal):
        gr, gc = gal_pos(grid, str(g))
        for gt in range(gal):
            if g == gt:
                continue
            gtr, gtc = gal_pos(grid, str(gt))
            sums += abs(gtr - gr) + abs(gtc - gc)
            for e in empties_r:
                if e > min(gr, gtr) and e < max(gr, gtr):
                    sums += 999999
            for e in empties_c:
                if e > min(gc, gtc) and e < max(gc, gtc):
                    sums += 999999


    print("Part 2: ", sums/2)


#part_one()
part_two()