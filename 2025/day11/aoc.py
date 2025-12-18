import os
from collections import defaultdict
#import heapq
#import copy
from functools import cache
from frozendict import frozendict
import time

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]


def bfs(devs, node):
    #visited.append(node)
    queue = []
    queue.append(node)
    count = 0

    while queue:
        node = queue.pop(0)

        if node == "out":
            count += 1
            continue

        for neighbour in devs[node]:
            queue.append(neighbour)
    return count

def part_one():
    sums = 0
    devs = {}
    for i, line in enumerate(input()):
        dev_in, dev_out = line.split(":")
        dev_out = dev_out.lstrip()
        dev_out = dev_out.split(" ")
        devs[dev_in] = dev_out

    sums = bfs(devs, "you")
    print("Part 1: ", sums)
    assert(sums == 699)


def dfs(devs, node, node_end, visited):
    if node == node_end:
        return 1

    count_loc = 0
    for neighbour in devs[node]:
        if neighbour == "out" and node_end != "out":
            continue
        if neighbour in visited:
            count_loc += visited[neighbour]
            continue
        count_loc += dfs(devs, neighbour, node_end, visited)
    visited[node] = count_loc
    return count_loc



def bfs2(devs, node, node_end, visited):
    start_time = time.time()
    queue = []
    queue.append((node, 0))
    count2 = 0

    while queue:
        node, count = queue.pop(0)
        if node in visited:
            count2 += visited[node]
            continue
        if node == node_end:
            count2 += 1
            continue
        if node == "out":
            continue
        if time.time() - start_time > 0.5:
            return None

        for neighbour in devs[node]:
            queue.append((neighbour, count+1))
    return count2

def num_path(devs, start, end):
    visited = defaultdict(int)
    dfs(devs, start, end, visited)
    return visited[start]

def part_two():
    sums = 0
    devs = {}
    for i, line in enumerate(input()):
        dev_in, dev_out = line.split(":")
        dev_out = dev_out.lstrip()
        dev_out = dev_out.split(" ")
        devs[dev_in] = tuple(dev_out)
    
    sums = num_path(devs, "svr", "fft") * num_path(devs, "fft", "dac") * num_path(devs, "dac", "out")
    
    print("Part 2: ", sums)
    assert(sums == 388893655378800)


#part_one()
part_two()