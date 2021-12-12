
def day_11():
    file = open('11.txt', 'r')
    input = []
    for line in file:
        line = [int(l) for l in list(line.strip())]
        input.append(line)
    grid = {}
    for x in range(len(input)):
        for y in range(len(input)):
            grid[x, y] = input[x][y]
    
    shifts = ((0,1), (1,1), (1,0), (0, -1), (-1, -1), (-1, 0), (1, -1), (-1, 1))
    count_flashes = 0
    steps = 100
    part2_s = 0
    for s in range(steps * 10):
        count_flashes_step = 0
        for x in range(len(input)):
            for y in range(len(input)):
                grid[x, y] = grid[x, y] + 1
        x = 0
        while x < len(input):
            y = 0
            while y < len(input):
                if grid[x, y] > 9:
                    grid[x, y] = 0
                    if s < steps:
                        count_flashes = count_flashes + 1
                    count_flashes_step = count_flashes_step + 1
                    for shift in shifts:
                        coo = (x - shift[0], y - shift[1])
                        if coo in grid and grid[coo] != 0:
                            grid[coo] = grid[coo] + 1
                    x = 0
                    y = 0
                else:
                    y = y + 1
            x = x + 1
        i = 0
        if count_flashes_step == 100:
            part2_s = s
            break
    print(f"Part one: {count_flashes}") # 1615 correct
    print(f"Part two: {part2_s + 1}")

day_11()