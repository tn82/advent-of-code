def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]

def get_grid():
    grid = {}
    for line in input():
        x_prev = None
        y_prev = None
        for coo in line.split(" -> "):
            x, y = coo.split(",")
            x = int(x)
            y = int(y)
            if x_prev and y_prev:
                for xi in range(min(x, x_prev), max(x, x_prev) + 1):
                    grid[(xi, y)] = 1
                for yi in range(min(y, y_prev), max(y, y_prev) + 1):
                    grid[(x, yi)] = 1
            x_prev = x
            y_prev = y
    return grid

def part_one():
    grid = get_grid()
    abyss = max(([key[1] for key, _ in grid.items()]))
    count = 0
    found = False
    while not found: # Add one sand
        x = 500
        y = 0
        while True: # Step falling
            if y >= abyss:
                found = True
                break
            if (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in grid:
                y += 1
                x += 1
            else:
                grid[(x, y)] = 1
                count += 1
                break

    print("Part 1: ", count)
    assert count == 964


part_one()

def part_two():
    count = 0
    grid = get_grid()
    abyss = max(([key[1] for key, _ in grid.items()])) + 2
    count = 0
    found = False
    while not found: # Add one sand
        x = 500
        y = 0
        while True: # Step falling
            if (x, y + 1) not in grid and y + 1 < abyss:
                y += 1
            elif (x - 1, y + 1) not in grid and y + 1 < abyss:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in grid and y + 1 < abyss:
                y += 1
                x += 1
            else:
                grid[(x, y)] = 2
                count += 1
                if x == 500 and y == 0:
                    found = True
                break
    print("Part 2: ", count)
    assert count == 32041
part_two()
