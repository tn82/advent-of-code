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

def deltas(line):
    d = []
    for i in range(1, len(line)):
        d.append(line[i] - line[i - 1])
    return d

def only_zero(line):
    return all(v == 0 for v in line)

def part_one():
    sums = 0
    for i, line in enumerate(input()):
        linep = int_list(line.split())
        i = 0

        grid = [[]]
        grid[0] = linep
        j = 1
        while True:
            grid.append(deltas(grid[j - 1]))
            if only_zero(grid[j]):
                break
            j += 1
        s = 0
        for j in range(len(grid) - 1, 0, -1):
            s = grid[j][-1] + grid[j-1][-1]
            grid[j-1].append(s)
        sums += s
    print("Part 1: ", sums)
    assert(sums == 1762065988)


def part_two():
    sums = 0
    for i, line in enumerate(input()):
        linep = int_list(line.split())
        i = 0

        grid = [[]]
        grid[0] = linep
        j = 1
        while True:
            grid.append(deltas(grid[j - 1]))
            if only_zero(grid[j]):
                break
            j += 1
        s = 0
        for j in range(len(grid) - 1, 0, -1):
            s = -grid[j][0] + grid[j-1][0]
            grid[j-1].insert(0, s)
        sums += s
    print("Part 2: ", sums)
    assert(sums == 1066)


part_one()
part_two()
