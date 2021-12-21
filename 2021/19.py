
import itertools

def intersection12(l1, l2):
    return [v for v in l2 if v in l1]
    if len(inter) > 11:
        return True
    return False

def normalize(grid, b_norm):
    grid_norm = []
    for b in grid:
        grid_norm.append((b[0] - b_norm[0], b[1] - b_norm[1], b[2] - b_norm[2]))
    return grid_norm

def day_19():
    file = open('19.txt', 'r')
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
    global_grid = grids[0][:]
    search_grids = {0: grids[0][:]}
    found = set()
    found.add(0)
    map_b = {}
    while len(found) < len(grids):
        found_inner = set()
        for i, _ in enumerate(grids):
            if i not in found:
                continue
            gridi = search_grids[i]
            print(found)
            for bi in gridi:
                gridi_norm = normalize(gridi, bi)
                for j, gridj in enumerate(grids):
                    if i == j or j == 0 or j in found:# or (i == 0 and j ==4):
                        continue
                    for perm in range(6): #itertools.permutations(b):
                        for flip in flips:
                            if j in found:
                                continue
                            #if flip == [1, -1, -1] and perm == 3:
                            #    continue
                            gridj_fliped = []
                            for b in gridj:
                                perm_b = list(itertools.permutations(b))[perm]
                                perm_b = (perm_b[0] * flip[0], perm_b[1] * flip[1], perm_b[2] * flip[2])
                                gridj_fliped.append(perm_b)
                            for b in gridj_fliped:
                                gridj_norm = normalize(gridj_fliped, b)
                                inter = intersection12(gridi_norm, gridj_norm)
                                if len(inter) > 11:
                                    if not j in map_b:
                                        map_b[j] = {}
                                    #map_b[j][i] = bi
                                    found.add(j)
                                    found_inner.add(j)
                                    gridj_norm = normalize(gridj_norm, (-bi[0], -bi[1], -bi[2]))
                                    inter = normalize(inter, (-bi[0], -bi[1], -bi[2]))
                                    #ix = j
                                    #while ix != 0:
                                    #    bx = list(map_b[ix].values())[0]
                                    #    gridj_norm = normalize(gridj_norm, (-bx[0], -bx[1], -bx[2]))
                                    #    inter = normalize(inter, (-bx[0], -bx[1], -bx[2]))
                                    #    ix = list(map_b[ix].keys())[0]
                                    global_grid.extend(gridj_norm)
                                    global_grid = list(set(global_grid)) # duplicates
                                    global_grid.sort()
                                    #search_grids[j] = gridj_fliped[:]
                                    search_grids[j] = gridj_norm[:]
                                    break
                #break # after first bi
        if not found_inner:
            break
    #global_grid = list(set(global_grid)) # duplicates
    print(len(global_grid)) # 666 too high
    #print(global_grid) 

day_19()