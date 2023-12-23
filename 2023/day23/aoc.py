import os
from collections import defaultdict
import heapq

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def grid_input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        grid = [list(r) for r in file.read().strip().split("\n")]
        n, m = len(grid), len(grid[0])
        return grid, n, m

def grid_test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        grid = [list(r) for r in file.read().strip().split("\n")]
        n, m = len(grid), len(grid[0])
        return grid, n, m

def part_one():
    grid = {}
    xmax = 0
    ymax = 0
    for i, line in enumerate(reversed(input())):
        for j, v in enumerate(line):
            grid[(i, j)] = v
            if i > xmax:
                xmax = i
            if j > ymax:
                ymax = j

    long_grid = {}
    best_global = 0
    q = [[(xmax, 1, ".")]] # start
    while q:
        path = heapq.heappop(q)
        x = path[-1][0]
        y = path[-1][1]
        d = path[-1][2]
        if d == ".":
            shifts = ((1, 0), (0, 1), (0, -1), (-1, 0))
        if d == ">":
            shifts = ((0, 1),)
        if d == "<":
            shifts = ((0, -1),)
        if d == "^":
            shifts = ((1, 0),)
        if d == "v":
            shifts = ((-1, 0),)
        for shift in shifts:
            sx, sy = shift
            if not (x + sx, y + sy) in grid:
                continue
            if grid[(x + sx, y + sy)] == "#":
                continue
            if len(path) > 1 and (x + sx, y + sy) == (path[-2][0], path[-2][1]):
                continue
            if (x + sx, y + sy, grid[(x + sx, y + sy)]) in path:
                continue
            new_path = path + [(x + sx, y + sy, grid[(x + sx, y + sy)])]
            
            if (x + sx, y + sy) in long_grid and long_grid[(x + sx, y + sy)] > len(path):
                continue
            long_grid[(x + sx, y + sy, grid[(x + sx, y + sy)])] = len(new_path)
            heapq.heappush(q, new_path)

            if x + sx == 0 and y + sy == ymax - 1 and len(new_path) > best_global:
                best_global = len(new_path)
                print(len(q), len(new_path))
    print("Part 1: ", best_global - 1)
    assert(best_global - 1 == 2214)

def coo_shifts(coo, grid, n, m):
    x, y = coo
    coo_new = []
    for dx, dy in ((1, 0), (0, 1), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if nx in range(n) and ny in range(m) and grid[nx][ny] != "#":
            coo_new.append((nx, ny))
    return coo_new

def part_two():
    grid, n, m = grid_input()

    # Find points with more than 2 directions
    nodes = set()
    for x in range(n):
        for y in range(m):
            if grid[x][y] != "#":
                if len(coo_shifts((x, y), grid, n, m)) > 2:
                    nodes.add((x, y))
    nodes.add((0, 1)) # start
    nodes.add((n - 1, m - 2)) # goal

    # Build graph with distance
    graph = defaultdict(list)
    for x, y in nodes:
        q = []
        q.append((x,y))
        seen = {(x,y)}
        dist = 0
        while len(q) > 0:
            # Step until we find another node
            new_q = []
            dist += 1
            for coo in q:
                for coos in coo_shifts(coo, grid, n, m):
                    if coos not in seen:
                        if coos in nodes:
                            graph[(x, y)].append((dist, coos))
                            seen.add(coos)
                        else:
                            seen.add(coos)
                            new_q.append(coos)
            q = new_q

    best_global = 0
    q = [[(0, 1), 0, [(0, 1)]]] # start
    while q:
        node, dist, path = q.pop()
        any = False
        for next_dist, next_node in graph[node]:
            if next_node in path:
                continue
            if next_node == (n - 1, m - 2):
                if dist + next_dist > best_global:
                    best_global = dist + next_dist
                print(len(q), dist + next_dist, best_global)
                continue
            q.append((next_node, dist + next_dist, path + [next_node]))

    print("Part 1: ", best_global)
    assert(best_global == 6594)

part_one()
part_two()