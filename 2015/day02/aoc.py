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
    paper = 0
    ribbon = 0
    for i, line in enumerate(input()):
        l, w, h = int_list(line.split("x"))
        paper += 2* l * w + 2 * l * h + 2 * w * h + min(l * w, l * h, w * h)
        dims = sorted([l, w, h])
        ribbon += dims[0] * 2 + dims[1] * 2 + l * w * h

    print("Part 1: ", paper)
    assert(paper == 1588178)

    print("Part 2: ", ribbon)
    assert(ribbon == 3783758)

part_one()
#part_two()