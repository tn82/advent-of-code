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

def part_two(n):
    ball_grid = {}
    wall_grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate(input()):
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

    for s in range(n):
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
        #print("First grid:", count)
        #grid_printer(grid)

    print("Part 2: ", len(ball_grid))
    return len(ball_grid)

import time
import copy
def part_two2(n):
    sums = 0
    ball_grid = {}
    wall_grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate(input()):
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
    now = time.time()
    prev_odd = 0
    prev_even = 0
    for s in range(n):
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
                    if s % 2 == 0:
                        if coos in wall_even:
                            continue
                        grids[coos] = "0"
                    if s % 2 != 0:
                        if coos in wall_odd:
                            continue
                        grids[coos] = "0"

        #prev_ball_grid = copy.copy(grids)
        if s % 2 == 0:
            count_even += len(grids)
            #wall_even = copy.copy(grids)
            wall_even = grids
        else:
            count_odd += len(grids)
            #wall_odd = copy.copy(grids)
            wall_odd = grids
        #print("Even: ", count_even)
        #print("Odd: ", count_odd)
        #ball_grid = copy.copy(grids)
        ball_grid = grids
        if s % 100 == 0:
            #print("Iteration,", s, ",", time.time() - now, ",", len(grids), ",", count_even, ",", count_even - prev_even, ",", count_odd, ",", count_odd - prev_odd)
            prev_even = count_even
            prev_odd = count_odd
            now = time.time()
        #grid_printer(grid)
    #print("Even: ", count_even)
    #print("Odd: ", count_odd)
    #print("Part 2: ", count_odd) # 3737 2665
    print("n=", n, count_odd if n % 2 != 0 else count_even)
    return count_odd if n % 2 != 0 else count_even


#part_one()
k0 = part_two(65 + 131 * 0) #2722
k1 = part_two(65 + 131 * 1) #25621
k2 = part_two(65 + 131 * 2) #71435
import numpy as np

vandermonde = np.matrix([[1, 0, 0], [1, 1, 1], [1, 2, 4]])
b = np.array([k0, k1, k2])
x = np.linalg.solve(vandermonde, b).astype(np.int64)

# note that 26501365 = 202300 * 131 + 65 where 131 is the dimension of the grid
n = 202300
print("part 2:", x[0] + x[1] * n + x[2] * n * n)
# 468883362047022 low
# 468228516137765
# 625382415472037 low