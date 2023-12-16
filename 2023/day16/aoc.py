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

def grid_printer(grid):
    row = 0
    for coo, v in grid.items():
        r, c = coo
        if r != row:
            print()
            row = r
        print(v, end = "")

    print()
    print()

def part_one():
    sums = 0
    grid = {}
    for i, line in enumerate(input()):
        for j, v in enumerate(line):
            grid[(i, j)] = v

    litt = {}
    q = [("R", 0, 0)]
    while q:
        d, x, y = q.pop()
        if (x, y) not in grid:
            continue
        if (x, y, d) in litt:
            continue
        litt[(x, y, d)] = 1
        val = grid[(x, y)]
        if d == "L":
            if val == ".":
                q.append((d, x, y - 1))
            elif val == "-":
                q.append((d, x, y - 1))
            elif val == "/":
                q.append(("D", x + 1, y))
            elif val == "T":
                q.append(("U", x - 1, y))
            elif val == "|":
                q.append(("D", x + 1, y))
                q.append(("U", x - 1, y))

        elif d == "R":
            if val == ".":
                q.append((d, x, y + 1))
            elif val == "-":
                q.append((d, x, y + 1))
            elif val == "/":
                q.append(("U", x - 1, y))
            elif val == "T":
                q.append(("D", x + 1, y))
            elif val == "|":
                q.append(("D", x + 1, y))
                q.append(("U", x - 1, y))

        elif d == "D":
            if val == ".":
                q.append((d, x + 1, y))
            elif val == "-":
                q.append(("L", x, y - 1))
                q.append(("R", x, y + 1))
            elif val == "/":
                q.append(("L", x, y - 1))
            elif val == "T":
                q.append(("R", x, y + 1))
            elif val == "|":
                q.append((d, x + 1, y))

        elif d == "U":
            if val == ".":
                q.append((d, x - 1, y))
            elif val == "-":
                q.append(("L", x, y - 1))
                q.append(("R", x, y + 1))
            elif val == "/":
                q.append(("R", x, y + 1))
            elif val == "T":
                q.append(("L", x, y - 1))
            elif val == "|":
                q.append((d, x - 1, y))


    litt_u = {}
    for k, v in litt.items():
        litt_u[(k[0], k[1])] = 1
    print("Part 1: ", sum(litt_u.values()))
    #assert(sums == 7185)


def litter(grid, sx, sy, d):
    litt = {}
    q = [(d, sx, sy)]
    while q:
        d, x, y = q.pop()
        if (x, y) not in grid:
            continue
        if (x, y, d) in litt:
            continue
        litt[(x, y, d)] = 1
        val = grid[(x, y)]
        if d == "L":
            if val == ".":
                q.append((d, x, y - 1))
            elif val == "-":
                q.append((d, x, y - 1))
            elif val == "/":
                q.append(("D", x + 1, y))
            elif val == "T":
                q.append(("U", x - 1, y))
            elif val == "|":
                q.append(("D", x + 1, y))
                q.append(("U", x - 1, y))

        elif d == "R":
            if val == ".":
                q.append((d, x, y + 1))
            elif val == "-":
                q.append((d, x, y + 1))
            elif val == "/":
                q.append(("U", x - 1, y))
            elif val == "T":
                q.append(("D", x + 1, y))
            elif val == "|":
                q.append(("D", x + 1, y))
                q.append(("U", x - 1, y))

        elif d == "D":
            if val == ".":
                q.append((d, x + 1, y))
            elif val == "-":
                q.append(("L", x, y - 1))
                q.append(("R", x, y + 1))
            elif val == "/":
                q.append(("L", x, y - 1))
            elif val == "T":
                q.append(("R", x, y + 1))
            elif val == "|":
                q.append((d, x + 1, y))

        elif d == "U":
            if val == ".":
                q.append((d, x - 1, y))
            elif val == "-":
                q.append(("L", x, y - 1))
                q.append(("R", x, y + 1))
            elif val == "/":
                q.append(("R", x, y + 1))
            elif val == "T":
                q.append(("L", x, y - 1))
            elif val == "|":
                q.append((d, x - 1, y))


    litt_u = {}
    for k, v in litt.items():
        litt_u[(k[0], k[1])] = 1
    return sum(litt_u.values())

def part_two():
    grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate(input()):
        for j, v in enumerate(line):
            grid[(i, j)] = v
            if i > xmax:
                xmax = i
            if j > ymax:
                ymax = j

    litt_max = 0
    for sx in range(xmax):
        m = litter(grid, sx, 0, "L")
        if m > litt_max:
            litt_max = m
        m = litter(grid, sx, ymax, "R")
        if m > litt_max:
            litt_max = m
    for sy in range(ymax):
        m = litter(grid, 0, sy, "D")
        if m > litt_max:
            litt_max = m
        m = litter(grid, xmax, sy, "U")
        if m > litt_max:
            litt_max = m
    print("Part 2: ", litt_max)
    #assert(sums == 7185)


#part_one()
part_two()