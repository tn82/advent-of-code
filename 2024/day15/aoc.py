import os
from collections import defaultdict
import copy

day_path = os.path.dirname(__file__)


def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]


def input_raw():
    with open(os.path.join(day_path, "input.txt"), "r") as f:
        return f.read().strip()


def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test_raw():
    with open(os.path.join(day_path, "test.txt"), "r") as f:
        return f.read().strip()

def int_list(char_list):
    return [int(c) for c in char_list]


def move_xy(m):
    return {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}[m]


def grid_printer(grid):
    row = 0
    for coo, v in grid.items():
        x, y = coo
        if y != row:
            print()
            row = y
        print(v, end="")

    print()
    print()


def try_move(grid, rx, ry, x, y):
    nx = rx + x
    ny = ry + y
    if grid[(nx, ny)] == ".":
        robo_moved = True if grid[(rx, ry)] == "@" else False
        grid[(nx, ny)] = grid[(rx, ry)]  # Update new pos
        grid[(rx, ry)] = "."  # Update new pos
        return robo_moved, True, nx, ny
    elif grid[(nx, ny)] == "#":
        return False, False, rx, ry
    else:
        ok = True
        nxc, nyc = nx, ny
        # any_ok = False
        while ok:
            robo_moved, ok, _, _ = try_move(grid, nxc, nyc, x, y)
            if robo_moved:
                break
            nxc -= x
            nyc -= y
        if robo_moved:
            return robo_moved, True, nx, ny
        else:
            return robo_moved, ok, rx, ry


def part_one():
    sums = 0
    grid = {}
    rx, ry = 0, 0
    start_grid, moves = input_raw().split("\n\n")
    for y, line in enumerate(start_grid.split("\n")):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "@":
                rx = x
                ry = y

    grid_printer(grid)
    for c in moves.replace("\n", ""):
        x, y = move_xy(c)
        # print(c)
        robo_moved, ok, rx, ry = try_move(grid, rx, ry, x, y)
        # grid_printer(grid)
        # print(rx, ry)

    for coo, v in grid.items():
        if v == "O":
            sums += coo[0] + 100 * coo[1]

    print("Part 1: ", sums)
    assert sums == 1515788

# Move multple blocks
# Move tetris block if not blocked
def part_two():
    sums = 0
    grid2 = {}
    rx, ry = 0, 0
    start_grid, moves = input_raw().split("\n\n")
    for y, line in enumerate(start_grid.split("\n")):
        for x, c in enumerate(line):
            grid2[(x, y)] = c
            if c == "@":
                rx = x
                ry = y
    grid = {}
    for coo, v in grid2.items():
        x, y = coo
        if v == "#":
            grid[(x * 2, y)] = "#"
            grid[(x * 2 + 1, y)] = "#"
        if v == "O":
            grid[(x * 2, y)] = "["
            grid[(x * 2 + 1, y)] = "]"
        if v == ".":
            grid[(x * 2, y)] = "."
            grid[(x * 2 + 1, y)] = "."
        if v == "@":
            grid[(x * 2, y)] = "@"
            grid[(x * 2 + 1, y)] = "."

    rx *= 2
    grid_printer(grid)
    for c in moves.replace("\n", ""):
        dx, dy = move_xy(c)
        #print("Move " + c + ":")

        coo_list = [(rx, ry)]
        i = 0
        do_move = True
        while i < len(coo_list):
            x, y = coo_list[i]
            nx, ny = x + dx, y + dy
            if grid[(nx, ny)] in "O[]":
                if (nx, ny) not in coo_list:
                    coo_list.append((nx, ny))
                if grid[(nx, ny)] == "[":
                    if (nx + 1, ny) not in coo_list:
                        coo_list.append((nx + 1, ny))
                if grid[(nx, ny)] == "]":
                    if (nx - 1, ny) not in coo_list:
                        coo_list.append((nx - 1, ny))
            elif grid[(nx, ny)] == "#":
                do_move = False
                break
            i += 1
        if not do_move:
            continue

        new_grid = copy.copy(grid)
        for x, y in coo_list:
            new_grid[(x, y)] = "."
        for x, y in coo_list:
            new_grid[(x + dx, y + dy)] = grid[(x, y)]

        grid = new_grid

        rx += dx
        ry += dy

        #grid_printer(grid)
        #print(rx, ry)

    for coo, v in grid.items():
        if v in "O[":
            sums += coo[0] + 100 * coo[1]

    print("Part 2: ", sums)
    assert(sums == 1516544)


#part_one()
part_two()
