import os
from collections import defaultdict
import heapq
import copy

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
    for i, line in enumerate(test()):
        sums += int(line)

    print("Part 1: ", sums)
    #assert(sums == 0)


def part_two():
    sums = 0
    for i, line in enumerate(test()):
        sums += int(line)

    print("Part 2: ", sums)
    #assert(sums == 0)


part_one()
#part_two()