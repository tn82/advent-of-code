import copy
import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]


def computer(program, noun, verb):
    program = copy.deepcopy(program)
    program[1] = noun
    program[2] = verb
    i = 0
    while i < len(program):
        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            i += 4
        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
            i += 4
        elif program[i] == 99:
            break
    return program[0]


def part_two(program):
    for noun in range(0, 100):
        for verb in range(0, 100):
            res = computer(program, noun, verb)
            if 19690720 == res:
                return 100 * noun + verb

def aoc():
    part_one = 0
    program = []
    for line in input():
        for i in line.split(","):
            program.append(int(i))

    part_one = computer(program, 12, 2)
    print("Part 1: ", part_one)
    assert 3166704 == part_one

    two = part_two(program)
    print("Part 2: ", two)
    assert 8018 == two


aoc()
