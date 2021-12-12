from collections import defaultdict

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper():
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_all_paths2(graph, start, end, path=[], found2 = False):
    path = path + [start]
    
    if not start.isupper() and path.count(start) == 2:
        found2 = True

    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if path.count(node) < 2 or node.isupper():
            if not node.isupper() and found2 and node in path:
                continue
            if node == "start" and node in path:
                continue
            #print(path, node, path.count(node), found2)
            newpaths = find_all_paths2(graph, node, end, path, found2)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def day_12():
    file = open('12.txt', 'r')
    graph = defaultdict(list)
    for line in file:
        s = line.strip().split("-")
        graph[s[0]].append(s[1])
        graph[s[1]].append(s[0])
    #graph = dict(graph)
    paths = find_all_paths(graph, "start", "end")
    print(f"Part one: {len(paths)}") # 5254 correct
    paths = find_all_paths2(graph, "start", "end")
    print(f"Part two: {len(paths)}") # 149385 correct

day_12()