from collections import defaultdict
from copy import deepcopy


def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


jumps = {}
jumps["N"] = (0, -1)
jumps["S"] = (0, 1)
jumps["E"] = (1, 0)
jumps["W"] = (-1, 0)
jumps["H"] = (0, 0)
dirs = "SEHNW"

def day24():
    grid = {}
    wall = {}
    wall[(1, -1)] = 1
    for y, line in enumerate(input()):
        for x, c in enumerate(line):
            if c != "#" and c != "." and c != "E":
                grid[(x, y)] = [c]
            if c == "#":
                wall[(x, y)] = 1
    wall_x = max([x for x, _ in wall.keys()])
    wall_y = max([y for _, y in wall.keys()])
    start_position = (1, 0)
    goal = (6, 5)
    goal = (120, 26)
    wall[(goal[0], goal[1] + 1)] = 1
    time = 0
    path_list = [start_position]
    goal_list = [1]
    part_one = 0
    part_two = 0
    while True:
        grid_tmp = defaultdict(list)
        for coo, vals in grid.items():
            while vals:
                val = vals.pop(0)
                if val == "v":
                    x = coo[0]
                    y = coo[1] + 1 if coo[1] + 1 < wall_y else 1
                if val == "^":
                    x = coo[0]
                    y = coo[1] - 1 if coo[1] - 1 > 0 else wall_y - 1
                if val == "<":
                    x = coo[0] - 1 if coo[0] - 1 > 0 else wall_x - 1
                    y = coo[1]
                if val == ">":
                    x = coo[0] + 1 if coo[0] + 1 < wall_x else 1
                    y = coo[1]
                grid_tmp[(x, y)].append(val)
        grid = grid_tmp

        time += 1
        # move pos in an optimal way
        path_list_tmp = []
        goal_list_tmp = []
        cache = set()
        for path, goal_num in zip(path_list, goal_list):
            if time > 300 and goal_num == 1:
                continue
            if time > 600 and goal_num == 2:
                continue
            for d in dirs:
                new_pos = path[0] + jumps[d][0], path[1] + jumps[d][1]
                if new_pos not in grid and new_pos not in wall:
                    if (new_pos[0], new_pos[1], goal_num) in cache:
                        continue
                    cache.add((new_pos[0], new_pos[1], goal_num))
                    path_list_tmp.append(new_pos)
                    if goal_num in (1, 3) and new_pos == goal or goal_num == 2 and new_pos == start_position:
                        if goal_num == 1 and not part_one:
                            part_one = time
                        if goal_num == 3:
                            part_two = time
                            print("Part 1: ", part_one)
                            assert part_one == 277

                            print("Part 2: ", part_two)
                            assert part_two == 877
                            exit(0)
                        goal_list_tmp.append(goal_num + 1)
                    else:
                        goal_list_tmp.append(goal_num)
        path_list = path_list_tmp
        goal_list = goal_list_tmp
        print("Time:", time, len(path_list), goal_list.count(1), goal_list.count(2), goal_list.count(3))

day24()
