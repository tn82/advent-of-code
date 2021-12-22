
def day():
    file = open('22_test.txt', 'r')
    input = []
    for line in file:
        row = line.strip().split()
        coo = []
        coo.append(1 if row[0] == "on" else 0)
        for c in row[1].split(","):
            co = c.split("=")[1].split("..")
            coo.extend([int(co[0]), int(co[1])])
        input.append(coo)
        
    grid = {}
    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                grid[x, y, z] = 0
                
    for coo in input:
        if coo[2] < -50 or coo[1] > 50:
            continue
        if coo[3] < -50 or coo[4] > 50:
            continue
        if coo[5] < -50 or coo[6] > 50:
            continue
        for x in range(coo[1], coo[2]+1):
            for y in range(coo[3], coo[4]+1):
                for z in range(coo[5], coo[6]+1):
                    grid[x, y, z] = coo[0]
    print(sum(grid.values()))

day()