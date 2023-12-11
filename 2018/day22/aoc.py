import networkx

def neighbours(x, y):
    return [(x-1, y),(x+1, y),(x, y-1),(x, y+1)]

# get a set of allowed tools for a given erosion level
# 0 = nothing, 1 = climbing gear, 2 = torch
def allowed_tools(erosion_level):
    erosion_level = erosion_level % 3
    if erosion_level == 0:
        return {1, 2}
    if erosion_level == 1:
        return {0, 1}
    if erosion_level == 2:
        return {0, 2}


def solve(depth, target):
    tx, ty = target

    # create 2d array for storing the grid
    # I put a buffer of 100 around it in case the shortest path travels beyond tx or ty
    grid = []
    for y in range(ty + 100):
        row = []
        for x in range(tx + 100):
            row.append(0)
        grid.append(row)

    # populate the erosion levels
    for y in range(ty + 100):
        for x in range(tx + 100):
            if x == 0 and y == 0:
                gi = 0
            elif x == 0:
                gi = y * 48271
            elif y == 0:
                gi = x * 16807
            elif tx == x and ty == y:
                gi = 0
            else:
                gi = grid[y - 1][x] * grid[y][x - 1]
            el = (gi + depth) % 20183
            grid[y][x] = el

    # create a graph and add edges for switching tools
    G = networkx.DiGraph()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            allowed = allowed_tools(grid[y][x])
            for t1 in allowed:
                for t2 in allowed:
                    if t1 == t2:
                        continue
                    G.add_edge((x, y, t1), (x, y, t2), weight=7)

    # add edges for travelling between squares
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for nx, ny in neighbours(x, y):
                if nx < 0 or nx >= len(grid[0]):
                    continue
                if ny < 0 or ny >= len(grid):
                    continue
                from_erosion = grid[y][x]
                to_erosion = grid[ny][nx]

                # get tools that can be used when travelling between these cells
                tools = allowed_tools(from_erosion).intersection(allowed_tools(to_erosion))

                for tool in tools:
                    G.add_edge((x, y, tool), (nx, ny, tool), weight=1)

    total = 0
    for y in range(ty + 1):
        for x in range(tx + 1):
            total += grid[y][x] % 3
    print("Part 1", total)

    shortest_path_length = networkx.dijkstra_path_length(G, (0, 0, 2), (tx, ty, 2))
    print("Part 2", shortest_path_length)

# EXAMPLE:
#solve(510, (10, 10))
solve(9171, (7,721))