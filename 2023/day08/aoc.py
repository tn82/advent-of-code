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
    while True:
        c = t1[steps % len(t1)]
        j = pos[0] if c == "L" else pos[1]
        pos = grid[j]
        steps += 1
        if j == "ZZZ":
            break

    print("Part 1: ", steps)
    assert(steps == 21797)

import math
def prime_factors(n):
    primes = []
    while n % 2 == 0: 
        primes.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
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

    primes = set()
    for start_pos in positions:
        pos = grid[start_pos]
        steps = 0
        while True:
            c = t1[steps % len(t1)]
            j = pos[0] if c == "L" else pos[1]
            pos = grid[j]
            steps += 1
            if j.endswith("Z"):
                primes.update(prime_factors(steps))
                break

    common_factor = 1
    for p in primes:
        common_factor *= int(p)
    print("Part 2: ", common_factor)
    assert(common_factor == 23977527174353)

part_one()
part_two()