def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]



def best_flow_path(cur, time, valves, dist, flows, graph, visited):
    visited = visited.copy()
    visited.add(cur)
    best_visited = visited.copy()
    valves = valves - visited

    best_flow = 0
    for valve in valves:
        # Jump to valve and open (any valve and no concept of not open)
        time_left = time - dist[(cur, valve)] - 1
        if time_left > 0:
            flow = flows[valve] * time_left
            flow_, visited_ = best_flow_path(valve, time_left, valves, dist, flows, graph, visited)
            flow += flow_
            if flow > best_flow:
                best_flow = flow
                best_visited = visited_.copy()
    return best_flow, best_visited

def valve_distance(graph, valves):
    distances = {}
    for valve in valves:
        cur = set([valve,])
        next = set()
        dist = 0
        while cur:
            dist += 1
            for pos in cur:
                for n in graph[pos]:
                    if (valve, n) not in distances:
                        distances[(valve, n)] = dist
                        next.add(n)
            cur = next
            next = set()

    return distances


def day16():
    graph = {} 
    flows = {}
    for line in input():
        line = line.replace("Valve ", "")
        line = line.replace(" has flow rate", "")
        line = line.replace(" tunnels lead to valves ", "")
        line = line.replace(" tunnel leads to valve ", "")
        v, m = line.split(";")
        valve, flow = v.split("=")
        flow = int(flow)
        nodes = m.split(", ")
        graph[valve] = nodes
        flows[valve] = flow

    valves = {k for k in graph.keys() if flows[k] > 0 or k == "AA"}
    dist = valve_distance(graph, valves)
    visited = set()
    best_flow, best_visited = best_flow_path("AA", 30, valves.copy(), dist, flows, graph, visited)
    print("Part 1: ", best_flow)
    assert best_flow == 1720

    visited = set()
    best_flow, best_visited = best_flow_path("AA", 26, valves.copy(), dist, flows, graph, visited)
    print(best_flow, len(best_visited), len(valves))
    best_flow_ele, best_visited = best_flow_path("AA", 26, valves.copy(), dist, flows, graph, best_visited)
    print("Part 2: ", best_flow + best_flow_ele)
    assert best_flow + best_flow_ele == 2582


day16()
