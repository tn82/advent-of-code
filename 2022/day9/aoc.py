def print_grid(grid):
    inverse = [(key) for key, value in grid.items()]
    for p in grid:


def is_lost(h, t):
    return abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1

def visited(ropes: int):
    file = open("input.txt", "r")

    grids = {}
    curr_pos = []
    for i in range(ropes):
        grids[i] = {}
        grids[i][(0, 0)] = 1
        curr_pos.append((0, 0))

    for line in file:
        line = line.strip()
        d, steps = line.split()
        for _ in range(int(steps)):
            h = curr_pos[ropes - 1]
            grid = grids[ropes - 1]
            if d == "U":
                h = (h[0], h[1] + 1)
                G[h] = 1
            if d == "D":
                h = (h[0], h[1] - 1)
                grid[h] = 1
            if d == "R":
                h = (h[0] + 1, h[1])
                grid[h] = 1
            if d == "L":
                h = (h[0] - 1, h[1])
                grid[h] = 1
            curr_pos[ropes - 1] = h

            for i in range(ropes - 2, -1, -1):
                up = False
                h = curr_pos[i + 1]
                t = curr_pos[i]
                grid = grids[i]
                if h[0] == t[0]:
                    if h[1] - t[1] > 1:
                        t = (t[0], t[1] + 1)
                        up = True
                    elif h[1] - t[1] < -1:
                        t = (t[0], t[1] - 1)
                        up = True

                elif h[1] == t[1]:
                    if h[0] - t[0] > 1:
                        t = (t[0] + 1, t[1])
                        up = True

                    elif h[0] - t[0] < -1:
                        t = (t[0] - 1, t[1])
                        up = True

                elif is_lost(h, t):
                    if h[0] - t[0] > 0 and h[1] - t[1] > 0:
                        t = (t[0] + 1, t[1] + 1)
                        up = True

                    elif h[0] - t[0] > 0 and h[1] - t[1] < 0:
                        t = (t[0] + 1, t[1] - 1)
                        up = True

                    elif h[0] - t[0] < 0 and h[1] - t[1] > 0:
                        t = (t[0] - 1, t[1] + 1)
                        up = True

                    elif h[0] - t[0] < 0 and h[1] - t[1] < 0:
                        t = (t[0] - 1, t[1] - 1)
                        up = True
                if not up:
                    break
                grid[t] = 1
                curr_pos[i] = t

    return sum(grids[0].values())

part_one = visited(2)
print("Part 1: ", part_one)
assert part_one == 6087

part_two = visited(10)
print("Part 2: ", part_two)
assert part_two == 2493
