import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def in_grid(grid, r, c):
    shifts = ((1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1))
    for shift in shifts:
        coo = (r + shift[0], c + shift[1])
        if coo in grid and not grid[coo].isdigit() and not grid[coo] == ".":
            return True
    return False

def is_gear(grid, r, c):
    shifts = ((1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1))
    for shift in shifts:
        coo = (r + shift[0], c + shift[1])
        if coo in grid and not grid[coo].isdigit() and grid[coo] == "*":
            return True, coo
    return False, (None, None)

def zero_out(grid, r, c):
    grid[(r, c)] = "."
    for i in range(1, 3):
        if (r, c + i) in grid and grid[(r, c + i)].isdigit():
            grid[(r, c + i)] = "."
        else:
            return
    return

def part_one():
    sums = 0
    grid = {}
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c
    for key, val in grid.items():
        r, c = key
        dig = ""
        ok = False
        if val.isdigit():
            ok = in_grid(grid, r, c)
            dig += val
            for i in range(1, 3):
                if (r, c + i) in grid and grid[(r, c + i)].isdigit():
                    dig += grid[(r, c + i)]
                    ok = ok or in_grid(grid, r, c + i)
                else:
                    break
        if ok:
            sums += int(dig)
            zero_out(grid, r, c)

    print("Part 1: ", sums)
    assert(sums == 525911)

def part_two():
    sums = 0
    grid = {}
    gear_grid = defaultdict(list)
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c
    for key, val in grid.items():
        r, c = key
        dig = ""
        ok = False
        gear = ()
        if val.isdigit():
            ok, gear = is_gear(grid, r, c)
            dig += val
            for i in range(1, 3):
                if (r, c + i) in grid and grid[(r, c + i)].isdigit():
                    dig += grid[(r, c + i)]
                    ok1, gear1 = is_gear(grid, r, c + i)
                    ok = ok or ok1
                    if ok1:
                        gear = gear1
                else:
                    break
        if ok:
            gear_grid[gear].append(int(dig))
            zero_out(grid, r, c)
    
    for _, g1 in gear_grid.items():
        if len(g1) == 2:
            sums+=g1[0] * g1[1]

    print("Part 2: ", sums)
    assert(sums == 75805607)

part_one()
part_two()