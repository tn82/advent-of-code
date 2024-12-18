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


def neighbor_weights(grid, current_node):
    nw = []
    x, y = current_node
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        neighbor = x + dx, y + dy
        if (neighbor) not in grid or grid[(neighbor)] == "#":
            continue
        nw.append((neighbor, 1))
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

    return -1, []  # No path found


def part_one():
    points = []
    for i, line in enumerate(input()):
        points.append(tuple(int_list(line.split(","))))

    dims = 70 # 6 for test
    grid = {}
    for x in range(dims + 1):
        for y in range(dims + 1):
            grid[(x, y)] = "."

    for b in range(1024): # 12 in test
        grid[points[b]] = "#"
    cost, _ = dijkstra_grid_single_path(grid, (0, 0), (dims, dims))


    print("Part 1: ", cost)
    assert(cost == 234)


def part_two():
    points = []
    for i, line in enumerate(input()):
        points.append(tuple(int_list(line.split(","))))

    dims = 70
    grid = {}
    for x in range(dims + 1):
        for y in range(dims + 1):
            grid[(x, y)] = "."

    point = ""
    for i in range((dims + 1) * (dims + 1)):
        grid2 = copy.copy(grid)
        for b in range(i+1): # Add i points
            grid2[points[b]] = "#"
        cost, _ = dijkstra_grid_single_path(grid2, (0, 0), (dims, dims))
        if cost == -1:
            point = str(points[i][0]) + "," + str(points[i][1])
            break

    print("Part 2: ", point)
    assert(point == "58,19")


part_one()
part_two()
