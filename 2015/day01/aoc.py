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
    sums = 0
    for i, line in enumerate(input()):
        for c in line:
            if c == "(":
                sums += 1
            if c == ")":
                sums -= 1

    print("Part 1: ", sums)
    assert(sums == 232)


def part_two():
    sums = 0
    for _, line in enumerate(input()):
        for i, c in enumerate(line):
            if c == "(":
                sums += 1
            if c == ")":
                sums -= 1
            if sums < 0:
                break

    print("Part 2: ", i + 1)
    assert(i + 1 == 1783)


part_one()
part_two()