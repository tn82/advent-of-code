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
    grid = defaultdict(int)
    for i, line in enumerate(input()):
        x, y = 0, 0
        grid[(x, y)] += 1
        for _, c in enumerate(line):
            if c == "<":
                y -= 1
            elif c == ">":
                y += 1
            elif c == "^":
                x += 1
            elif c == "v":
                x -= 1
            grid[(x, y)] += 1

    print("Part 1: ", len(grid))
    assert(len(grid) == 2565)


def part_two():
    grid = defaultdict(int)
    for i, line in enumerate(input()):
        x, y = 0, 0
        rx, ry = 0, 0
        grid[(x, y)] += 1
        for j, c in enumerate(line):
            if j % 2 == 0:
                if c == "<":
                    y -= 1
                elif c == ">":
                    y += 1
                elif c == "^":
                    x += 1
                elif c == "v":
                    x -= 1
                grid[(x, y)] += 1
            else:
                if c == "<":
                    ry -= 1
                elif c == ">":
                    ry += 1
                elif c == "^":
                    rx += 1
                elif c == "v":
                    rx -= 1
                grid[(rx, ry)] += 1


    print("Part 2: ", len(grid))
    assert(len(grid) == 2639)


part_one()
part_two()