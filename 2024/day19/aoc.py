import os
from functools import cache


day_path = os.path.dirname(__file__)



def input_raw():
    with open(os.path.join(day_path, "input.txt"), "r") as f:
        return f.read().strip()


def test_raw():
    with open(os.path.join(day_path, "test.txt"), "r") as f:
        return f.read().strip()


@cache
def count_match(ftowles, design):
    count = 0
    for ft in ftowles:
        if design.startswith(ft):
            idx = design.index(ft) + len(ft)
            if not design[idx:]:
                count += 1
            else:
                count += count_match(ftowles, design[idx:])

    return count

def part_one_two():
    towles, designs = input_raw().split("\n\n")
    towles = towles.split(", ")
    designs = designs.split("\n")

    part1 = 0
    part2 = 0
    for design in designs:
        ftowles = tuple([t for t in towles if t in design])
        count = count_match(ftowles, design)

        if count:
            part1 += 1
            part2 += count

    print("Part 1: ", part1)
    assert(part1 == 347)

    print("Part 2: ", part2)
    assert(part2 == 919219286602165)



part_one_two()
