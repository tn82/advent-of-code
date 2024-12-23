import os
import networkx as nx

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    cons = []
    graph = nx.Graph()
    for i, line in enumerate(input()):
        c1, c2 = line.split("-")
        if True or c1.startswith("t") or c2.startswith("t"):
            cons.append(line.split("-"))
            graph.add_edge(c1, c2)
            graph.add_edge(c2, c1)
    
    sums = 0
    for c in list(nx.simple_cycles(graph,length_bound=3)):
        if len(c) != 3:
            continue
        c1, c2, c3 = c
        if c1.startswith("t") or c2.startswith("t") or c3.startswith("t"):
            print(c)
            sums+=1

    print("Part 1: ", sums)
    assert(sums == 1370)

def find_longest_clique(graph):
    lan_cycle = []
    for component in list(nx.find_cliques(graph)):
        if len(component) > len(lan_cycle):
            lan_cycle = component
    return lan_cycle

def part_two():
    graph = nx.Graph()
    for _, line in enumerate(input()):
        c1, c2 = line.split("-")
        graph.add_edge(c1, c2)
        graph.add_edge(c2, c1)
    
    lan_cycle = find_longest_clique(graph)
    lan_cycle = ",".join(sorted(lan_cycle))
    print("Part 2: ", lan_cycle)
    assert(lan_cycle == "co,de,ka,ta")



#part_one()
part_two()