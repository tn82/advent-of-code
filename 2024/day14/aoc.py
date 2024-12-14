import os
from collections import defaultdict
from time import sleep

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
    points = []
    velo = []
    for i, line in enumerate(input()):
        p, v = line.split()
        _, p2 = p.split("=")
        p3, p4 = p2.split(",")
        points.append((int(p3), int(p4)))

        _, v2 = v.split("=")
        v3, v4 = v2.split(",")
        velo.append((int(v3), int(v4)))

    xs = 101
    # xs = 11

    ys = 103
    # ys = 7

    for t in range(100):
        pointsn = []
        for p, v in zip(points, velo):
            xn = (p[0] + v[0]) % xs
            yn = (p[1] + v[1]) % ys
            pointsn.append((xn, yn))
        points = pointsn

    q1, q2, q3, q4 = 0, 0, 0, 0
    for p in points:
        if p[0] < xs / 2 - 1 and p[1] < ys / 2 - 1:
            q1 += 1
        elif p[0] < xs / 2 - 1 and p[1] > ys / 2:
            q2 += 1
        elif p[0] > xs / 2 and p[1] < ys / 2 - 1:
            q3 += 1
        elif p[0] > xs / 2 and p[1] > ys / 2:
            q4 += 1

    print("Part 1: ", q1 * q2 * q3 * q4)
    assert q1 * q2 * q3 * q4 == 218295000


def grid_printer(grid):
    row = 0
    for coo, v in grid.items():
        r, c = coo
        if r != row:
            print()
            row = r
        print(v, end="")

    print()
    print()


def printer(points):
    max_x = max(coord[0] for coord in points)
    max_y = max(coord[1] for coord in points)
    grid = []
    for _ in range(max_y + 1):
        grid.append("." * (max_x + 1))
    for p in points:
        s = grid[p[1]]
        s = s[: p[0]] + "#" + s[p[0] + 1 :]
        grid[p[1]] = s
    for g in grid:
        print(g)


def part_two():
    points = []
    velo = []
    for i, line in enumerate(input()):
        p, v = line.split()
        _, p2 = p.split("=")
        p3, p4 = p2.split(",")
        points.append((int(p3), int(p4)))

        _, v2 = v.split("=")
        v3, v4 = v2.split(",")
        velo.append((int(v3), int(v4)))

    xs = 101
    ys = 103
    for t in range(10000):
        pointsn = []
        for p, v in zip(points, velo):
            xn = (p[0] + v[0]) % xs
            yn = (p[1] + v[1]) % ys
            pointsn.append((xn, yn))
        points = pointsn

        q_middle = 0
        for p in points:
            if xs / 3 < p[0] < xs * 2 / 3 and ys / 3 < p[1] < ys * 2 / 3:
                q_middle += 1

        if q_middle > len(points) / 2:
            printer(points)
            break

    print("Part 2: ", t + 1)
    assert(t + 1 == 6870)


part_one()
part_two()
