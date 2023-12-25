import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

import networkx as nx
import matplotlib.pyplot as plt

def part_one():
    sums = 0
    grid = defaultdict(list)
    graph = nx.Graph()
    for i, line in enumerate(input()):
        c1, cs = line.split(":")
        for c in cs.split():
            if c == "jjn" and c1 == "nhg" or c1 == "jjn" and c == "nhg":
                continue
            if c == "lms" and c1 == "tmc" or c1 == "lms" and c == "tmc":
                continue
            if c == "txf" and c1 == "xnn" or c1 == "txf" and c == "xnn":
                continue
            grid[c1].append(c)
            grid[c].append(c1)
            graph.add_edge(c1, c)
            graph.add_edge(c, c1)

    dcs = list(nx.chain_decomposition(graph))
    dcs.sort(key = lambda x: len(x), reverse=True)

    q = ["tmd"]
    visited = set()
    while q:
        node = q.pop()
        visited.add(node)
        for n in grid[node]:
            if n in visited:
                continue
            q.append(n)
    print(len(visited))
    q = ["skv"]
    visited = set()
    while q:
        node = q.pop()
        visited.add(node)
        for n in grid[node]:
            if n in visited:
                continue
            q.append(n)
    print(len(visited))

    nx.draw(graph, cmap = plt.get_cmap('jet'), with_labels=True )
    plt.show()
    print("Part 1: ", sums)

    #assert(sums == 0)

part_one()
