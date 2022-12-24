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

def part_one():
    count = 0
    grid = {}
    wall = {}
    wall[(1, -1)] = 1
    for y, line in enumerate(input()):
        for x, c in enumerate(line):
            if c != "#" and c != "." and c != "E":
                grid[(x, y)] = [c]
            if c == "#":
                wall[(x, y)] = 1
    wall_x = 7
    wall_y = 5
    wall_x = 121
    wall_y = 26
    pos = (1, 0)
    goal = (6, 5)
    goal = (120, 26)
    wall[(goal[0], goal[1] + 1)] = 1
    time = 0
    path_list = [[pos]]
    goal_list = [1]
    while True:
        # move time
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
        # move pos in an optimal way?
        path_list_tmp = []
        goal_list_tmp = []
        cache = set()
        dist = []
        found_goal = False
        for path, goal_num in zip(path_list, goal_list):
            if len(path) > 300 and goal_num == 1:
                continue
            if len(path) > 600 and goal_num == 2:
                continue
            for d in dirs:
                new_pos = path[-1][0] + jumps[d][0], path[-1][1] + jumps[d][1]
                if new_pos not in grid and new_pos not in wall:
                    if (new_pos[0], new_pos[1], goal_num) in cache:
                        continue
                    cache.add((new_pos[0], new_pos[1], goal_num))
                    dist.append(goal[0] - new_pos[0] + goal[1] - new_pos[1])
                    if goal[0] - new_pos[0] < 0:
                        print("Error", goal, new_pos)
                    if goal[1] - new_pos[1] < 0:
                        print("Error", goal, new_pos)
                    new_path = deepcopy(path)
                    new_path.append(new_pos)
                    path_list_tmp.append(new_path)
                    if goal_num in (1, 3) and new_pos == goal or goal_num == 2 and new_pos == pos:
                        print(time, goal_num) # 277 low
                        if goal_num == 3:
                            exit(0)
                        goal_list_tmp.append(goal_num + 1)
                    else:
                        goal_list_tmp.append(goal_num)
        path_list = path_list_tmp
        goal_list = goal_list_tmp
        print("Time:", time, len(path_list), min(dist), goal_list.count(1), goal_list.count(2), goal_list.count(3))
    print("Part 1: ", time)
    assert time == 277

    print("Part 2: ", count)
    assert count == 0


part_one()
