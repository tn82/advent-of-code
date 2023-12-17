import os
import heapq

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate(reversed(input())):
        for j, v in enumerate(line):
            grid[(i, j)] = int(v)
            if i > xmax:
                xmax = i
            if j > ymax:
                ymax = j

    q = [(0, xmax, 0, "S", 0)]
    best_grid = {}
    best_global = 0
    
    x = xmax
    y = 0
    while True:
        x -= 1
        best_global += grid[(x, y)]
        if x == 0 and y == ymax:
            break
        y += 1
        best_global += grid[(x, y)]
        if x == 0 and y == ymax:
            break
    best_global = 850

    while q:
        cost, sx, sy, sd, count = q.pop()
        directions = ("L", "R") if sd in ("U", "D") else ("U", "D")
        if sd == "S":
            directions = ("R", "D")
        for d in directions:        
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
        
            for i in range(1, 4):
                if not (sx + jx * i, sy + jy * i) in grid:
                    continue
                #if (sx + jx * i, sy + jy * i, d) in path:
                #    continue
                weight = 0
                for iw in range(1, i + 1):
                    weight += grid[(sx + jx * iw, sy + jy * iw)]
                if (sx + jx * i, sy + jy * i, d) in best_grid and best_grid[(sx + jx * i, sy + jy * i, d)] < cost + weight:
                    continue
                if cost + weight + sx + jx * i + (ymax - sy + jy * i) > best_global + 1:
                    continue
                best_grid[(sx + jx * i, sy + jy * i, d)] = cost + weight
                #new_path = path + [(sx + jx * i, sy + jy * i, d, cost + weight)]
                q.append((cost + weight, sx + jx * i, sy + jy * i, d, count + 1))
                if sx + jx * i == 0 and sy + jy * i == ymax:
                    best_global = cost + weight
                    print(count + 1, len(q), cost + weight)

    print("Part 1: ", best_global)
    assert(best_global == 847) # high 848 off by one?

def part_two():
    grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate(reversed(input())):
        for j, v in enumerate(line):
            grid[(i, j)] = int(v)
            if i > xmax:
                xmax = i
            if j > ymax:
                ymax = j

    #graph = networkx.DiGraph()
    #litt = defaultdict(set)
    paths = [[(xmax, 0, "x", 0)]]
    q = [[(xmax, 0, "x", 0)]]
    best_grid = {}
    best_global = 0
    
    x = xmax
    y = 0
    while True:
        for iw in range(1, 5):
            best_global += grid[(x - iw, y)]
        x -= 4
        if x == 0 and y == ymax:
            break
        for iw in range(1, 5):
            best_global += grid[(x, y + iw)]
        y += 4
        if x == 0 and y == ymax:
            break
    while q:
        path = q.pop()
        sx, sy, sd, cost = path[-1]
        for d in ("L", "R", "D", "U"):
            if d == sd:
                continue
            if sd == "L" and d == "R":
                continue
            if sd == "R" and d == "L":
                continue
            if sd == "U" and d == "D":
                continue
            if sd == "D" and d == "U":
                continue
        
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
        
            for i in range(4, 11):
                if not (sx + jx * i, sy + jy * i) in grid:
                    continue
                #if (sx + jx * i, sy + jy * i, d) in path:
                #    continue
                weight = 0
                for iw in range(1, i + 1):
                    weight += grid[(sx + jx * iw, sy + jy * iw)]
                if (sx + jx * i, sy + jy * i, d) in best_grid and best_grid[(sx + jx * i, sy + jy * i, d)] <= cost + weight:
                    continue
                if cost + weight + sx + jx * i + (ymax - sy + jy * i) > best_global + 1:
                    continue
                best_grid[(sx + jx * i, sy + jy * i, d)] = cost + weight
                new_path = path + [(sx + jx * i, sy + jy * i, d, cost + weight)]
                q.append(new_path)
                if sx + jx * i == 0 and sy + jy * i == ymax:
                    best_global = cost + weight
                    print(len(new_path), len(q), cost + weight)


part_one()
#part_two()