def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


def compare(left, right):
    while True:
        if left and not right or type(left) == int and type(right) == list:
            return 0
        elif not left and right or type(right) == int and type(left) == list:
            return 1
        elif left == right:
            return -1
        elif type(left) == int and type(right) == int:
            return 1 if left < right else 0
        elif type(left) == list and type(right) != list:
            right = [right]
        elif type(left) != list and type(right) == list:
            left = [left]
        left0 = left.pop(0)
        right0 = right.pop(0)
        comp0 = compare(left0, right0)
        if comp0 > -1:
            return comp0

def compare2(left, right):
    while True:
        if type(left) == int and type(right) == int:
            if left == right:
                return 0
            return -1 if left < right else 1
        elif type(left) == list and type(right) == list:
            if left == right:
                return 0
            if left and not right:
                return 1
            elif not left and right:
                return -1
            left0 = left.pop(0)
            right0 = right.pop(0)
            comp0 = compare2(left0, right0)
            if comp0:
                return comp0
        elif type(left) == list and type(right) != list:
            right = [right]
            if left == right:
                return 0
            if left and not right:
                return 1
            elif not left and right:
                return -1
            left0 = left.pop(0)
            right0 = right.pop(0)
            comp0 = compare2(left0, right0)
            if comp0:
                return comp0
        elif type(left) != list and type(right) == list:
            left = [left]
            if left == right:
                return 0
            if left and not right:
                return 1
            elif not left and right:
                return -1
            left0 = left.pop(0)
            right0 = right.pop(0)
            comp0 = compare2(left0, right0)
            if comp0:
                return comp0
import copy
def compare3(left, right):
    l = copy.deepcopy(left)
    r = copy.deepcopy(right)
    c = compare2(l, r)
    if c == 1:
        return -1
    if c == 0:
        return 1
    return 0

def part_one():
    count = 0
    left = None
    right = None
    package = 0
    for line in input():
        if not line:
            left = None
            right = None
            continue
        l = eval(line)
        if left is None:
            left = l
        else:
            package += 1
            right = l
            if compare2(left, right) < 0:
                count += package


    print("Part 1: ", count)
    assert count == 6420

part_one()

import functools
compare_key = functools.cmp_to_key(compare3)

def part_two():
    count = 0
    package = 0
    lines = []
    for line in input():
        if not line:
            continue
        lines.append(eval(line))
    lines.append([[2]])
    lines.append([[6]])
    #sorted_lines = sorted(lines, key=functools.cmp_to_key(compare2))
    print(lines)
    sorted1 = sorted(lines, key=compare_key)
    print(sorted1)
    index = 0
    for l in sorted1:
        index += 1
        if l == [[2]]:
            print(index, 1)
        if l == [[6]]:
            print(index, 2)
    print("Part 2: ", count)
    assert count == 22000


part_two()
