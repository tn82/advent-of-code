
def day():
    file = open('25.txt', 'r')
    east = {}
    south = {}
    x = 0
    for line in file:
        row = line.strip()
        y = 0
        for c in row:
            if c == ">":
                east[x, y] = c
            if c == "v":
                south[x, y] = c
            y += 1
        x += 1
    max_x = x-1
    max_y = y-1
    steps = 0
    while True:
        moves = 0
        east_m = {}
        for (x, y) in east:
            y1 = 0 if y == max_y else y + 1
            if (x, y1) not in east and (x, y1) not in south:
                east_m[x, y1] = east[x, y]
                moves += 1
            else:
                east_m[x, y] = east[x, y]
        east = east_m
        
        south_m = {}
        for (x, y) in south:
            x1 = 0 if x == max_x else x + 1
            if (x1, y) not in east and (x1, y) not in south:
                south_m[x1, y] = south[x, y]
                moves += 1
            else:
                south_m[x, y] = south[x, y]
        south = south_m
        steps += 1
        print(moves, steps)
        if not moves or steps > 1000:
            break

day()