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
    #assert(sums == 0)

def part_two():
    sums = 0
    for line in test():
        sums += int(line)

    print("Part 2: ", sums)
    #assert(sums == 0)

def in_grid(grid, r, c):
    # No diagonal shifts = ((1, 0), (0, 1), (0, -1), (-1, 0))
    # 3D shifts = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    # All directions
    shifts = ((1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1))
    for shift in shifts:
        coo = (r + shift[0], c + shift[1])
        if coo in grid and True: # Add conditions
            return True
    return False

import math
def prime_factors(n):
    primes = []
    while n % 2 == 0: 
        primes.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i== 0: 
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

def bfs_driver():
    graph = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }
    visited = [] # List for visited nodes.
    queue = []     #Initialize a queue
    # Driver Code
    print("Breadth-First Search")
    res = bfs(visited, queue, graph, '5')    # function calling
    print("Res: ", res)

bfs_driver()
#part_one()
#part_two()