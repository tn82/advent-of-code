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

def next_num(n):
    mul = n * 64
    n = mul ^ n
    n = n % 16777216

    mul = int(n / 32)
    n = mul ^ n
    n = n % 16777216

    mul = n * 2048
    n = mul ^ n
    n = n % 16777216

    return n

def part_one():
    sums = 0
    nums = []
    for i, line in enumerate(input()):
        nums.append(int(line))

    for n in nums:
        for _ in range(2000):
            n = next_num(n)
        sums += n

    print("Part 1: ", sums)
    assert(sums == 17262627539)


def part_two():
    sums = 0
    nums = []
    for i, line in enumerate(input()):
        nums.append(int(line))

    combos = defaultdict(list)
    combos_check = set()
    for n in nums:
        changes = [(n,n % 10,1e9)]
        n2 = n
        for _ in range(2000):
            n2 = next_num(n2)
            ones = n2 % 10
            changes.append((n,ones, ones - changes[-1][1]))
            if len(changes) > 4:
                changes.pop(0)
            changes2 = [c[2] for c in changes]
            if changes2 == [-2,1,-1,3]:
                kk = 0
            changes3 = copy.copy(changes2)
            changes3.append(n)
            if tuple(changes3) not in combos_check:
                combos[tuple(changes2)].append((n, ones))
            combos_check.add(tuple(changes3))

    
    for change, combo in combos.items():
        s = sum([c[1] for c in combo])
        if s > sums:
            sums = s


    print("Part 2: ", sums)
    assert(sums == 1986)


part_one()
part_two()