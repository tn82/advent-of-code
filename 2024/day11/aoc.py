import os
from functools import cache
from collections import defaultdict
import copy

day_path = os.path.dirname(__file__)

@cache
def counter(s, i, break_i):
    if i == break_i:
        return 1
    num_sols = 0
    ss = str(s)
    if s == 0:
        num_sols += counter(1, i + 1, break_i)
    elif len(ss) % 2 == 0:
        middle = len(ss) // 2
        num_sols += counter(int(ss[:middle]), i + 1, break_i)
        num_sols += counter(int(ss[middle:]), i + 1, break_i)
    else:
        num_sols += counter(s * 2024, i + 1, break_i)
    return num_sols


def part_one():
    sums = 0
    stones = [4329, 385, 0, 1444386, 600463, 19, 1, 56615]
    for s in stones:
        sums += counter(s, 0, 25)

    print("Part 1: ", sums)
    assert(sums == 218079)


def part_two():
    stones = [4329, 385, 0, 1444386, 600463, 19, 1, 56615]
    resse = defaultdict(int)
    for s in stones:
        resse[s] = 1
    for _ in range(75):
        ress_local = defaultdict(int)
        for s in resse.keys():
            ss = str(s)
            if s == 0:
                ress_local[1] += resse[s]
            elif len(ss) % 2 == 0:
                middle = len(ss) // 2
                ress_local[int(ss[:middle])] += resse[s]
                ress_local[int(ss[middle:])] += resse[s]
            else:
                ress_local[s * 2024] += resse[s]
        resse = ress_local

    sums = 0
    for s, sv in resse.items():
        sums += sv
    print("Part 2: ", sums)


    sums = 0
    stones = [4329, 385, 0, 1444386, 600463, 19, 1, 56615]
    for s in stones:
        sums += counter(s, 0, 75)

    print("Part 2: ", sums)
    assert(sums == 259755538429618)


part_one()
part_two()
