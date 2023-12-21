import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

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
    for i, line in enumerate((test())):
        for j, v in enumerate(line):
            grid[(i, j)] = v
    
    for s in range(64):
        grids = {}
        for coo, v in grid.items():
            if v == "0":
                grid[coo] = "."
                shifts = ((1, 0), (0, 1), (0, -1), (-1, 0))
                for shift in shifts:
                    coos = (coo[0] + shift[0], coo[1] + shift[1])
                    if coos in grid and grid[coos] != "#":
                        grids[coos] = "0"
        for coo, v in grids.items():
            grid[coo] = v
        grids.clear()
        grid_printer(grid)


    for coo, v in grid.items():
        if v == "0":
            sums += 1

    print("Part 1: ", sums)
    assert(sums == 3737)

def part_two():
    sums = 0
    ball_grid = {}
    wall_grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate((input())):
        for j, v in enumerate(line):
            if v == "0":
                ball_grid[(i, j)] = v
            elif v == "#":
                wall_grid[(i, j)] = v
            if i > xmax:
                xmax = i
            if j > ymax:
                ymax = j
    
    grid_grid = {}

    for s in range(26501365):
        grids = {}
        for coo, v in ball_grid.items():
            shifts = ((1, 0), (0, 1), (0, -1), (-1, 0))
            for shift in shifts:
                coos = (coo[0] + shift[0], coo[1] + shift[1])
                x, y = coos
                coos_mod = (x % (xmax+1), y % (ymax+1))
                if coos_mod not in wall_grid:
                    grids[coos] = "0"

        ball_grid.clear()
        for coo, v in grids.items():
            ball_grid[coo] = v
        grids.clear()
        #print(len(ball_grid))
        
        count = 0
        for coo, v in ball_grid.items():
            x, y = coo
            if x >= 0 and x < xmax and y >= 0 and y < ymax:
                count += 1
        print("First grid:", count)
        #grid_printer(grid)

    print("Part 2: ", len(ball_grid))

import copy
def part_two2():
    sums = 0
    ball_grid = {}
    wall_grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate((input())):
        for j, v in enumerate(line):
            if v == "0":
                ball_grid[(i, j)] = v
            elif v == "#":
                wall_grid[(i, j)] = v
            if i > xmax:
                xmax = i
            if j > ymax:
                ymax = j
    
    count_odd = len(ball_grid) # = 1
    count_even = 0
    wall_odd = copy.copy(ball_grid)
    wall_even = {}
    #prev_ball_grid = {}
    for s in range(26501365):
        grids = {}
        for coo, v in ball_grid.items():
            shifts = ((1, 0), (0, 1), (0, -1), (-1, 0))
            for shift in shifts:
                coos = (coo[0] + shift[0], coo[1] + shift[1])
                x, y = coos
                coos_mod = (x % (xmax+1), y % (ymax+1))
                if coos_mod not in wall_grid and coos not in ball_grid:
                    #if coos in prev_ball_grid:
                    #    continue
                    if s % 2 == 0 and coos in wall_even:
                        continue
                    if s % 2 != 0 and coos in wall_odd:
                        continue
                    grids[coos] = "0"

        #prev_ball_grid = copy.copy(grids)
        if s % 2 == 0:
            count_even += len(grids)
            wall_even = copy.copy(grids)
        else:
            count_odd += len(grids)
            wall_odd = copy.copy(grids)
        #print("Even: ", count_even)
        #print("Odd: ", count_odd)
        ball_grid = copy.copy(grids)
        if s % 100000 == 0:
            print("Iteration:", s)
        #grid_printer(grid)
    print("Even: ", count_even)
    print("Odd: ", count_odd)
    print("Part 2: ", count_odd) # 3737 2665

#part_one()
part_two2()