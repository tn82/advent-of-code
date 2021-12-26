import copy
energy = {}
energy["A"] = 1
energy["B"] = 10
energy["C"] = 100
energy["D"] = 1000
dest = {}
dest["A"] = 2
dest["B"] = 4
dest["C"] = 6
dest["D"] = 8
def movep(p_start, p_end, steps, grid):
    grid[p_end] = grid.pop(p_start)
    grid[p_end][2] += 1
    #max_energy = 0 if grid[p_end][2] == 2 else energy[grid[p_end][0]]*(abs(p_start[0] - dest[grid[p_end][0]]) + 1)
    max_energy = energy[grid[p_end][0]]*(abs(p_start[0] - dest[grid[p_end][0]]) + 1)
    ener = energy[grid[p_end][0]]*steps
    return grid, ener, max_energy+ener

startp = (0, 1, 3, 5, 7, 9, 10)
finalp = ((2,1),(2,2), (4,1),(4,2), (6,1),(6,2), (8,1),(8,2))
def moves(grid, cost, max_cost):
    grids = []
    costs = []
    max_costs = []
    for coo, v in grid.items():
        if (coo[0], coo[1]-1) in grid: # blocked
            continue
        if (coo[0] == dest[v[0]] and coo[1] == 2): # Already good
            continue
        if (coo[0] == dest[v[0]] and coo[1] == 1 and grid[coo[0], 2][0] == v[0]): # Already good
            continue
        if v[2] == 0: # First move
            if ((dest[v[0]], 2) not in grid and (dest[v[0]], 1) not in grid) or ((dest[v[0]], 1) not in grid and grid[dest[v[0]], 2][0] == v[0]):
                breaker = False
                offset = 1 if coo[0] < dest[v[0]] else -1
                for x in range(coo[0], dest[v[0]]+offset, offset):
                    if (x, 0) in grid: # blocked
                        breaker = True
                        break
                if not breaker:
                    gridm = copy.deepcopy(grid)
                    deep = 1 if (dest[v[0]], 2) in grid else 2
                    steps = coo[1] + deep + abs(coo[0] - dest[v[0]])
                    gridm, costm, max_costm = movep(coo, (dest[v[0]], deep), steps, gridm)
                    grids.append(gridm)
                    costs.append(cost+costm)
                    max_costs.append(max_cost+max_costm)
                    continue
            for m in startp: # start moves
                breaker = False
                offset = 1 if coo[0] < m else -1
                for x in range(coo[0], m+offset, offset):
                    if (x, 0) in grid: # blocked
                        breaker = True
                        break
                if breaker:
                    continue
                gridm = copy.deepcopy(grid)
                steps = coo[1] + abs(coo[0] - m)
                gridm, costm, max_costm = movep(coo, (m, 0), steps, gridm)
                grids.append(gridm)
                costs.append(cost+costm)
                max_costs.append(max_cost+max_costm)
        if v[2] == 1: # Final move
            offset = 1 if coo[0] < dest[v[0]] else -1
            for x in range(coo[0] + offset, dest[v[0]], offset):
                if (x, 0) in grid: # blocked
                    continue
            if (dest[v[0]], 1) in grid:
                continue
            if (dest[v[0]], 2) in grid and grid[dest[v[0]], 2][0] != v[0]:
                continue
            if (dest[v[0]], 2) in grid:
                gridm = copy.deepcopy(grid)
                steps = 1 + abs(coo[0] - dest[v[0]])
                gridm, costm, max_costm = movep(coo, (dest[v[0]], 1), steps, gridm)
            else:
                gridm = copy.deepcopy(grid)
                steps = 2 + abs(coo[0] - dest[v[0]])
                gridm, costm, max_costm = movep(coo, (dest[v[0]], 2), steps, gridm)
            grids.append(gridm)
            costs.append(cost+costm)
            max_costs.append(cost+costm)
    return grids, costs, max_costs

def moves_rec(grid, cost, path=[]):
    grids = []
    costs = []
    paths = []
    for coo, v in grid.items():
        if (coo[0], coo[1]-1) in grid: # blocked
            continue
        if v[1] == 0: # First move
            for m in startp: # start moves
                gridm = copy.deepcopy(grid)
                steps = 1 + abs(coo[0] - m)
                gridm, costm = movep(coo, (m, 0), steps, gridm)
                newpaths = moves_rec(gridm, costm, path)
                for newpath in newpaths:
                    paths.append(newpath)
        if v[1] == 1: # Final move
            for x in range(coo[0], dest[v], 1 if coo[0] < dest[v] else -1):
                if (x, 0) in grid: # blocked
                    continue
            if (dest[v], 2) in grid:
                gridm = copy.deepcopy(grid)
                steps = 1 + abs(coo[0] - dest[v])
                gridm, costm = movep(coo, (dest[v], 1), steps, gridm)
            else:
                gridm = copy.deepcopy(grid)
                steps = 2 + abs(coo[0] - dest[v])
                gridm, costm = movep(coo, (dest[v], 2), steps, gridm)
            grids.append(gridm)
            costs.append(cost+costm)
    return paths

def all_good(grid):
    for c in "ABCD":
        if not (dest[c], 1) in grid or not (dest[c], 2) in grid:
            return False
        if grid[dest[c], 1][0] != c or grid[dest[c], 2][0] != c:
            return False
    return True

def day():
    grid = {}
    #for i in range(11):
    #    grid[i, 0] = "-" if i in (2,4,6,8) else "."
        #grid[i, 0] = "."

    #prod
    grid = {}
    grid[2,1] = ["B", 0,0]
    grid[2,2] = ["B", 0,0]
    grid[4,1] = ["A", 0,0]
    grid[4,2] = ["C", 0,0]
    grid[6,1] = ["A", 0,0]
    grid[6,2] = ["D", 0,0]
    grid[8,1] = ["D", 0,0]
    grid[8,2] = ["C", 0,0]
    
    #Test
    #grid2 = {}
    #grid2[2,1] = ["B", 0,0]
    #grid2[2,2] = ["A", 0,0]
    #grid2[4,1] = ["C", 0,0]
    #grid2[4,2] = ["D", 0,0]
    #grid2[6,1] = ["B", 0,0]
    #grid2[6,2] = ["C", 0,0]
    #grid2[8,1] = ["D", 0,0]
    #grid2[8,2] = ["A", 0,0]
    
    costs = [0]
    max_costs = [0]
    grids = [grid]
    final_cost = []
    ci = 0
    killed = 0
    while True:
        print(ci, len(grids), killed)
        ci += 1
        if not grids:
            break
        if ci > 10:
            print(ci)
        many_grids = []
        many_costs = []
        many_max_costs = []
        for (g,c,max_c) in zip(grids, costs, max_costs):
            gridsi, costsi, max_costi = moves(g, c, max_c)
            for (g1, c1, max_c1) in zip(gridsi, costsi, max_costi):
                if all_good(g1):
                    final_cost.append(c1)
                    print(f"Cost: {c1}")
                else:
                    if c1 < 11453 and g1 not in many_grids:
                        many_grids.append(g1)
                        many_costs.append(c1)
                        many_max_costs.append(max_c1)
                    else:
                        killed += 1
        grids = many_grids
        costs = many_costs
        max_costs = many_max_costs
    print(min(final_cost)) # 11453 too high 11417 corre t

day()