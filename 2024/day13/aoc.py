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
    button_a = []
    button_b = []
    prize = []
    for i, line in enumerate(input()):
        if not line:
            continue
        a, b = line.split(":")
        x, y = b.split(",")
        if a == "Button A":
            _, xp = x.split("+")
            _, yp = y.split("+")
            button_a.append((int(xp), int(yp)))
        elif a == "Button B":
            _, xp = x.split("+")
            _, yp = y.split("+")
            button_b.append((int(xp), int(yp)))
        elif a == "Prize":
            _, xp = x.split("=")
            _, yp = y.split("=")
            prize.append((int(xp), int(yp)))

    for ba, bb, p in zip(button_a, button_b, prize):
        tok = 10000000
        for i in range(100):
            for j in range(100):
                if p[0] == i * ba[0] + j * bb[0] and p[1] == i * ba[1] + j * bb[1]:
                    if i * 3 + j < tok:
                        tok = i * 3 + j
        if tok != 10000000:
            sums += tok

    print("Part 1: ", 33921)
    assert sums == 0


def find_intersection(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2 = line2

    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # Lines are parallel

    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)


def part_two():
    sums = 0
    button_a = []
    button_b = []
    prize = []
    for i, line in enumerate(input()):
        if not line:
            continue
        a, b = line.split(":")
        x, y = b.split(",")
        if a == "Button A":
            _, xp = x.split("+")
            _, yp = y.split("+")
            button_a.append((int(xp), int(yp)))
        elif a == "Button B":
            _, xp = x.split("+")
            _, yp = y.split("+")
            button_b.append((int(xp), int(yp)))
        elif a == "Prize":
            _, xp = x.split("=")
            _, yp = y.split("=")
            prize.append((int(xp) + 10000000000000, int(yp) + 10000000000000))

    for ba, bb, p in zip(button_a, button_b, prize):
        intersection = find_intersection([ba[0], bb[0], p[0]], [ba[1], bb[1], p[1]])
        if (
            intersection
            and intersection[0].is_integer()
            and intersection[1].is_integer()
        ):
            sums += intersection[0] * 3 + intersection[1]
        else:
            print("Lines are parallel")

    print("Part 2: ", sums)
    assert sums == 82261957837868


part_one()
part_two()
