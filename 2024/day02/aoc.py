import copy
from itertools import pairwise
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
    lines =[]
    for i, line in enumerate(input()):
        line = line.split()
        lines.append(int_list(line))

    for line in lines:
        m = max(b-a for (a,b) in pairwise(line))
        m1 = min(b-a for (a,b) in pairwise(line))
        if m > 3 or m1 < -3:
            continue
        is_sorted = all(line[x] < line[x + 1] for x in range(len(line) - 1))
        is_sortedr = all(line[x] > line[x + 1] for x in range(len(line) - 1))
        if not is_sorted and not is_sortedr:
            continue
        sums += 1


    print("Part 1: ", sums)
    #assert(sums == 0)


def part_two():
    sums = 0
    lines =[]
    for i, line in enumerate(input()):
        line = line.split()
        lines.append(int_list(line))

    remain = []
    for line in lines:
        m = max(b-a for (a,b) in pairwise(line))
        m1 = min(b-a for (a,b) in pairwise(line))
        if m > 3 or m1 < -3:
            remain.append(line)
            continue
        is_sorted = all(line[x] < line[x + 1] for x in range(len(line) - 1))
        is_sortedr = all(line[x] > line[x + 1] for x in range(len(line) - 1))
        if not is_sorted and not is_sortedr:
            remain.append(line)
            continue
        sums += 1

    for line in remain:
        for i, l in enumerate(line):
            line2 = copy.copy(line)
            line2.pop(i)
            m = max(b-a for (a,b) in pairwise(line2))
            m1 = min(b-a for (a,b) in pairwise(line2))
            if m > 3 or m1 < -3:
                continue
            is_sorted = all(line2[x] < line2[x + 1] for x in range(len(line2) - 1))
            is_sortedr = all(line2[x] > line2[x + 1] for x in range(len(line2) - 1))
            if not is_sorted and not is_sortedr:
                continue
            sums += 1
            break
    print("Part 2: ", sums)



#part_one()
part_two()