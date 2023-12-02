import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    sum = 0
    for line in input():
        sum += int(line)

    print("Part 1: ", sum)

def part_two():
    sum = 0
    for line in input():
        sum += int(line)

    print("Part 2: ", sum)

part_one()
#part_two()