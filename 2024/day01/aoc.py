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


def parse_input():
    left = []
    right = []
    for _, line in enumerate(input()):
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    return left, right


def part_one():
    sums = 0
    left, right = parse_input()

    for l, r in zip(left, right):
        sums += abs(l - r)

    print("Part 1: ", sums)
    assert sums == 3508942


def part_two():
    sums = 0
    left, right = parse_input()

    for l in left:
        sums += right.count(l) * l

    print("Part 2: ", sums)
    assert sums == 26593248


part_one()
part_two()
