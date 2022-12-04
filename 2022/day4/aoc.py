import re


def part_one():
    file = open("input.txt", "r")
    sum = 0
    for line in file:
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1 = [int(i) for i in elf1.split('-')]
        elf2 = [int(i) for i in elf2.split('-')]

        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            sum = sum + 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            sum = sum + 1

    assert sum == 530
    print("Part 1: ", sum)

part_one()

def any_overlap(range1, range2):
    if range2[0] <= range1[0] <= range2[1]:
        return True
    if range2[0] <= range1[1] <= range2[1]:
        return True
    if range1[0] <= range2[0] <= range1[1]:
        return True
    if range1[0] <= range2[1] <= range1[1]:
        return True


def overlap_set(range1, range2):
    s1 = set(range(range1[0], range1[1] + 1))
    s2 = set(range(range2[0], range2[1] + 1))
    return True if len(sorted(s1.intersection(s2))) else False


def part_two():
    file = open("input.txt", "r")
    sum = 0
    for line in file:
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1 = [int(i) for i in elf1.split('-')]
        elf2 = [int(i) for i in elf2.split('-')]

        if overlap_set(elf1, elf2):
            sum = sum + 1

    assert sum == 903
    print("Part 2: ", sum)

part_two()