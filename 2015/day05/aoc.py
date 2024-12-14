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


def invalid1(line):
    for s in ("ab", "cd", "pq", "xy"):
        if s in line:
            return True
    return False


def invalid2(line):
    c = 0
    for s in "aeiou":
        cs = line.count(s)
        if s in line:
            c += cs
    return c < 3


def valid3(line):
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            return True
    return False


def part_one():
    sums = 0
    for i, line in enumerate(input()):
        if invalid1(line):
            continue
        if invalid2(line):
            continue
        if valid3(line):
            sums += 1

    print("Part 1: ", sums)
    assert sums == 255


def valid4(line):
    for i in range(len(line) - 3):
        if line[i : i + 2] in line[i + 2 :]:
            return True
    return False


def valid5(line):
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            return True
    return False


def part_two():
    sums = 0
    for i, line in enumerate(input()):
        if valid4(line) and valid5(line):
            sums += 1

    print("Part 2: ", sums)
    assert sums == 55


part_one()
part_two()
