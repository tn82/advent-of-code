import re

prios = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part_one():
    file = open("input.txt", "r")
    sum = 0
    for line in file:
        line = line.strip()
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]
        for c in ''.join(set(comp1)):
            if c in comp2:
                sum = sum + prios.index(c) + 1
    assert sum == 7674
    print("Part 1: ", sum)

part_one()

def part_two():
    file = open("input.txt", "r")
    sum = 0
    i = 0
    l1 = []
    for line in file:
        line = line.strip()
        l1.append(line)
        i = i + 1
        if i == 3:
            for c in ''.join(set(l1[0])):
                if c in l1[1] and c in l1[2]:
                    sum = sum + prios.index(c) + 1
            l1 = []
            i = 0
    assert sum == 2805
    print("Part 2: ", sum)

part_two()