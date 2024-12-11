import os
from functools import cache

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
    sums = 0
    stones = [4329, 385, 0, 1444386, 600463, 19, 1, 56615]
    for s in stones:
        sums += counter(s, 0, 75)

    print("Part 2: ", sums)
    assert(sums == 259755538429618)


part_one()
part_two()
