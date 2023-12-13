import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def mirror_line(grid):
    for i in range(len(grid) - 1):
        if grid[i] != grid[i + 1]:
            continue
        i2_offset = 1
        for i2 in range(i + 1, len(grid) + 1):
            if i2 - i2_offset < 0:
                return i + 1
            if i2 == len(grid):
                return i + 1
            if grid[i2] == grid[i2 - i2_offset]:
                i2_offset += 2
            else:
                break
    return 0

def rotate2D_clockwise(grid):
    return list(zip(*grid[::-1]))

def part_one():
    sums = 0
    i = 0
    grid = []
    for _, line in enumerate(input()):
        if not line or line == "T":
            sums += 100 * mirror_line(grid)
            rot = rotate2D_clockwise(grid)
            sums += mirror_line(rot)
            i = 0
            grid.clear()
            continue
        grid.append([])
        for ci, c in enumerate(line):
            grid[i].append(c)
        i += 1

    print("Part 1: ", sums)
    assert(sums == 33975)

def line_errors(line1, line2):
    return sum(1 for i, j in zip(line1, line2) if i != j)

def mirror_line_smudge(grid):
    for i in range(len(grid) - 1):
        errors = 0
        i2_offset = 1
        for i2 in range(i + 1, len(grid) + 1):
            if i2 - i2_offset < 0:
                break
            if i2 == len(grid):
                break
            errors += line_errors(grid[i2], grid[i2 - i2_offset])
            i2_offset += 2

            if errors > 1:
                break
        if errors == 1:
            return i + 1 
    return 0

def part_two():
    sums = 0
    i = 0
    grid = []
    for _, line in enumerate(input()):
        if not line or line == "T":
            sums += 100 * mirror_line_smudge(grid)
            rot = rotate2D_clockwise(grid)
            sums += mirror_line_smudge(rot)
            i = 0
            grid.clear()
            continue
        grid.append([])
        for ci, c in enumerate(line):
            grid[i].append(c)
        i += 1

    print("Part 2: ", sums)
    assert(sums == 29083)

part_one()
part_two()