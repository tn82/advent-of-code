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
    l = []
    r = []
    for i, line in enumerate(input()):
        line = line.split()
        #lis = int_list(line)
        l.append(int(line[0]))
        r.append(int(line[1]))
    l.sort()
    r.sort()

    for a, b in zip(l, r):
        sums += abs(a - b)


    print("Part 1: ", sums)
    #assert(sums == 0)


def part_two():
    sums = 0
    l = []
    r = []
    for i, line in enumerate(input()):
        line = line.split(" ")
        #lis = int_list(line)
        l.append(int(line[0]))
        r.append(int(line[3]))
    l.sort()
    r.sort()

    for a in l:
        sums += r.count(a) * a


    print("Part 2: ", sums)
    #assert(sums == 0)


part_one()
part_two()