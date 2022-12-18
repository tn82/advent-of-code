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

def day17(number_of_rocks):
    grid = {(0, 0): 1, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, (5, 0): 1, (6, 0): 1}
    count = 0
    gases = input()[0]
    gases_len = len(gases)
    rock = 0
    prev_size = 0
    prev_rock = 0
    extra = 0
    while rock < number_of_rocks:
        rock_type = rock % 5
        shape = shapes[rock_type]
        y = grid_max(grid) + 4
        shape = shift(shape, y)
        while True:
            gas = gases[count % gases_len]
            if rock == 3453: # Recurring pattern at 3453
                mega_step = round(number_of_rocks / (rock - prev_rock)) -2
                extra = (grid_max(grid) - prev_size) * mega_step
                rock += mega_step * (rock - prev_rock)
            # Find recurring pattern => pattern at rock 3453
            if count % gases_len == 0:
                 prev_rock = rock
                 prev_size = grid_max(grid)
            count +=1
            if not hit_wall(shape, gas, grid):
                shape = shift(shape, gas)
            if not hit(shape, grid):
                shape = shift(shape, "v")
            else:
                update_grid(shape, grid)
                break
        rock += 1
    return grid_max(grid) + extra

one = day17(2022)
print("Part 1: ", one)
assert one == 3090

two = day17(1e12)
print("Part 1: ", two)
assert two == 1530057803453
