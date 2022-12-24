def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]



def part_one():
    shifts = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    shift = {}

    shift["N"] = [(-1, -1), (0, -1), (1, -1)]
    shift["S"] = [(-1, 1), (0, 1), (1, 1)]
    shift["E"] = [(1, 0), (1, 1), (1, -1)]
    shift["W"] = [(-1, 0), (-1, 1), (-1, -1)]
    jumps = {}
    jumps["N"] = (0, -1)
    jumps["S"] = (0, 1)
    jumps["E"] = (1, 0)
    jumps["W"] = (-1, 0)
    dirs = "NSWE"
    grid = {}
    count = 0
    for y, line in enumerate(input()):
        for x, c in enumerate(line):
            if c == "#":
                grid[(x, y)] = 1

    for round in range(1, 11):

        proposed = {}
        for coo in grid.keys():
            move = False
            for s in shifts:
                if (coo[0] + s[0], coo[1] + s[1]) in grid:
                    move = True
                    break
            if move:
                for d in dirs:
                    for s in shift[d]:
                        breaker = False
                        if (coo[0] + s[0], coo[1] + s[1]) in grid:
                            breaker= True
                            break
                    if breaker:
                        continue
                    prop = (coo[0] + jumps[d][0], coo[1] + jumps[d][1])
                    if prop not in proposed:
                        proposed[prop] = [coo]
                    else:
                        proposed[prop].append(coo)
                    break
        for prop, coos in proposed.items():
            if len(coos) == 1:
                del grid[coos[0]]
                if prop in grid:
                    print(1)
                grid[prop] = 1

        # Update order
        dirs = dirs[1:] + dirs[0]
    min_x = 1e12
    max_x = -1e12
    min_y = 1e12
    max_y = -1e12
    for x, y in grid.keys():
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    part_one = 0
    for x in range(min_x, max_x + 1):
         for y in range(min_y, max_y + 1):
             if not (x, y) in grid:
                 part_one += 1

    print("Part 1: ", part_one)
    assert part_one == 4049

    print("Part 2: ", count)
    assert count == 0

def part_two():
    shifts = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    shift = {}

    shift["N"] = [(-1, -1), (0, -1), (1, -1)]
    shift["S"] = [(-1, 1), (0, 1), (1, 1)]
    shift["E"] = [(1, 0), (1, 1), (1, -1)]
    shift["W"] = [(-1, 0), (-1, 1), (-1, -1)]
    jumps = {}
    jumps["N"] = (0, -1)
    jumps["S"] = (0, 1)
    jumps["E"] = (1, 0)
    jumps["W"] = (-1, 0)
    dirs = "NSWE"
    grid = {}
    count = 0
    for y, line in enumerate(input()):
        for x, c in enumerate(line):
            if c == "#":
                grid[(x, y)] = 1

    for round in range(1, 10000):
        proposed = {}
        for coo in grid.keys():
            move = False
            for s in shifts:
                if (coo[0] + s[0], coo[1] + s[1]) in grid:
                    move = True
                    break
            if move:
                for d in dirs:
                    for s in shift[d]:
                        breaker = False
                        if (coo[0] + s[0], coo[1] + s[1]) in grid:
                            breaker= True
                            break
                    if breaker:
                        continue
                    prop = (coo[0] + jumps[d][0], coo[1] + jumps[d][1])
                    if prop not in proposed:
                        proposed[prop] = [coo]
                    else:
                        proposed[prop].append(coo)
                    break
        moves = 0
        for prop, coos in proposed.items():
            if len(coos) == 1:
                del grid[coos[0]]
                grid[prop] = 1
                moves += 1
        if not moves:
            break
        # Update order
        dirs = dirs[1:] + dirs[0]
    min_x = 1e12
    max_x = -1e12
    min_y = 1e12
    max_y = -1e12
    for x, y in grid.keys():
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    part_one = 0
    for x in range(min_x, max_x + 1):
         for y in range(min_y, max_y + 1):
             if not (x, y) in grid:
                 part_one += 1

    print("Part 2: ", round)
    assert round == 1021

part_two()
