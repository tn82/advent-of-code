import networkx as nx
import matplotlib.pyplot as plt
import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    graph = nx.Graph()
    for i, line in enumerate(input()):
        c1, cs = line.split(":")
        for c in cs.split():
            graph.add_edge(c1, c)
            graph.add_edge(c, c1)

    nx.draw(graph, cmap = plt.get_cmap('jet'), with_labels=True)
    plt.show()
    print("Part 1: ", 0)

part_one()
