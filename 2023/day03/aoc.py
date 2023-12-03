import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def is_ok(grid, r, c):
    k = (r - 1, c)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    k = (r + 1, c)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    k = (r, c - 1)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    k = (r, c + 1)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    k = (r - 1, c - 1)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    k = (r + 1, c + 1)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    k = (r + 1, c - 1)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    k = (r - 1, c + 1)
    if k in grid and not grid[k].isdigit() and not grid[k] == ".":
        return True
    return False

def part_one():
    sums = 0
    grid = {}
    syms = ("*", "*")
    for row, line in enumerate(input()):
        for col, c in enumerate(line):
            grid[(row, col)] = c
    for key, val in grid.items():
        r, c = key
        dig = ""
        ok = False
        if val.isdigit():
            ok = is_ok(grid, r, c)
            dig += val
            for i in range(1, 5):
                if (r, c + i) in grid and grid[(r, c + i)].isdigit():
                    dig += grid[(r, c + i)]
                    ok = ok or is_ok(grid, r, c + i)
                else:
                    break
        if ok:
            sums += int(dig)
            grid[(r, c)] = "."
            for i in range(1, 5):
                if (r, c + i) in grid and grid[(r, c + i)].isdigit():
                    grid[(r, c + i)] = "."
                else:
                    break


    print("Part 1: ", sums)
    assert(sums == 525911)

def is_gear(grid, r, c):
    #r, c = key
    k = (r - 1, c)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    k = (r + 1, c)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    k = (r, c - 1)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    k = (r, c + 1)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    k = (r - 1, c - 1)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    k = (r + 1, c + 1)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    k = (r + 1, c - 1)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    k = (r - 1, c + 1)
    if k in grid and not grid[k].isdigit() and grid[k] == "*":
        return True, k
    return False, k

def part_two():
    sums = 0
    grid = {}
    ggrid = {}
    ggrid2 = {}
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
            for i in range(1, 5):
                if (r, c + i) in grid and grid[(r, c + i)].isdigit():
                    dig += grid[(r, c + i)]
                    ok1, gear1 = is_gear(grid, r, c + i)
                    ok = ok or ok1
                    if ok1:
                        gear = gear1
                else:
                    break
        if ok:
            if gear in ggrid:
                ggrid2[(gear)] = int(dig)
            else:
                ggrid[(gear)] = int(dig)
            grid[(r, c)] = "."
            for i in range(1, 5):
                if (r, c + i) in grid and grid[(r, c + i)].isdigit():
                    grid[(r, c + i)] = "."
                else:
                    break
    
    for k1, g1 in ggrid.items():
        if k1 in ggrid2:
            sums+=g1*ggrid2[k1]

    print("Part 2: ", sums)
    assert(sums == 75805607)

part_one()
part_two()