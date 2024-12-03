import copy
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


def is_safe(line):
    dec_ok = all(
        line[i] - line[i + 1] < 0 and line[i] - line[i + 1] >= -3
        for i in range(len(line) - 1)
    )
    inc_ok = all(
        line[i] - line[i + 1] > 0 and line[i] - line[i + 1] <= 3
        for i in range(len(line) - 1)
    )
    return dec_ok or inc_ok


def part_one():
    sums = 0
    lines = []
    for i, line in enumerate(input()):
        line = line.split()
        lines.append(int_list(line))

    for line in lines:
        if is_safe(line):
            sums += 1

    print("Part 1: ", sums)
    assert sums == 516


def part_two():
    sums = 0
    lines = []
    for i, line in enumerate(input()):
        line = line.split()
        lines.append(int_list(line))

    remain = []
    for line in lines:
        if is_safe(line):
            sums += 1
            continue
        remain.append(line)

    for line in remain:
        for i, _ in enumerate(line):
            line2 = copy.copy(line)
            line2.pop(i)
            if is_safe(line2):
                sums += 1
                break

    print("Part 2: ", sums)
    assert sums == 561


part_one()
part_two()
