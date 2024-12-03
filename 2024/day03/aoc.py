import os
import re

day_path = os.path.dirname(__file__)


def input_raw():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return file.readline()


def part_one():
    sums = 0
    message = re.findall(r"(mul\(\d+,\d+\))", input_raw())
    for op in message:
        dig = re.findall(r"(\d+)", op)
        sums += int(dig[0]) * int(dig[1])

    print("Part 1: ", sums)
    assert sums == 179834255


def part_two():
    sums = 0
    message = re.findall(r"(mul\(\d+,\d+\)|do\(\)||don't\(\))", input_raw())
    active = True
    for op in message:
        if not op:
            continue
        if "mul" in op:
            if active:
                dig = re.findall(r"(\d+)", op)
                sums += int(dig[0]) * int(dig[1])
        elif "don't" in op:
            active = False
        elif "do(" in op:
            active = True
        else:
            raise ValueError(op)

    print("Part 2: ", sums)
    assert sums == 80570939


part_one()
part_two()
