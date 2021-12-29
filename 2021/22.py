
def counters(cubes):
    ons = 0 
    for cube in cubes:
        ons += cube[6] * (cube[1] - cube[0] + 1) * (cube[3] - cube[2] + 1) * (cube[5] - cube[4] + 1)
    return ons

def spawn_neg(oldc, newc):
    #if oldc[6] != 1:
    #    return
    if oldc[0] > newc[1] or oldc[1] < newc[0] or oldc[2] > newc[3] or oldc[3] < newc[2] or oldc[4] > newc[5] or oldc[5] < newc[4]:
        return
    else:
        return [max(oldc[0], newc[0]), min(oldc[1], newc[1]), max(oldc[2], newc[2]), min(oldc[3], newc[3]), max(oldc[4], newc[4]), min(oldc[5], newc[5]), 1 if oldc[6] == -1 else -1]

def day():
    file = open('22.txt', 'r')
    input = []
    for line in file:
        row = line.strip().split()
        coo = []
        for c in row[1].split(","):
            co = c.split("=")[1].split("..")
            coo.extend([int(co[0]), int(co[1])])
        coo.append(1 if row[0] == "on" else 0)
        input.append(coo)
        
    grid = {}
    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                grid[x, y, z] = 0
                
    for coo in input:
        if coo[1] < -50 or coo[0] > 50:
            continue
        if coo[2] < -50 or coo[3] > 50:
            continue
        if coo[4] < -50 or coo[5] > 50:
            continue
        for x in range(coo[0], coo[1]+1):
            for y in range(coo[2], coo[3]+1):
                for z in range(coo[4], coo[5]+1):
                    grid[x, y, z] = coo[6]
    print(f"Part 1: {sum(grid.values())}")
    
    cubes = []
    for i, new_cube in enumerate(input):
        cubes_split = []
        for old_cube in cubes:
            cubes_split.append(old_cube)
            neg_cube = spawn_neg(old_cube, new_cube)
            if neg_cube:
                cubes_split.append(neg_cube)
        if new_cube[6] == 1:
            cubes_split.append(new_cube)
        cubes = cubes_split
    print(counters(cubes))
    print(f"Part 2: {counters(cubes)}")
day()