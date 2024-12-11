import os
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
    # stones = [125,17]
    stones = [4329]
    res = []
    for x in range(8):
        cd = 0
        for i, s in enumerate(stones):
            ss = str(s)
            if s == 0:
                res.append(1)
            elif len(ss) % 2 == 0:
                middle = len(ss) // 2
                res.append(int(ss[:middle]))
                res.append(int(ss[middle:]))
                cd += 1
                # las = int(ss[middle:])
                # if las:
                #    res.append(las)
            else:
                res.append(s * 2024)
        stones = res
        print(res)
        res = []
        # print(len(stones))

    print("Part 1: ", len(res))
    # assert(sums == 0)


def part_two():
    sums = 0
    stones = [4329, 385, 0, 1444386, 600463, 19, 1, 56615]
    for s in stones:
        sums += counter(s, 0, 75)

    print("Part 2: ", sums)
    # assert(sums == 0)


# part_one()
part_two()
