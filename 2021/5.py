import re

def day_5():
    file = open('5.txt', 'r')
    coor = []
    min_max = [1000000, 1000000, -1000000, -1000000]
    minX = 1000000
    for line in file:
        co = (re.split(r",|->|", line.strip().replace(' ', '')))
        if co[0] == co[2] or co[1] == co[3]:
            co1 = [int(l) for l in co]
            min_max[0] = min(min_max[0], co1[0], co1[2])
            min_max[1] = min(min_max[1], co1[1], co1[3])
            min_max[2] = max(min_max[2], co1[0], co1[2])
            min_max[3] = max(min_max[3], co1[1], co1[3])
            coor.append(co1)
    #print(coor)
    grid = [[0]*1000 for i in range(1000)]
    for co in coor:
        if co[0] == co[2]:
            y1 = co[1] if co[1] < co[3] else co[3]
            y2 = co[1] if co[1] >= co[3] else co[3]
            for y in range(y1, y2 +1):
                grid[co[0]][y] = grid[co[0]][y] + 1
        if co[1] == co[3]:
            x1 = co[0] if co[0] < co[2] else co[2]
            x2 = co[0] if co[0] >= co[2] else co[2]
            for x in range(x1, x2 + 1):
                grid[x][co[1]] = grid[x][co[1]] + 1
    
    sum = 0
    for row in grid:
        sum += len([1 for i in row if i > 1])
    print(sum)
    # 5774 yes
    #6191 too high

def day_5_2():
    file = open('5.txt', 'r')
    coor = []
    min_max = [1000000, 1000000, -1000000, -1000000]
    for line in file:
        cos = (re.split(r",|->|", line.strip().replace(' ', '')))
        if True: #co[0] == co[2] or co[1] == co[3]:
            co = [int(l) for l in cos]
            coor.append(co)
    #print(coor)
    grid = [[0]*1000 for i in range(1000)]
    #coor.sort()
    #coor = list(dict.fromkeys(coor))
    for co in coor:
        if co[0] == co[2]:
            y1 = co[1] if co[1] < co[3] else co[3]
            y2 = co[1] if co[1] >= co[3] else co[3]
            for y in range(y1, y2 + 1):
                grid[y][co[0]] = grid[y][co[0]] + 1
        if co[1] == co[3]:
            x1 = co[0] if co[0] < co[2] else co[2]
            x2 = co[0] if co[0] >= co[2] else co[2]
            for x in range(x1, x2 + 1):
                grid[co[1]][x] = grid[co[1]][x] + 1
    for co in coor:
        if co[0] != co[2] and co[1] != co[3]:
            x = co[0]
            y = co[1]
            dirx = 1 if co[0] < co[2] else -1
            diry = 1 if co[1] < co[3] else -1
            for s in range(1000):
                grid[y][x] = grid[y][x] + 1
                x = x + dirx
                y = y + diry
                if dirx == 1:
                    if x > co[2]:
                        break
                if dirx == -1:
                    if x < co[2]:
                        break
    #18423 correct
    sum = 0
    for row in grid:
        sum += len([1 for i in row if i > 1])
    print(sum)
    
day_5_2()