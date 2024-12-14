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
    grid = {}
    for i, line in enumerate(input()):
        parts = line.split()
        action = parts[0] if parts[0] == "toggle" else " ".join(parts[:2])
        x1, y1 = map(int, parts[-3].split(","))
        x2, y2 = map(int, parts[-1].split(","))
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if action == "turn on":
                    grid[(x, y)] = 1
                elif action == "turn off":
                    grid[(x, y)] = 0
                elif action == "toggle":
                    if (x, y) in grid and grid[(x, y)] == 1:
                        grid[(x, y)] = 0
                    elif (x, y) not in grid or grid[(x, y)] == 0:
                        grid[(x, y)] = 1

    print("Part 1: ", sum(grid.values()))
    assert(sum(grid.values()) == 569999)


def part_two():
    grid = defaultdict(int)
    for i, line in enumerate(input()):
        parts = line.split()
        action = parts[0] if parts[0] == "toggle" else " ".join(parts[:2])
        x1, y1 = map(int, parts[-3].split(","))
        x2, y2 = map(int, parts[-1].split(","))
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if action == "turn on":
                    grid[(x, y)] += 1
                elif action == "turn off":
                    if (x, y) in grid and grid[(x, y)] > 0:
                        grid[(x, y)] -= 1
                elif action == "toggle":
                    grid[(x, y)] += 2

    print("Part 2: ", sum(grid.values()))
    assert(sum(grid.values()) == 17836115)


part_one()
part_two()