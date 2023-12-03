import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    sums = 0
    for line in test():
        sums += int(line)

    print("Part 1: ", sums)
    #assert(sums == 0)

def part_two():
    sums = 0
    for line in test():
        sums += int(line)

    print("Part 2: ", sums)
    #assert(sums == 0)

def in_grid(grid, r, c):
    # No diagonal
    # shifts = ((1, 0), (0, 1), (0, -1), (-1, 0))
    # All directions
    shifts = ((1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1))
    for shift in shifts:
        coo = (r + shift[0], c + shift[1])
        if coo in grid and True: # Add conditions
            return True
    return False

#part_one()
#part_two()