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


def day14():
    grid = get_grid()
    part1_abyss = max(([key[1] for key, _ in grid.items()]))
    part2_abyss = part1_abyss + 2
    part1 = 0
    part2 = 0
    count = 0
    while not part1 or not part2: # Add one sand
        x = 500
        y = 0
        while True: # Step falling
            if not part1 and y >= part1_abyss:
                part1 = count
            if (x, y + 1) not in grid and y + 1 < part2_abyss:
                y += 1
            elif (x - 1, y + 1) not in grid and y + 1 < part2_abyss:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in grid and y + 1 < part2_abyss:
                y += 1
                x += 1
            else:
                grid[(x, y)] = 2
                count += 1
                if x == 500 and y == 0:
                    part2 = count
                break

    print("Part 1: ", part1)
    assert 964 == part1
    print("Part 2: ", part2)
    assert 32041 == part2


day14()
