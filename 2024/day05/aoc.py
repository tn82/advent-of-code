import os
from collections import defaultdict

day_path = os.path.dirname(__file__)


def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]


def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]


def input2():
    with open(os.path.join(day_path, "input2.txt"), "r") as file:
        return [line.rstrip() for line in file]


def test2():
    with open(os.path.join(day_path, "test2.txt"), "r") as file:
        return [line.rstrip() for line in file]


def findex(my_list, target):
    try:
        return my_list.index(target)
    except ValueError:
        return -1


def part_one():
    sums = 0
    order = []
    for i, line in enumerate(input()):
        f, s = line.split("|")
        order.append((int(f), int(s)))

    inst = []
    for i, line in enumerate(input2()):
        inst.append([int(c) for c in line.split(",")])

    for ins in inst:
        for ord in order:
            f = findex(ins, ord[0])
            s = findex(ins, ord[1])
            if f != -1 and s != -1 and f > s:
                break
        else:
            # only executed if the inner loop did NOT break
            sums += ins[int((len(ins) - 1) / 2)]

    print("Part 1: ", sums)
    assert sums == 4774


def part_two():
    sums = 0
    order = []
    for i, line in enumerate(input()):
        f, s = line.split("|")
        order.append((int(f), int(s)))

    inst = []
    for i, line in enumerate(input2()):
        inst.append([int(c) for c in line.split(",")])

    bad = []
    for ins in inst:
        for ord in order:
            f = findex(ins, ord[0])
            s = findex(ins, ord[1])
            if f != -1 and s != -1 and f > s:
                break
        else:
            # only executed if the inner loop did NOT break
            continue
        bad.append(ins)

    for ins in bad:
        updated = 1
        while updated:
            updated = 0
            for ord in order:
                f = findex(ins, ord[0])
                s = findex(ins, ord[1])
                if f != -1 and s != -1 and f > s:
                    updated += 1
                    ins[f], ins[s] = ins[s], ins[f]

    for ins in bad:
        sums += ins[int((len(ins) - 1) / 2)]

    print("Part 2: ", sums)
    assert sums == 6004


part_one()
part_two()
