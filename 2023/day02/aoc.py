import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

# only 12 red cubes, 13 green cubes, and 14 blue cubes
def part_one():
    sums = 0
    for id, line in enumerate(input()):
        _, subsets = line.split(":")
        ok = True
        for subset in subsets.split(";"):
            for nbr_color in subset.split(","):
                nbr, color = nbr_color.strip().split()
                if color == "red" and int(nbr) > 12:
                    ok = False
                    break
                if color == "green" and int(nbr) > 13:
                    ok = False
                    break
                if color == "blue" and int(nbr) > 14:
                    ok = False
                    break
        if ok:
            sums += id + 1

    print("Part 1: ", sums)
    assert(sums == 2348)

def part_two():
    sums = 0
    for _, line in enumerate(input()):
        _, subsets = line.split(":")
        red_max = 1
        green_max = 1
        blue_max = 1
        for subset in subsets.split(";"):
            for nbr_color in subset.split(","):
                nbr, col = nbr_color.strip().split()
                if col == "red" and int(nbr) > red_max:
                    red_max = int(nbr)
                if col == "green" and int(nbr) > green_max:
                    green_max = int(nbr)
                if col == "blue" and int(nbr) > blue_max:
                    blue_max = int(nbr)
        sums += red_max * green_max * blue_max

    print("Part 2: ", sums)
    assert(sums == 76008)


part_one()
part_two()