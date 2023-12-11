import copy
import os

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def gal_pos(grid, gal):
    for r, line in enumerate(grid):
        for c, v in enumerate(line):
            if grid[r][c] == str(gal):
                return (r, c)

def aoc(space_addon):
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
    for ci, _ in enumerate(grid[0]):
        any_gal = False
        for i, r in enumerate(grid):
            if grid[i][ci] == "#":
                any_gal = True
        if not any_gal:
            empties_c.append(ci)
    
    gal = 0
    for r, line in enumerate(grid):
        for c, v in enumerate(line):
            if grid[r][c] == "#":
                grid[r][c] = str(gal)
                gal += 1

    for g in range(gal):
        gr, gc = gal_pos(grid, str(g))
        for gt in range(g + 1, gal):
            gtr, gtc = gal_pos(grid, str(gt))
            sums += abs(gtr - gr) + abs(gtc - gc)
            for e in empties_r:
                if e > min(gr, gtr) and e < max(gr, gtr):
                    sums += space_addon
            for e in empties_c:
                if e > min(gc, gtc) and e < max(gc, gtc):
                    sums += space_addon

    return int(sums)

part1 = aoc(1)
print("Part 1: ", part1)
assert (part1 == 10292708)

part2 = aoc(1000000 - 1)
print("Part 2: ", part2)
assert (part2 == 790194712336)
