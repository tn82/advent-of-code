def points(op, me):
    points = 0
    if me == "X":
        points = points + 1
    if me == "Y":
        points = points + 2
    if me == "Z":
        points = points + 3
    if (
        (op == "A" and me == "X")
        or (op == "B" and me == "Y")
        or (op == "C" and me == "Z")
    ):
        points = points + 3
    if me == "X" and op == "C":
        points = points + 6
    if me == "Y" and op == "A":
        points = points + 6
    if me == "Z" and op == "B":
        points = points + 6
    return points


def part_one():
    file = open("input.txt", "r")
    sum = 0
    for line in file:
        op, me = line.strip("\n").split()
        sum = sum + points(op, me)
    print("Part 1: ", sum)


part_one()


def part_two():
    file = open("input.txt", "r")
    sum = 0
    for line in file:
        op, me = line.strip("\n").split()
        if op == "A" and me == "X":
            me = "Z"
        elif op == "A" and me == "Y":
            me = "X"
        elif op == "A" and me == "Z":
            me = "Y"
        elif op == "B" and me == "X":
            me = "X"
        elif op == "B" and me == "Y":
            me = "Y"
        elif op == "B" and me == "Z":
            me = "Z"
        elif op == "C" and me == "X":
            me = "Y"
        elif op == "C" and me == "Y":
            me = "Z"
        elif op == "C" and me == "Z":
            me = "X"

        sum = sum + points(op, me)
    print("Part 2: ", sum)


part_two()
