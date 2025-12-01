import os
from collections import defaultdict
import heapq
import copy
from functools import cache

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
    code = 0
    sums = 50
    for i, line in enumerate(input()):
        dir = line[0]
        steps = int(line[1:])
        
        if dir == "L":
            sums = (sums - steps) % 100
        if dir == "R":
            sums = (sums + steps) % 100
        if sums == 0:
            code += 1
            

    print("Part 1: ", code)
    assert(code == 1064)


def part_two():
    code = 0
    sums = 50
    for i, line in enumerate(input()):
        dir = line[0]
        steps = int(line[1:])
        dir = -1 if dir == "L" else 1
        for i in range(steps):
            sums = (sums + 1 * dir) % 100
            if sums == 0:
                code += 1
            

    print("Part 1: ", code)
    assert(code == 6122)


part_one()
part_two()