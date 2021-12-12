from collections import defaultdict

def find_paths(graph, start, end, lower_visited_twice = False, path=[]):
    path = path + [start]
    if start.islower() and path.count(start) > 1:
        lower_visited_twice = True
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node.islower() and path.count(node) > 1:
            continue
        if node.islower() and lower_visited_twice and node in path:
            continue
        if node == "start":
            continue
        newpaths = find_paths(graph, node, end, lower_visited_twice, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths

def day_12():
    file = open('12.txt', 'r')
    graph = defaultdict(list)
    for line in file:
        s = line.strip().split("-")
        graph[s[0]].append(s[1])
        graph[s[1]].append(s[0]) # Bi-directional graph
        
    paths = find_paths(graph, "start", "end", True)
    print(f"Part one: {len(paths)}") # 5254 correct
    paths = find_paths(graph, "start", "end", False)
    print(f"Part two: {len(paths)}") # 149385 correct

day_12()