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
    sums = 0
    grid = {}
    for i, line in enumerate(input()):
        for j, c in enumerate(line):
            grid[(i, j)] = c
    maxx = i

    for coo, s in grid.items():
        if s == "O":
            ii = 1
            while True:
                x, y = coo
                if (x - ii, y) in grid and grid[(x - ii, y)] == ".":
                    grid[(x - ii, y)] = "O"
                    grid[(x - ii + 1, y)] = "."
                    ii += 1
                else:
                    break

    for coo, s in grid.items():
        if s == "O":
            sums += maxx - coo[0] + 1
    print("Part 1: ", sums)
    assert(sums == 109665)

def printer(grid):
    row = 0
    for coo, v in grid.items():
        r, c = coo
        if r != row:
            print()
            row = r
        print(v, end = "")

    print()
    print()

def part_two():
    sums = 0
    grid = {}
    for i, line in enumerate(input()):
        for j, c in enumerate(line):
            grid[(i, j)] = c
    maxx = i

    for hh in range(10000):
        # N
        for coo, s in grid.items():
            if s == "O":
                ii = 1
                while True:
                    x, y = coo
                    if (x - ii, y) in grid and grid[(x - ii, y)] == ".":
                        grid[(x - ii, y)] = "O"
                        grid[(x - ii + 1, y)] = "."
                        ii += 1
                    else:
                        break
        # W
        for coo, s in sorted(grid.items(), key=lambda item: item[0][1]):
            if s == "O":
                ii = 1
                while True:
                    x, y = coo
                    if (x, y - ii) in grid and grid[(x, y - ii)] == ".":
                        grid[(x, y - ii)] = "O"
                        grid[(x, y - ii + 1)] = "."
                        ii += 1
                    else:
                        break
        # S
        for coo, s in reversed(grid.items()):
            if s == "O":
                ii = 1
                while True:
                    x, y = coo
                    if (x + ii, y) in grid and grid[(x + ii, y)] == ".":
                        grid[(x + ii, y)] = "O"
                        grid[(x + ii - 1, y)] = "."
                        ii += 1
                    else:
                        break
        # E
        for coo, s in reversed(sorted(grid.items(), key=lambda item: item[0][1])):
            if s == "O":
                ii = 1
                while True:
                    x, y = coo
                    if (x, y + ii) in grid and grid[(x, y + ii)] == ".":
                        grid[(x, y + ii)] = "O"
                        grid[(x, y + ii - 1)] = "."
                        ii += 1
                    else:
                        break
        #printer(grid)
        sums = 0
        for coo, s in grid.items():
            if s == "O":
                sums += maxx - coo[0] + 1
        print("Part 2: ", hh, sums)


#part_one()
part_two()