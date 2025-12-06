import os
from collections import defaultdict
import heapq
import copy
from functools import cache

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line[:-1] for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line[:-1] for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]

def part_one():
    sums = 0
    data = []
    ops = []
    for i, line in enumerate(input()):
        if "+" in line:
            ops = line.split()
        else:
            data.append(line.split())

    for c in range(len(data[0])):
        s = int(data[0][c])
        for r in range(1, len(data)):
            if ops[c] == "+":
                s += int(data[r][c])
            else:
                s *= int(data[r][c])
        sums += s


    print("Part 1: ", sums)
    assert(sums == 6299564383938)


def part_two():
    sums = 0
    data = []
    ops = []
    raw_data = input()
    raw_ops = raw_data[-1]
    raw_data = raw_data[:-1]

    ok = True
    while (ok):
        p = raw_ops.find("+")
        p = 1000 if p == -1 else p
        m = raw_ops.find("*")
        m = 1000 if m == -1 else m
        op = "+" if p < m else "*"
        ops.append(op)
        i = min(p, m)
        raw_ops = raw_ops[i + 1:]

        next_p = raw_ops.find("+")
        next_p = 1000 if next_p == -1 else next_p

        next_m = raw_ops.find("*")
        next_m = 1000 if next_m == -1 else next_m

        next_i = min(next_p, next_m)
        next_i = next_i if next_i != 1000 else len(raw_data[0])

        if next_i == 0:
            break

        datas = []
        for c in range(next_i):
            n = ""
            for r in raw_data:
                if r[c] != " ":
                    n += r[c]
            datas.append(int(n))
        data.append(datas)
        raw_data2 = []
        for r in raw_data:
            raw_data2.append(r[next_i + 1:])
        raw_data = raw_data2



    for i, r in enumerate(data):
        s = int(r[0])
        for j in range(1, len(r)):
            if ops[i] == "+":
                s += int(r[j])
            else:
                s *= int(r[j])
        sums += s

    print("Part 2: ", sums)
    #assert(sums == 0)


#part_one()
part_two()