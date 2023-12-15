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
    ask = []
    for i, line in enumerate(input()):
        ask = line.split(",")

    for a in ask:
        val = 0
        for c in a:
            val += ord(c)
            val *= 17
            val = val % 256
        sums += val
    print("Part 1: ", sums)
    assert(sums == 510388)

def hask1(a):
    val = 0
    for c in a:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

def len_in_list(a, ll):
    al = a.split("=")
    for i, l in enumerate(ll):
        lo = l.split("=")
        if al[0] == lo[0]:
            ll[i] = a
            return
    ll.append(a)

def remove(a, ll):
    al = a.split("-")
    for i, l in enumerate(ll):
        lo = l.split("=")
        if al[0] == lo[0]:
            ll.pop(i)
            return

def part_two():
    sums = 0
    ask = []
    for i, line in enumerate(input()):
        ask = line.split(",")

    grid = {}
    grid = {}
    for a in ask:
        val = 0
        if "=" in a:
            al = a.split("=")
            o = hask1(al[0])
            if o in grid:
                len_in_list(a, grid[o])
            else:
                grid[o] = [a]
            continue

        if "-" in a:
            al = a.split("-")
            o = hask1(al[0])
            if o in grid:
                remove(a, grid[o])
                if not grid[o]:
                    del grid[o]

    for box, focals in grid.items():
        for i, f in enumerate(focals):
            al = f.split("=")
            sums += (box + 1) * (i + 1) * int(al[1])

    print("Part 2: ", sums)
    assert(sums == 291774)


part_one()
part_two()