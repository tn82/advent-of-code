import os
from collections import defaultdict
import copy
from functools import cache

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

@cache
def is_valid(group, code):
    if "?" in group:
        return
    broken = 0
    gc = []
    for gi, g in enumerate(group):
        if g == "#":
            broken += 1
        else:
            if broken:
                gc.append(str(broken))
            broken = 0
    if broken:
        gc.append(str(broken))
    return tuple(gc) == code
        
@cache
def is_valid_so_far(group, code):
    code_sum = sum([int(c) for c in code])
    if group.count("#") > code_sum:
        return False
    if group.count(".") > len(group) - code_sum:
        return False

    broken = 0
    gc = []
    for gi, g in enumerate(group):
        if g == "?":
            broken = 0
            break
        if g == "#":
            broken += 1
        else:
            if broken:
                gc.append(broken)
            broken = 0
    if broken:
        gc.append(broken)
    if len(gc) > len(code):
        return False
    for i, g in enumerate(gc):
        if g != code[i]:
            return False
    return True

@cache
def lopploop2(group, code):
    i = -1
    sums = 0
    for gi, g in enumerate(group):
        if g == "?":
            i = gi
            break
    if i >= 0:
        groupc = copy.deepcopy(list(group))
        groupc[i] = "."
        #if is_valid_so_far(tuple(groupc), code):
        sums += lopploop2(tuple(groupc), code)

        groupc = copy.deepcopy(list(group))
        groupc[i] = "#"
        #if is_valid_so_far(tuple(groupc), code):
        sums += lopploop2(tuple(groupc), code)
        return sums
    else:
        return 1 if is_valid(group, code) else 0


def part_one():
    sums = 0

    for i, line in enumerate(input()):
        group, code = line.split(" ")
        group = [g for g in group]
        code = code.split(",")
        sums += lopploop2(tuple(group), tuple(code))
        print("Line: ", i, sums)

    print("Part 1: ", sums)
    #assert(sums == 0)

def part_two2():
    sums = 0
    for i, line in enumerate(input()):
        group_, code_ = line.split(" ")
        group = group_
        code = code_
        for j in range(4):
            group += "?" + group_
            code += "," + code_
        group = tuple([g for g in group])
        code = tuple(code.split(","))
        sums += lopploop2(group, code)
        print("Line: ", i, sums)

    print("Part 2: ", sums)
    #assert(sums == 0)

#@cache
def bfs(group0, code):
    queue = []
    queue.append(group0)

    while queue:
        group = queue.pop(0) 
        i = -1
        for gi, g in enumerate(group):
            if g == "?":
                i = gi
                break
        if i >= 0:
            groupc = copy.deepcopy(group)
            groupc[i] = "."
            if is_valid_so_far(tuple(groupc), code):
                queue.append(groupc)
            # v = lopploop2(groupc, code)
            groupc = copy.deepcopy(group)
            groupc[i] = "#"
            if is_valid_so_far(tuple(groupc), code):
                queue.append(groupc)
        else:
            is_valid(tuple(group), code)

@cache
def lopploop5(group, sizes, num_done_in_group=0):
    if not group:
        if not sizes and num_done_in_group == 0:
            return 1
        else:
            return 0
    num_sols = 0
    neighbours = [".", "#"] if group[0] == "?" else group[0]
    for g in neighbours:
        if g == "#":
            num_sols += lopploop5(group[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += lopploop5(group[1:], sizes[1:])
            else:
                num_sols += lopploop5(group[1:], sizes)
    return num_sols

def part_two():
    global globvar 
    global groups
    sums = 0
    for i, line in enumerate(input()):
        group_, code_ = line.split(" ")
        group = group_
        code = code_
        for j in range(4):
            group += "?" + group_
            code += "," + code_

        code1 = tuple([int(c) for c in code.split(",")])
        #sums = lopploop3(group, code, sums)
        #group = [g for g in group]
        #bfs(group, code1)
        #print("Line: ", i, globvar)
        
        sums += lopploop5(group + ".", code1)
        print("Line: ", i, sums)


    print("Part 2: ", globvar)
    #assert(sums == 0)


#part_one()
part_two2() # 192397389393386 low