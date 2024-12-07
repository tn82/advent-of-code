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


def reccu(facit, vs, add, use_concat, curr_sum=0):
    b = vs[0]
    if add == 1:
        curr_sum = curr_sum + b
    if add == 2:
        curr_sum = curr_sum * b
    if add == 3:
        curr_sum = int(str(curr_sum) + str(b))
    if len(vs) == 1:
        return 1 if curr_sum == facit else 0
    t1 = reccu(facit, vs[1:], 1, use_concat, curr_sum)
    t2 = reccu(facit, vs[1:], 2, use_concat, curr_sum)
    t3 = reccu(facit, vs[1:], 3, use_concat, curr_sum) if use_concat else 0

    return t1 or t2 or t3


def day07():
    res = []
    vals = []
    for i, line in enumerate(input()):
        r, v = line.split(":")
        res.append(int(r))
        v = v.split(" ")
        vals2 = []
        for i in v:
            if i and i != " ":
                vals2.append(int(i))
        vals.append(vals2)

    part1 = 0
    for r, vs in zip(res, vals):
        t1 = reccu(r, vs[1:], 1, False, vs[0])
        t2 = reccu(r, vs[1:], 2, False, vs[0])

        if t1 or t2:
            part1 += r

    print("Part 1: ", part1)
    assert part1 == 1399219271639

    part2 = 0
    for r, vs in zip(res, vals):
        t1 = reccu(r, vs[1:], 1, True, vs[0])
        t2 = reccu(r, vs[1:], 2, True, vs[0])
        t3 = reccu(r, vs[1:], 3, True, vs[0])

        if t1 or t2 or t3:
            part2 += r

    print("Part 2: ", part2)
    assert part2 == 275791737999003


day07()
