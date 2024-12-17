import os
from collections import defaultdict
import heapq
import copy

day_path = os.path.dirname(__file__)


def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]


def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]


def int_list(char_list):
    return [int(c) for c in char_list]


def input_raw():
    with open(os.path.join(day_path, "input.txt"), "r") as f:
        return f.read().strip()


def test_raw():
    with open(os.path.join(day_path, "test.txt"), "r") as f:
        return f.read().strip()


def counter_clockwise(x, y):
    return (-y, x)


def clockwise(x, y):
    return (y, -x)


def dijkstra(grid, sx, sy):
    distances = {}
    distances[(sx, sy, 0, 1)] = 0
    distances2 = defaultdict(int)
    distances2[(sx, sy, 0, 1)] = 0
    visited = set()
    priority_queue = [(0, 0, (sx, sy, 0, 1))]  # (distance, steps, node)

    # curr_dir = (0, 1)

    while priority_queue:
        current_distance, current_steps, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        curr_dir = (current_node[2], current_node[3])
        for dir, weight in [
            (curr_dir, 1),
            (counter_clockwise(curr_dir[0], curr_dir[1]), 1000),
            (clockwise(curr_dir[0], curr_dir[1]), 1000),
        ]:
            if weight == 1:
                if grid[(current_node[0] + dir[0], current_node[1] + dir[1])] == "#":
                    continue
                neighbor = (
                    current_node[0] + dir[0],
                    current_node[1] + dir[1],
                    dir[0],
                    dir[1],
                )
            if weight == 1000:
                # if grid[(current_node[0] + dir[0], current_node[1] + dir[1])] == "#":
                #    continue
                neighbor = (current_node[0], current_node[1], dir[0], dir[1])
                # neighbor = (current_node[0] + dir[0], current_node[1] + dir[1], dir[0], dir[1])
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances2[neighbor] = current_steps + 1
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, current_steps + 1, neighbor))

    return distances, distances2


def part_one():
    sums = 1000000000
    grid = {}
    sx, sy = 0, 0
    ex, ey = 0, 0
    for x, line in enumerate(input_raw().split("\n")):
        for y, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                sx = x
                sy = y
            if c == "E":
                ex = x
                ey = y

    distances, distances2 = dijkstra(grid, sx, sy)
    edistances = {}
    steps = 0
    for coo, d in distances.items():
        if coo[0] == ex and coo[1] == ey:
            edistances[coo] = d
            # steps += distances2[coo]

    for coo, d in distances.items():
        if coo[0] == ex and coo[1] == ey and d <= sums:
            sums = d
    for coo, d in distances.items():
        if coo[0] == ex and coo[1] == ey and d == sums:
            steps += distances2[coo]

    # steps += distances2[coo]
    print("Part 1: ", sums)
    print("Part 2: ", steps)

    # assert(sums == 0)


def grid_dijkstra_shortest_path(grid, sx, sy, ex, ey):
    def neighbor_weights(grid, curr_node):
        nw = []
        x, y, dx, dy = curr_node
        if grid[(curr_node[0] + dx, curr_node[1] + dy)] != "#":
            # Move +dx +dy. Keep direction the same.
            weight = 1
            nw.append(((x + dx, y + dy, dx, dy), weight))
        weight = 1000       
        # No move only spin
        dx_cc, dy_cc = counter_clockwise(dx, dy)
        nw.append(((x, y, dx_cc, dy_cc), weight))

        # No move only spin
        dx_c, dy_c = clockwise(dx, dy)
        nw.append(((x, y, dx_c, dy_c), weight))
        return nw

    distances = {}
    distances[(sx, sy, 1, 0)] = 0
    visited = set()
    priority_queue = [(0, (sx, sy, 1, 0))]  # (distance, node)

    predecessors = defaultdict(list)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in neighbor_weights(grid, current_node):
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = [current_node]  # New shortest path
                heapq.heappush(priority_queue, (distance, neighbor))
            elif neighbor in distances and distance == distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor].append(current_node)  # Another shortest path
                heapq.heappush(priority_queue, (distance, neighbor))

    paths = []

    def build_paths(node, path):
        if node == (sx, sy, 1, 0):
            paths.append(path[::-1])  # Reverse the path
            return
        for predecessor in predecessors[node]:
            build_paths(predecessor, path + [predecessor])

    build_paths((ex, ey, 1, 0), [(ex, ey, 1, 0)])
    return distances, paths


def grid_dijkstra(grid, sx, sy, ex, ey):
    distances = {}
    distances[(sx, sy, 1, 0)] = 0
    visited = set()
    priority_queue = [(0, [(sx, sy, 1, 0)], (sx, sy, 1, 0))]  # (distance, steps, node)

    predecessors = defaultdict(list)

    end_steps = []
    while priority_queue:
        current_distance, current_steps, current_node = heapq.heappop(priority_queue)

        if current_node[0] == ex and current_node[1] == ey:
            end_steps += current_steps
            # break  # Found shortest path to end node

        # if current_node in visited:
        #    continue
        # visited.add(current_node)

        if tuple(current_steps) in visited:
            continue
        if current_distance > 66404:
            continue
        visited.add(tuple(current_steps))

        curr_dir = (current_node[2], current_node[3])
        for dir, weight in [
            (curr_dir, 1),
            (counter_clockwise(curr_dir[0], curr_dir[1]), 1000),
            (clockwise(curr_dir[0], curr_dir[1]), 1000),
        ]:
            if weight == 1:
                if grid[(current_node[0] + dir[0], current_node[1] + dir[1])] == "#":
                    continue
                neighbor = (
                    current_node[0] + dir[0],
                    current_node[1] + dir[1],
                    dir[0],
                    dir[1],
                )
            if weight == 1000:
                neighbor = (current_node[0], current_node[1], dir[0], dir[1])
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                neighbor_steps = copy.copy(current_steps)
                neighbor_steps.append(neighbor)
                distances[neighbor] = distance
                predecessors[neighbor] = [current_node]  # New shortest path
                heapq.heappush(priority_queue, (distance, neighbor_steps, neighbor))
            elif neighbor in distances and distance == distances[neighbor]:
                neighbor_steps = copy.copy(current_steps)
                neighbor_steps.append(neighbor)
                distances[neighbor] = distance
                predecessors[neighbor].append(current_node)  # Another shortest path
                heapq.heappush(priority_queue, (distance, neighbor_steps, neighbor))

    ss = set()
    for s in end_steps:
        ss.add((s[0], s[1]))
    unique_nodes = len(ss)

    paths = []

    def build_paths(node, path):
        if node == (sx, sy, 1, 0):
            paths.append(path[::-1])  # Reverse the path
            return
        for predecessor in predecessors[node]:
            build_paths(predecessor, path + [predecessor])

    build_paths((ex, ey, 1, 0), [(ex, ey, 1, 0)])
    return distances, unique_nodes, paths

def neighbor_weights(grid, curr_node):
    nw = []
    x, y, dx, dy = curr_node
    if grid[(curr_node[0] + dx, curr_node[1] + dy)] != "#":
        # Move +dx +dy. Keep direction the same.
        weight = 1
        nw.append(((x + dx, y + dy, dx, dy), weight))
    weight = 1000       
    # No move only spin
    dx_cc, dy_cc = counter_clockwise(dx, dy)
    nw.append(((x, y, dx_cc, dy_cc), weight))

    # No move only spin
    dx_c, dy_c = clockwise(dx, dy)
    nw.append(((x, y, dx_c, dy_c), weight))
    return nw

def dijkstra_grid_single_path(grid, start, end):
    distances = {}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)
    previous_nodes = {}
    previous_nodes[start] = None

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if (current_node[0], current_node[1]) == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return current_distance, path[::-1]  # Reverse the path

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in neighbor_weights(grid, current_node):
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return float("inf"), []  # No path found


def part_two2():
    sums = 1000000000
    grid = {}
    sx, sy = 0, 0
    ex, ey = 0, 0
    # for y, line in enumerate(test_raw().split("\n")):
    for y, line in enumerate(input_raw().split("\n")):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                sx = x
                sy = y
            if c == "E":
                ex = x
                ey = y

    distances, paths = dijkstra_grid_single_path(grid, (sx, sy, 1, 0), (ex, ey))
    #distances, paths = grid_dijkstra_shortest_path(grid, sx, sy, ex, ey)

    ss = set()
    for path in paths:
        for s in path:
            ss.add((s[0], s[1]))
    part2 = len(ss)
    print(part2)

    edistances = {}
    for coo, d in distances.items():
        if coo[0] == ex and coo[1] == ey:
            edistances[coo] = d

    part1 = 1000000000
    for coo, d in distances.items():
        if coo[0] == ex and coo[1] == ey and d <= part1:
            part1 = d
    ss = set()

    # steps += distances2[coo]
    print("Part 1: ", part1)
    assert part1 == 66404

    print("Part 2: ", unique_nodes)
    assert unique_nodes == 433


def part_two():
    sums = 1000000000
    grid = {}
    sx, sy = 0, 0
    ex, ey = 0, 0
    # for y, line in enumerate(test_raw().split("\n")):
    for y, line in enumerate(input_raw().split("\n")):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                sx = x
                sy = y
            if c == "E":
                ex = x
                ey = y

    distances, unique_nodes, paths = grid_dijkstra(grid, sx, sy, ex, ey)
    distances, paths = grid_dijkstra_shortest_path(grid, sx, sy, ex, ey)

    ss = set()
    for path in paths:
        for s in path:
            ss.add((s[0], s[1]))
    part2 = len(ss)
    print(part2)

    edistances = {}
    for coo, d in distances.items():
        if coo[0] == ex and coo[1] == ey:
            edistances[coo] = d

    part1 = 1000000000
    for coo, d in distances.items():
        if coo[0] == ex and coo[1] == ey and d <= part1:
            part1 = d
    ss = set()

    # steps += distances2[coo]
    print("Part 1: ", part1)
    assert part1 == 66404

    print("Part 2: ", unique_nodes)
    assert unique_nodes == 433


# part_one()
part_two2()
