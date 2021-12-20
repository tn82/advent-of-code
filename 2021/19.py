
import itertools

def intersection12(l1, l2):
    inter = [v for v in l1 if v in l2]
    if len(inter) > 11:
        print(inter)
        return True
    return False

def normalize(grid, b_norm):
    grid_norm = []
    for b in grid:
        grid_norm.append((b[0] - b_norm[0], b[1] - b_norm[1], b[2] - b_norm[2]))
    return grid_norm

def day_19():
    file = open('19_test.txt', 'r')
    #file = open('19.txt', 'r')
    grids = []
    myline = file.readline()
    while myline:
        if not myline.strip():
            continue
        if "--- scanner" in myline:
            myline = file.readline()
            grid = []
            while myline:
                line = [int(l) for l in list(myline.strip().split(","))]
                grid.append(tuple(line))
                #scanner_grid[line[0], line[1], line[2]] = 1
                myline = file.readline()
                if not myline.strip():
                    grids.append(grid)
                    break
        myline = file.readline()
    flips = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
    #delta_first = calc_delta(grids[0])
    grid0_norm = normalize(grids[0], grids[0][0])
    global_grid = grid0_norm[:]
    search_grids = [grid0_norm[:]]
    found = set()
    found.add(0)
    while len(found) < len(grids):
        found_inner = set()
        for i, gridi in enumerate(search_grids):
            for bi in gridi:
                gridi_norm = normalize(gridi, bi)
                #gridi_norm = normalize(gridi, (-618,-824,-621))
                for j, gridj in enumerate(grids):
                    if i == j or j == 0 or j in found:# or (i == 0 and j ==4):
                        continue
                    for perm in range(6): #itertools.permutations(b):
                        for flip in flips:
                            #if perm == 3 and flip == [-1, -1, 1]:
                            #    continue
                            #gridi_norm = normalize(gridi, gridi[0])
                            #for j, gridj in enumerate(grids):
                            #    if i == j or j == 0: #or j in found:
                            #        continue
                            gridj_fliped = []
                            for b in gridj:
                                perm_b = list(itertools.permutations(b))[perm]
                                perm_b = (perm_b[0] * flip[0], perm_b[1] * flip[1], perm_b[2] * flip[2])
                                gridj_fliped.append(perm_b)
                            for b in gridj_fliped:
                                gridj_norm = normalize(gridj_fliped, b)
                                if intersection12(gridi_norm, gridj_norm):
                                    found.add(j)
                                    found_inner.add(j)
                                    #gridj_norm = normalize(gridj_norm, grids[0][0])
                                    gridj_norm = normalize(gridj_norm, (-bi[0], -bi[1], -bi[2]))
                                    #gridj_norm = normalize(gridj_norm, grids[0][0])
                                    global_grid.extend(gridj_norm)
                                    global_grid = list(set(global_grid)) # duplicates
                                    search_grids.append(gridj_norm[:])
                                    break
        if not found_inner:
            break
    #global_grid = list(set(global_grid)) # duplicates
    print(len(global_grid))
    print(global_grid)

day_19()