import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]


def part_one():
    part_one = 0
    for line in input():
        fuel = int(line)
        fuel /= 3
        fuel = int(fuel) - 2
        part_one += fuel

    print("Part 1: ", part_one)
    assert 3224048 == part_one

def fuels(mass):
    fuel_tot = 0
    fuel = mass / 3
    fuel = int(fuel) - 2
    if fuel <= 0:
        return fuel_tot
    else:
        fuel_tot += fuel + fuels(fuel)
        return fuel_tot

def part_two():
    part_two = 0
    for line in input():
        part_two += fuels(int(line))

    print("Part 2: ", part_two)
    assert 4833211 == part_two


part_one()
part_two()
