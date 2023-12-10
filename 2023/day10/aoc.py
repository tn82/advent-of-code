import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def south_jump(c1, c2):
    if c1 in ("S", "|", "F", "7") and c2 in ("|", "L", "J"):
        return True
    return False

def north_jump(c1, c2):
    if c1 in ("S", "|", "L", "J") and c2 in ("|", "F", "7"):
        return True
    return False

def east_jump(c1, c2):
    if c1 in ("S", "-", "L", "F") and c2 in ("-", "J", "7"):
        return True
    return False

def west_jump(c1, c2):
    if c1 in ("S", "-", "J", "7") and c2 in ("-", "L", "F"):
        return True
    return False

def printer(grid, dists, c):
    row = 0
    for coo in grid:
        if coo[0] != row:
            row = coo[0]
            print()
        if coo in dists:
            if c:
                print(c, end = "")
            else:
                print(grid[coo], end = "")
        else:
            print(".", end = "")
    print()
    print()

def part_one():
    grid = {}
    start = None
    for r, line in enumerate(input()):
        for c, col in enumerate(line):
            grid[(r, c)] = col
            if col == "S":
                start = (r, c)
    
    dists = {}
    dists[start] = 0
    jump_q = [start]

    while jump_q:
        coo = jump_q.pop(0)
        coo_s = (coo[0] + 1, coo[1])
        if coo_s not in dists and coo_s in grid and south_jump(grid[coo], grid[coo_s]):
            dists[coo_s] = dists[coo] + 1
            jump_q.append(coo_s)
        coo_s = (coo[0] - 1, coo[1])
        if coo_s not in dists and coo_s in grid and north_jump(grid[coo], grid[coo_s]):
            dists[coo_s] = dists[coo] + 1
            jump_q.append(coo_s)
        coo_s = (coo[0], coo[1] + 1)
        if coo_s not in dists and coo_s in grid and east_jump(grid[coo], grid[coo_s]):
            dists[coo_s] = dists[coo] + 1
            jump_q.append(coo_s)
        coo_s = (coo[0], coo[1] - 1)
        if coo_s not in dists and coo_s in grid and west_jump(grid[coo], grid[coo_s]):
            dists[coo_s] = dists[coo] + 1
            jump_q.append(coo_s)


    print("Part 1: ", max(dists.values()))
    assert(max(dists.values()) == 6800)

    sums = 0
    enclosed = {}
    for coo in grid:
        if coo in dists:
            continue
        coo_s = coo
        count_crosses = 0
        while coo_s:
            coo_s = (coo_s[0], coo_s[1] + 1)
            if coo_s not in grid:
                coo_s = None
            elif coo_s in dists and grid[coo_s] in ("|", "J", "L", "S"):
                count_crosses += 1
        if count_crosses % 2 != 0:
            sums += 1
            enclosed[coo] = 1
    print("Part 2: ", sums)
    assert(sums == 483)
   
part_one()
