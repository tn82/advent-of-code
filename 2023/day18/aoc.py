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

def grid_printer(grid, xmin, xmax, ymin, ymax):
    row = xmin
    for x in range(xmin, xmax + 1):
        if x != row:
            print()
            row = x
        for y in range(ymin, ymax + 1):
            if (x, y) in grid:
                print(grid[(x, y)], end = "")
            else:
                print(".", end = "")
    print()
    print()

visited_glob = {}
visited_no_glob = {}

def inside(grid, x, y, xmin, xmax, ymin, ymax):
    q = [(x, y)]
    visited = {}
    visited.update(visited_glob)
    visited[(x, y)] = 1
    while q:
        xq, yq = q.pop()
        if (xq, yq) in visited_no_glob:
            return False
        if (xq + 1, yq) not in visited:
            visited[(xq + 1, yq)] = 1
            if (xq + 1, yq) not in grid:
                if xq + 1 > xmax:
                    #visited_no_glob.update(visited)
                    return False
                q.append((xq + 1, yq))
        if (xq - 1, yq) not in visited:
            visited[(xq - 1, yq)] = 1
            if (xq - 1, yq) not in grid:
                if xq - 1 < xmin:
                    #visited_no_glob.update(visited)
                    return False
                q.append((xq - 1, yq))
        if (xq, yq + 1) not in visited:
            visited[(xq, yq + 1)] = 1
            if (xq, yq + 1) not in grid:
                if yq + 1 > ymax:
                    #visited_no_glob.update(visited)
                    return False
                q.append((xq, yq + 1))
        if (xq, yq - 1) not in visited:
            visited[(xq, yq - 1)] = 1
            if (xq, yq - 1) not in grid:
                if yq - 1 < ymin:
                    #visited_no_glob.update(visited)
                    return False
                q.append((xq, yq - 1))
    visited_glob.update(visited)
    return True


def counter(grid, xmin, xmax, ymin, ymax):
    cc = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if (x, y) in grid:
                cc += 1
            else:
                if inside(grid, x, y, xmin, xmax, ymin, ymax):
                    cc += 1

    return cc


def part_one():
    sums = 0
    x = 0
    y = 0
    grid = {}
    grid[(x, y)] = 1
    xmax = -1000
    ymax = -1000
    xmin = 1000
    ymin = 1000
    for i, line in enumerate(input()):
        d, c, _ = line.split()
        if d == "L":
            jx = 0
            jy = -1
        elif d == "R":
            jx = 0
            jy = 1
        elif d == "D":
            jx = -1
            jy = 0
        elif d == "U":
            jx = 1
            jy = 0
        for i in range(int(c)):
            x += jx
            y += jy
            grid[(x, y)] = 1
            if x > xmax:
                xmax = x
            if y > ymax:
                ymax = y
            if x < xmin:
                xmin = x
            if y < ymin:
                ymin = y

    #grid_printer(grid, xmin, xmax, ymin, ymax)
    cc = counter(grid, xmin, xmax, ymin, ymax)
    print("Part 1: ", cc)
    assert(sums == 42317)


def polygon_area(xy):
    # A function to apply the Shoelace algorithm
    sum1 = 0
    sum2 = 0
    
    for i in range(0, len(xy) - 1):
        delta1 = 0
        if xy[i][0] != 0 and xy[i+1][1] != 0:
            delta1 = 0
        sum1 += (xy[i][0] + delta1) * (xy[i+1][1] + delta1)
        
        delta2 = 0
        if xy[i][1] != 0 and xy[i+1][0] != 0:
            delta2 = 0
        sum2 += (xy[i][1] + delta2) * (xy[i+1][0] + delta2)
    
    #Add xn.y1
    sum1 += (xy[len(xy) - 1][0] + 0) * (xy[0][1] + 0)
    #Add x1.yn
    sum2 += (xy[0][0] + 0) * (xy[len(xy) - 1][1] + 0)
    
    area = abs(sum1 - sum2) / 2
    return area

def part_two():
    sums = 0
    x = 0
    y = 0

    xy = [(x, y)]
    inmp = input()
    total_len = 0
    for i, line in enumerate(inmp):
        d, c, color = line.split()
        c = int(color[2:7], 16)
        d1 = int(color[7:8])

        if d1 == 2:
            d = "L"
        elif d1 == 0:
            d = "R"
        elif d1 == 1:
            d = "D"
        elif d1 == 3:
            d = "U"
        if d == "L":
            jx = 0
            jy = -1
        elif d == "R":
            jx = 0
            jy = 1
        elif d == "D":
            jx = -1
            jy = 0
        elif d == "U":
            jx = 1
            jy = 0

        x += jx * int(c)
        y += jy * int(c)
        xy.append((x, y))
        total_len += int(c)

    sums = int(polygon_area(xy) + total_len / 2 + 1)

    print("Part 1: ", sums)
    assert(sums == 83605563360288)


#part_one()
part_two()