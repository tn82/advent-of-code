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
    sums = 0
    fresh = []
    items = set()
    for i, line in enumerate(input()):
        if "-" in line:
            r1, r2 = line.split("-")
            fresh.append([int(r1), int(r2)])
        else:
            items.add(int(line))

    for item in items:
        for range in fresh:
            if range[0] <= item <= range[1]:
                sums += 1
                break

    print("Part 1: ", sums)
    assert(sums == 848)


def part_two():
    sums = 0
    ranges = []
    items = set()
    for _, line in enumerate(input()):
        if "-" in line:
            r1, r2 = line.split("-")
            ranges.append([int(r1), int(r2)])
        else:
            items.add(int(line))

    ranges.sort(key=lambda x: x[0])
    merged_ranges = []
    for r in ranges:
        in_merged = False
        for mr in merged_ranges:
            if mr[0] <= r[0] <= mr[1]:
                in_merged = True
            if mr[0] <= r[1] <= mr[1]:
                in_merged = True
            if not in_merged:
                continue
            
            
            if r[0] < mr[0]:
                mr[0] = r[0]
            elif r[1] > mr[1]:
                mr[1] = r[1]
        if not in_merged:
            merged_ranges.append(r)

    for r in merged_ranges:
        sums += r[1] - r[0] + 1


    print("Part 2: ", sums)
    assert(sums == 334714395325710)


part_one()
part_two()