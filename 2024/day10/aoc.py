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
    return [-1 if c == "." else int(c) for c in char_list]

def dfs(grid, r, c, find_unique, result, visited=None):
    if visited is None:
        visited = set()
    if find_unique and (r, c) in visited:
        return visited
    visited.add((r, c))
    if grid[(r, c)] == 9:
        result["count"] += 1
        return visited

    for jump in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        rj, cj = jump
        if (r + rj, c + cj) in grid and grid[(r + rj, c + cj)] == grid[(r, c)] + 1:
            dfs(grid, r + rj, c + cj, find_unique, result, visited)
    return visited


def bfs(grid, r, c, find_unique, result):
    visited = set()
    visited.add((r, c))
    queue = []
    queue.append((r, c))

    while queue:
        rq, cq = queue.pop(0)
        if grid[(rq, cq)] == 9:
            result["count"] += 1
            continue

        for jump in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rj, cj = jump
            if find_unique and (rq + rj, cq + cj) in visited:
                continue
            if (rq + rj, cq + cj) in grid and grid[(rq + rj, cq + cj)] == grid[
                (rq, cq)
            ] + 1:
                visited.add((rq + rj, cq + cj))
                queue.append((rq + rj, cq + cj))


def part_one():
    grid = {}
    for row, line in enumerate(input()):
        for col, c in enumerate(int_list(line)):
            grid[(row, col)] = c

    result = {"count": 0}
    for r in range(row + 1):
        for c in range(col + 1):
            if grid[(r, c)] != 0:
                continue
            bfs(grid, r, c, True, result)

    print("Part 1: ", result["count"])
    assert result["count"] == 629


def part_two():
    grid = {}
    for row, line in enumerate(input()):
        for col, c in enumerate(int_list(line)):
            grid[(row, col)] = c

    result = {"count": 0}
    for r in range(row + 1):
        for c in range(col + 1):
            if grid[(r, c)] != 0:
                continue
            bfs(grid, r, c, False, result)

    print("Part 2: ", result["count"])
    assert result["count"] == 1242


part_one()
part_two()
