import os
from collections import defaultdict
import heapq
import copy
from functools import cache
import networkx as nx


day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]

@cache
def dist(p1, p2):
    return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2) + pow(p1[2] - p2[2], 2)

def in_the_same_circut(circuts, p1, p2):
    for circut in nx.connected_components(circuts):
        if p1 in circut and p2 in circut:
            return True
    return False

def find_nodes_not_connected(G, node1):
    """
    Returns a set of all nodes in G that are NOT in the same connected 
    component as node1.
    """
    
    # 1. Check if the starting node exists in the graph
    if node1 not in G:
        return set(G.nodes) # If node1 doesn't exist, all other nodes are "not connected"
    
    # 2. Find the set of nodes connected to node1
    connected_nodes = set()
    
    # nx.connected_components returns a generator of node sets
    for component_nodes in nx.connected_components(G):
        if node1 in component_nodes:
            connected_nodes = component_nodes
            # Once found, we can stop the loop
            break 
            
    # If the graph is empty, this set will be empty
    if not connected_nodes:
        return set(G.nodes)

    # 3. Calculate the difference: All Nodes - Connected Nodes
    all_nodes = set(G.nodes)
    nodes_not_connected = all_nodes - connected_nodes
    
    return nodes_not_connected

def part_one2():
    sums = 0
    pn = 10 # 1000 in prod
    points = []
    circuts = nx.Graph()
    for i, line in enumerate(test()):
        x, y, z = line.split(",")
        node = (int(x), int(y), int(z))
        points.append(node)
        circuts.add_node(node)


    alls = set()
    ii = 0
    for iss in range(10):
        cp1 = []
        cp2 = []
        cd = 1e10
        for i, p1 in enumerate(points):
            for p2 in find_nodes_not_connected(circuts, p1):
                d = dist(p1, p2)
                if d < cd:
                    cd = d
                    cp1 = p1
                    cp2 = p2
        circuts.add_edge(cp1, cp2)
        alls.add(cp1)
        alls.add(cp2)
        ii += 1 
        for circut in sorted(list(nx.connected_components(circuts)), key=len, reverse=True)[:3]:
            print(len(circut))
        print(iss, "-----")
        if ii == 100:
            break

def part_one():
    sums = 0
    pn = 10 # 1000 in prod
    points = []
    circuts = nx.Graph()
    circuts2 = nx.Graph()
    for i, line in enumerate(input()):
        x, y, z = line.split(",")
        node = (int(x), int(y), int(z))
        points.append(node)
        circuts.add_node(node)
        circuts2.add_node(node)


    alls = set()
    ii = 0
    for i in range(1000):
        cp1 = []
        cp2 = []
        cd = 1e10
        for i2, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i2 == j:
                    continue
                d = dist(p1, p2)
                if d < cd and not circuts.has_edge(p1, p2) and not circuts2.has_edge(p1, p2):
                    cd = d
                    cp1 = p1
                    cp2 = p2
        if nx.has_path(circuts, cp1, cp2):
            circuts2.add_edge(cp1, cp2)
            continue
        circuts.add_edge(cp1, cp2)
        ii += 1 
        #for circut in sorted(list(nx.connected_components(circuts)), key=len, reverse=True)[:3]:
        #    print(len(circut))
        print(i, "-----")


    for circut in sorted(list(nx.connected_components(circuts)), key=len, reverse=True):
        print(len(circut))
            




    print("Part 1: ", sums)
    #assert(sums == 175440)


def part_two():
    sums = 0
    pn = 10 # 1000 in prod
    points = []
    circuts = nx.Graph()
    circuts2 = nx.Graph()
    for i, line in enumerate(input()):
        x, y, z = line.split(",")
        node = (int(x), int(y), int(z))
        points.append(node)
        circuts.add_node(node)
        circuts2.add_node(node)


    alls = set()
    ii = 0
    for i in range(100000):
        cp1 = []
        cp2 = []
        cd = 1e10
        for i2, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i2 == j:
                    continue
                d = dist(p1, p2)
                if d < cd and not circuts.has_edge(p1, p2) and not circuts2.has_edge(p1, p2):
                    cd = d
                    cp1 = p1
                    cp2 = p2
        if nx.has_path(circuts, cp1, cp2):
            circuts2.add_edge(cp1, cp2)
            continue
        circuts.add_edge(cp1, cp2)
        ii += 1 
        #for circut in sorted(list(nx.connected_components(circuts)), key=len, reverse=True)[:3]:
        #    print(len(circut))
        c = len(list(nx.connected_components(circuts)))
        print(i, c)
        if c == 1:
            print(cp1, cp2)
            print(cp1[0] * cp2[0])
            break


    print("Part 2: ", sums)
    #assert(sums == 3200955921)


#part_one()
part_two()