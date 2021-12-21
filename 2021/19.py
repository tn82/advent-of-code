
import itertools

def intersection12(l1, l2):
    return set(l1).intersection(l2)

def normalize(grid, b_norm):
    grid_norm = []
    for b in grid:
        grid_norm.append((b[0] - b_norm[0], b[1] - b_norm[1], b[2] - b_norm[2]))
    return grid_norm

def day_19():
    file = open('19.txt', 'r')
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
    distanceb = [[0,0,0]]
    while len(found) < len(grids):
        found_inner = set()
        for i, _ in enumerate(grids):
            if i not in found:
                continue
            gridi = search_grids[i]
            #print(found)
            for bi in gridi:
                gridi_norm = normalize(gridi, bi)
                for j, gridj in enumerate(grids):
                    if i == j or j == 0 or j in found:
                        continue
                    for perm in range(6): #itertools.permutations(b):
                        for flip in flips:
                            if j in found:
                                continue
                            gridj_fliped = []
                            for b in gridj:
                                perm_b = list(itertools.permutations(b))[perm]
                                perm_b = (perm_b[0] * flip[0], perm_b[1] * flip[1], perm_b[2] * flip[2])
                                gridj_fliped.append(perm_b)
                            for b in gridj_fliped:
                                gridj_norm = normalize(gridj_fliped, b)
                                inter = intersection12(gridi_norm, gridj_norm)
                                if len(inter) > 11:
                                    found.add(j)
                                    found_inner.add(j)
                                    print("i,j",i,j)
                                    gridj_norm = normalize(gridj_norm, (-bi[0], -bi[1], -bi[2]))
                                    inter = normalize(inter, (-bi[0], -bi[1], -bi[2]))
                                    global_grid.extend(gridj_norm)
                                    global_grid = list(set(global_grid)) # duplicates
                                    global_grid.sort()
                                    search_grids[j] = gridj_norm[:]
                                    distanceb.append([bi[0]-b[0], bi[1]-b[1], bi[2]-b[2]])
                                    break
                #break # after first bi
        if not found_inner:
            break
    print(len(global_grid)) # 666 too high 390 correct
    max_distance = 0
    for di in distanceb:
        for dj in distanceb:
            dist = abs(di[0] - dj[0]) + abs(di[1] - dj[1]) + abs(di[2] - dj[2])
            if dist > max_distance:
                max_distance = dist
    print(max_distance)

day_19()