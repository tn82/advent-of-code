def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]

shapes = [[(2, 0), (3, 0), (4, 0), (5, 0)],\
          [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],\
          [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],\
          [(2, 0), (2, 1), (2, 2), (2, 3)],\
          [(2, 0), (3, 0), (2, 1), (3, 1)]]

def shift(shape, shift):
    if shift == "<":
        return [(x - 1, y) for x, y in shape]
    if shift == ">":
        return [(x + 1, y) for x, y in shape]
    if shift == "v":
        return [(x, y - 1) for x, y in shape]
    else:
        return [(x, y + shift) for x, y in shape]

def hit(shape, grid):
    for sx, sy in shape:
        if (sx, sy - 1) in grid:
            return True
    return False


def hit_wall(shape, shif, grid):
    test = shift(shape, shif)
    for x, y in test:
        if (x, y) in grid:
            return True
        if x < 0 or x > 6:
            return True
    return False

def update_floor(shape, floor):
    floor_update = []
    for fx, fy in enumerate(floor):
        fy_max = fy
        for sx, sy in shape:
            if sx == fx:
                fy_max = sy
        floor_update.append(fy_max)
    return floor_update

def update_grid(shape, grid):
    for coo in shape:
        grid[coo] = 1

def grid_max(grid):
    return max([y for (_, y) in grid.keys()])

def part_one():
    grid = {}
    grid[(0, 0)] = 1
    grid[(1, 0)] = 1
    grid[(2, 0)] = 1
    grid[(3, 0)] = 1
    grid[(4, 0)] = 1
    grid[(5, 0)] = 1
    grid[(6, 0)] = 1
    count = 0
    gases = input()[0]
    gases_len = len(gases)
    for rock in range(0, 2022):
        rock_type = rock % 5
        shape = shapes[rock_type]
        x = 3
        y = grid_max(grid) + 4
        shape = shift(shape, y)
        while True:
            gas = gases[count % gases_len]
            count +=1
            if not hit_wall(shape, gas, grid):
                shape = shift(shape, gas)
            if not hit(shape, grid):
                shape = shift(shape, "v")
            else:
                update_grid(shape, grid)
                break

    print("Part 1: ", grid_max(grid))
    assert grid_max(grid) == 3090

def part_two():
    grid = {}
    grid[(0, 0)] = 1
    grid[(1, 0)] = 1
    grid[(2, 0)] = 1
    grid[(3, 0)] = 1
    grid[(4, 0)] = 1
    grid[(5, 0)] = 1
    grid[(6, 0)] = 1
    count = 0
    gases = input()[0]
    gases_len = len(gases)
    rock = 0
    prev_size = 0
    prev_rock = 0
    extra = 0
    while rock < 1e12:
        rock_type = rock % 5
        shape = shapes[rock_type]
        x = 3
        y = grid_max(grid) + 4
        shape = shift(shape, y)
        while True:
            gas = gases[count % gases_len]
            if rock == 3453:
                print("rock dist", rock - prev_rock)
                stepp = round(1e12 / (rock - prev_rock)) -2
                extra = (grid_max(grid) - prev_size) * stepp
                rock += stepp * (rock - prev_rock)
            if count % gases_len == 0:
                prev_rock = rock
                prev_size = grid_max(grid)
                print(rock_type, grid_max(grid), rock)
            count +=1
            #print(rock, count)
            if not hit_wall(shape, gas, grid):
                shape = shift(shape, gas)
            if not hit(shape, grid):
                shape = shift(shape, "v")
            else:
                update_grid(shape, grid)
                break
        rock += 1

    print("Part 2: ", grid_max(grid) + extra)
    assert grid_max(grid) + extra == 1530057803453

part_one()
part_two()
