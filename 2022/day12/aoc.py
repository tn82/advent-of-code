from collections import defaultdict


def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]


def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]

elev = "abcdefghijklmnopqrstuvwxyz"
elev_num = {c: i for i, c in enumerate(elev)}

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

def part_one():
    grid = {}
    S_coo = ()
    E_coo = ()
    for y, line in enumerate(input()):
        for x, c in enumerate(line):
            if c == "S":
                S_coo = (x, y)
                c = "a"
            if c == "E":
                E_coo = (x, y)
                c = "z"
            grid[(x, y)] = c

    graph = defaultdict(list)
    for coo, val in grid.items():
        x, y = coo
        moves = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        val_num = elev_num[val]
        for move in moves:
            if move in grid and val_num + 1 >= elev_num[grid[move]]:
                graph[coo].append(move)

    path = shortest_path(graph, S_coo, E_coo)
    print("Part 1: ", len(path) - 1)
    assert len(path) - 1 == 437

    longest_shortest = 1e9
    for coo, val in grid.items():
        if val != "a":
            continue
        path = shortest_path(graph, coo, E_coo)
        if not path:
            continue
        path_len = len(path) - 1
        if path_len < longest_shortest:
            longest_shortest = path_len

    print("Part 2: ", longest_shortest)
    assert 430 == longest_shortest


part_one()
