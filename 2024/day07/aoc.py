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

import copy

def reccu(facit, vs, add, curr_sum=0):
    a = vs.pop(0)
    b = vs[0]
    if add:
        curr_sum = curr_sum + b
    if not add:
        curr_sum = curr_sum * b
    if len(vs) == 1:
        return 1 if curr_sum == facit else 0
    t1 = reccu(facit, vs.copy(), True, curr_sum)
    t2 = reccu(facit, vs.copy(), False, curr_sum)

    return t1 or t2



def part_one():
    sums = 0
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
    
    for r, vs in zip(res, vals):
        t1 = reccu(r, vs.copy(), True, vs[0])
        t2 = reccu(r, vs.copy(), False, vs[0])

        if t1 or t2:
            sums += r

    
    
    

    print("Part 1: ", sums)
    assert(sums == 1399219271639)

def reccu2(facit, vs, add, curr_sum=0):
    vs.pop(0)
    b = vs[0]
    if add == 1:
        curr_sum = curr_sum + b
    if add == 2:
        curr_sum = curr_sum * b
    if add == 3:
        curr_sum = int(str(curr_sum) + str(b))
    if len(vs) == 1:
        return 1 if curr_sum == facit else 0
    t1 = reccu2(facit, vs.copy(), 1, curr_sum)
    t2 = reccu2(facit, vs.copy(), 2, curr_sum)
    t3 = reccu2(facit, vs.copy(), 3, curr_sum)

    return t1 or t2 or t3

def part_two():
    sums = 0
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
    
    for r, vs in zip(res, vals):
        t1 = reccu2(r, vs.copy(), 1, vs[0])
        t2 = reccu2(r, vs.copy(), 2, vs[0])
        t3 = reccu2(r, vs.copy(), 3, vs[0])

        if t1 or t2 or t3:
            sums += r

    print("Part 2: ", sums)
    assert(sums == 275791737999003)


part_one()
part_two()