import os
from collections import defaultdict
import heapq
import copy
#from functools import cache

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]

from dataclasses import dataclass

@dataclass
class Mashine:
    lamps_goal: [int]
    lamps: [int]
    buttons: [[int]]
    jolt_goal: [int]
    jolt: [int]

def bfs_break(machine, m):
    if m == machine.lamps_goal:
        return True
    else:
        return False

def pushes(machine, m):
    ps = []
    for b in machine.buttons:
        m_new = copy.copy(m)
        for bi in b:
            m_new[bi] = 0 if m_new[bi] == 1 else 1
        ps.append(m_new)

    return ps


def bfs(machine, visited, queue, graph, node):
    #visited.append(node)
    queue.append((0,None, node))

    while queue:
        count, prev, m = queue.pop(0)

        if bfs_break(machine, m):
            return count

        for i, neighbour in enumerate(pushes(machine, m)):
            if machine.buttons[i] == prev:
                continue
            queue.append((count+1, machine.buttons[i], neighbour))

def part_one():
    sums = 0
    mapping = {'.': 0, '#': 1}
    machines = []
    for i, line in enumerate(test()):
        m = Mashine([], [], [], [], [])
        for comp in line.split(" "):
            if "." in comp or "#" in comp:
                comp = comp[1:]
                comp = comp[:-1]
                m.lamps_goal= [mapping.get(char, 0) for char in comp]
            if "(" in comp:
                for c in comp.split(" "):
                    comp = comp[1:]
                    comp = comp[:-1]
                    m.buttons.append([int(c) for c in comp.split(",")])
        m.lamps = [0] * len(m.lamps_goal)
        machines.append(m)

    for i, m in enumerate(machines):
        graph = {}
        visited = set()  # Visited nodes
        queue = []  # Initialize a queue

        res = bfs(m, visited, queue, graph, copy.copy(m.lamps))  # function calling
        print("Res: ", i, res)
        sums += res



    print("Part 1: ", sums)
    assert(sums == 571)


def bfs_break2(machine, m):
    if m == machine.jolt_goal:
        return True
    else:
        return False

def pushes2(machine, m):
    ps = []
    for b in machine.buttons:
        m_new = copy.copy(m)
        ok = True
        for bi in b:
            m_new[bi] = m[bi] + 1
            if m_new[bi] > machine.jolt_goal[bi]:
                ok = False
        if ok:
            ps.append(m_new)

    return ps


def bfs2(machine, visited, queue, graph, node):
    #visited.append(node)
    states = {}
    queue.append((0, node))

    while queue:
        count, m = queue.pop(0)

        if bfs_break2(machine, m):
            return count

        for i, neighbour in enumerate(pushes2(machine, m)):
            ok = True
            if tuple(neighbour) in states:
                if states[tuple(neighbour)] <= count+1:
                    continue
            states[tuple(neighbour)] = count+1       
            queue.append((count+1, neighbour))

def part_two():
    sums = 0
    mapping = {'.': 0, '#': 1}
    machines = []
    for i, line in enumerate(input()):
        m = Mashine([], [], [], [], [])
        for comp in line.split(" "):
            if "{" in comp:
                comp = comp[1:]
                comp = comp[:-1]
                m.jolt_goal = [int(c) for c in comp.split(",")]
            if "(" in comp:
                for c in comp.split(" "):
                    comp = comp[1:]
                    comp = comp[:-1]
                    m.buttons.append([int(c) for c in comp.split(",")])
        m.jolt = [0] * len(m.jolt_goal)
        machines.append(m)

    for i, m in enumerate(machines):
        graph = {}
        visited = set()  # Visited nodes
        queue = []  # Initialize a queue

        res = bfs2(m, visited, queue, graph, copy.copy(m.jolt))  # function calling
        print("Res: ", i, res)
        sums += res


    print("Part 2: ", sums)
    #assert(sums == 0)

from z3 import *

def part_two2():
    sums = 0
    mapping = {'.': 0, '#': 1}
    machines = []
    for i, line in enumerate(input()):
        m = Mashine([], [], [], [], [])
        for comp in line.split(" "):
            if "{" in comp:
                comp = comp[1:]
                comp = comp[:-1]
                m.jolt_goal = [int(c) for c in comp.split(",")]
            if "(" in comp:
                for c in comp.split(" "):
                    comp = comp[1:]
                    comp = comp[:-1]
                    m.buttons.append([int(c) for c in comp.split(",")])
        m.jolt = [0] * len(m.jolt_goal)
        machines.append(m)

    for i, m in enumerate(machines):
        opt = Optimize()
        x = IntVector('x', len(m.buttons))
        for xi in x:
            opt.add(xi >= 0)

        for j, y in enumerate(m.jolt_goal):
            coef = [0] * len(m.buttons)
            for bi, b in enumerate(m.buttons):
                if j in b:
                    coef[bi] = 1
            opt.add(Sum([xi * c for xi, c in zip(x, coef)]) == y)

        sum_x = Sum(x) 
        h = opt.minimize(sum_x)
        if opt.check() == sat:
            m = opt.model()
            ms = 0
            for mi in m:
                ms += m[mi].as_long()
            sums += ms
            print(ms)





    print("Part 2: ", sums)
    #assert(sums == 0)
    # too high 21494

#part_one()
part_two2()