import heapq

def dijkstra(graph, start):


  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  visited = set()
  priority_queue = [(0, start)]  # (distance, node)

  while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)

    if current_node in visited:
      continue

    visited.add(current_node)

    for neighbor, weight in graph[current_node].items():
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(priority_queue, (distance, neighbor))

  return distances


# Example graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1, 'E': 3},
    'D': {'B': 5, 'C': 1, 'E': 1},
    'E': {'C': 3, 'D': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}: {shortest_distances}")


def clockwise(x, y):
    return (y, -x)

def counter_clockwise(x, y):
    return (-y, x)

def neighbor_weights_simple(grid, current_node):
    nw = []
    x, y = current_node
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        neighbor = x + dx, y + dy
        if (neighbor) not in grid or grid[(neighbor)] == "#":
            continue
        nw.append((neighbor, 1))
    return nw

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

input_raw = "\
###############\n\
#.......#....E#\n\
#.#.###.#.###.#\n\
#.....#.#...#.#\n\
#.###.#####.#.#\n\
#.#.#.......#.#\n\
#.#.#####.###.#\n\
#...........#.#\n\
###.#.#####.#.#\n\
#...#.....#.#.#\n\
#.#.#.###.#.#.#\n\
#.....#...#.#.#\n\
#.###.#.#.#.#.#\n\
#S..#.....#...#\n\
###############"

sx, sy = 0, 0
ex, ey = 0, 0
grid = {}
# for y, line in enumerate(test_raw().split("\n")):
for y, line in enumerate(input_raw.split("\n")):
    for x, c in enumerate(line):
        grid[(x, y)] = c
        if c == "S":
            sx = x
            sy = y
        if c == "E":
            ex = x
            ey = y

distances, paths = dijkstra_grid_single_path(grid, (sx, sy, 1, 0), (ex, ey))
print(distances)