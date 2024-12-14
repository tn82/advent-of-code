import heapq

def dijkstra(graph, start):
  """
  Computes the shortest distances from a starting node to all other nodes in a graph.

  Args:
    graph: A dictionary representing the graph where keys are nodes and 
           values are dictionaries mapping neighbors to edge weights.
    start: The starting node for computing shortest paths.

  Returns:
    A dictionary mapping nodes to their shortest distances from the start node.
  """

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