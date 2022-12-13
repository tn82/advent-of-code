import functools
import copy


def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]


def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        return -1 if left < right else 1
    elif type(left) == list and type(right) != list:
        right = [right]
    elif type(left) != list and type(right) == list:
        left = [left]
    if left == right:
        return 0
    if left and not right:
        return 1
    elif not left and right:
        return -1
    comp0 = compare(left[0], right[0])
    if comp0:
        return comp0
    return compare(left[1:], right[1:])


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
            if compare(left, right) < 0:
                count += package


    print("Part 1: ", count)
    assert count == 6420


part_one()


def part_two():
    count = 0
    lines = []
    for line in input():
        if not line:
            continue
        lines.append(eval(line))
    lines.append([[2]])
    lines.append([[6]])
    sorted1 = sorted(lines, key=functools.cmp_to_key(compare))
    count = 1
    for i, l in enumerate(sorted1):
        if l == [[2]] or l == [[6]]:
            count *= (i + 1)
    print("Part 2: ", count)
    assert count == 22000


part_two()
