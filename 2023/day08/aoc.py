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
    t1 = "LLR"
    t1 = "LRRLLRLLRRRLRRLRLRRRLRLLRLRRLRRRLRRRLRRLRRRLRLRRRLRLRRLRLRRRLRRLLRRLLLRRLRLRRRLRLRRRLRRLRRRLRLLRRLRRLRLRRRLRRRLRRLRRLLRLLRRRLRLRRLRRRLRRLRRRLRRRLLLLRRLRLRRRLRRRLLRRLLRRLRRRLRRRLRLRLLRRLRLRLRLRLRRLRLRLRRRLRRLRRLRRLRRRLRLRRRLRLRRLRLLLLRRRLLRRRLRLLRRRLRLLRRRLLRRLRLRLRLRLLLLRRLRRRLRLLRRLRRRLRRRLRLRRLRRLRLLRRRR"
    grid = {}
    for i, line in enumerate(input()):
        p, lr = line.split("=")
        p = p.replace(" ", "")
        lr = lr.replace("(", "").replace(")", "").replace(" ", "")
        left, right = lr.split(",")
        grid[p] = (left, right)
    pos = grid["AAA"]
    steps = 0
    for c in t1 * 1000:
        j = pos[0] if c == "L" else pos[1]
        pos = grid[j]
        steps += 1
        if j == "ZZZ":
            break

    print("Part 1: ", steps)
    assert(steps == 21797)


def part_two2():
    t1 = "LR"
    t1 = "LRRLLRLLRRRLRRLRLRRRLRLLRLRRLRRRLRRRLRRLRRRLRLRRRLRLRRLRLRRRLRRLLRRLLLRRLRLRRRLRLRRRLRRLRRRLRLLRRLRRLRLRRRLRRRLRRLRRLLRLLRRRLRLRRLRRRLRRLRRRLRRRLLLLRRLRLRRRLRRRLLRRLLRRLRRRLRRRLRLRLLRRLRLRLRLRLRRLRLRLRRRLRRLRRLRRLRRRLRLRRRLRLRRLRLLLLRRRLLRRRLRLLRRRLRLLRRRLLRRLRLRLRLRLLLLRRLRRRLRLLRRLRRRLRRRLRLRRLRRLRLLRRRR"
    grid = {}
    for i, line in enumerate(input()):
        p, lr = line.split("=")
        p = p.replace(" ", "")
        lr = lr.replace("(", "").replace(")", "").replace(" ", "")
        left, right = lr.split(",")
        grid[p] = (left, right)
    positions = []
    for g in grid.keys():
        if g.endswith("A"):
            positions.append(g)
    steps = 0
    lens = len(t1)
    t1i = 0
    oks_max = 0
    while True:
        c = t1[t1i]
        t1i += 1
        t1i = t1i % lens
        oks = 0
        positions_temp = []
        for p in positions:
            pos = grid[p]
            j = pos[0] if c == "L" else pos[1]
            pos = grid[j]
            positions_temp.append(j)
            if j.endswith("Z"):
                oks += 1
            break
        positions = positions_temp
        steps += 1
        if steps % 1000000 == 0:
            print("Steps: ", steps)
        if oks == len(positions_temp):
            print("Part 2: ", steps)
            #break
        if oks > oks_max:
            oks_max = oks
            print("oks_max: ", oks_max)

    print("Part 2: end")

import math   
def prime_factors(n): 
    primes = []
    while n % 2 == 0: 
        primes.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            primes.append(i)
            n = n / i 
    if n > 2: 
        primes.append(n)
    return primes

def part_two():
    t1 = "LR"
    t1 = "LRRLLRLLRRRLRRLRLRRRLRLLRLRRLRRRLRRRLRRLRRRLRLRRRLRLRRLRLRRRLRRLLRRLLLRRLRLRRRLRLRRRLRRLRRRLRLLRRLRRLRLRRRLRRRLRRLRRLLRLLRRRLRLRRLRRRLRRLRRRLRRRLLLLRRLRLRRRLRRRLLRRLLRRLRRRLRRRLRLRLLRRLRLRLRLRLRRLRLRLRRRLRRLRRLRRLRRRLRLRRRLRLRRLRLLLLRRRLLRRRLRLLRRRLRLLRRRLLRRLRLRLRLRLLLLRRLRRRLRLLRRLRRRLRRRLRLRRLRRLRLLRRRR"
    grid = {}
    for i, line in enumerate(input()):
        p, lr = line.split("=")
        p = p.replace(" ", "")
        lr = lr.replace("(", "").replace(")", "").replace(" ", "")
        left, right = lr.split(",")
        grid[p] = (left, right)
    positions = []
    for g in grid.keys():
        if g.endswith("A"):
            positions.append(g)
    lens = len(t1)

    prime_factor = lens
    for p in positions:
        pp = p
        steps = 0   
        t1i = 0
        while True:
            c = t1[t1i]
            t1i += 1
            t1i = t1i % lens
            oks = 0
            pos = grid[pp]
            j = pos[0] if c == "L" else pos[1]
            pos = grid[j]
            pp = j
            if j.endswith("Z"):
                oks += 1
            steps += 1
            if oks == 1:
                prime_factor *= prime_factors(steps)[0]
                print("Part 2,", prime_factors(steps))
                break

    print("Part 2: ", prime_factor)
    assert(prime_factor == 23977527174353)

part_one()
part_two()