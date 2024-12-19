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
    for line in test():
        sums += int(line)

    print("Part 1: ", sums)
    # assert(sums == 0)


def part_two():
    sums = 0
    for line in test():
        sums += int(line)

    print("Part 2: ", sums)
    # assert(sums == 0)


def in_grid(grid, r, c):
    # No diagonal shifts = ((1, 0), (0, 1), (0, -1), (-1, 0))
    # 3D shifts = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    # All directions
    shifts = ((1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1))
    for shift in shifts:
        coo = (r + shift[0], c + shift[1])
        if coo in grid and True:  # Add conditions
            return True
    return False


import math


def prime_factors(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes


from dataclasses import dataclass


@dataclass
class Monkey:
    name: str
    oper1: str


def bfs_break(m):
    if m == "8":
        return True
    else:
        return False


def bfs(visited, queue, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m)
        if bfs_break(m):
            return m

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# DFS algorithm
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)

    print(node)

    for neighbour in graph[node]:
        dfs(graph, neighbour, visited)
    return visited


def driver():
    graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
    visited = set()  # Visited nodes
    queue = []  # Initialize a queue
    # Driver Code
    print("Breadth-First Search")
    res = bfs(visited, queue, graph, "5")  # function calling
    print("Res: ", res)

    # Driver Code
    print("Breadth-First Search")
    res = bfs(visited, queue, graph, "5")  # function calling
    print("Res: ", res)


driver()


def rotate2D_clockwise(grid):
    return list(zip(*grid[::-1]))


def rotate_90_degrees_clockwise(x, y):
    return (y, -x)


def rotate_90_degrees_counter_clockwise(x, y):
    return (-y, x)


from functools import cache


# Depth-First Search with functools cache#
# Input must be
@cache
def dfs(group, sizes, num_done_in_group=0):
    if not group:
        if not sizes and num_done_in_group == 0:
            return 1
        else:
            return 0
    num_sols = 0
    neighbours = ["A", "B"]
    for neighbour in neighbours:
        if neighbour == "#":
            num_sols += dfs(group[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += dfs(group[1:], sizes[1:])
            else:
                num_sols += dfs(group[1:], sizes)
    return num_sols


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


# Add total length if 2D grid with end-point included
def polygon_area(xy):
    # A function to apply the Shoelace algorithm
    sum1 = 0
    sum2 = 0

    for i in range(0, len(xy) - 1):
        delta1 = 0
        if xy[i][0] != 0 and xy[i + 1][1] != 0:
            delta1 = 0
        sum1 += (xy[i][0] + delta1) * (xy[i + 1][1] + delta1)

        delta2 = 0
        if xy[i][1] != 0 and xy[i + 1][0] != 0:
            delta2 = 0
        sum2 += (xy[i][1] + delta2) * (xy[i + 1][0] + delta2)

    # Add xn.y1
    sum1 += (xy[len(xy) - 1][0] + 0) * (xy[0][1] + 0)
    # Add x1.yn
    sum2 += (xy[0][0] + 0) * (xy[len(xy) - 1][1] + 0)

    area = abs(sum1 - sum2) / 2
    return area

# join list to comma string
res = [1,2,3]
result_string = ",".join(map(str, res))