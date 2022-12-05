s1 = "QFMRLWCV"
s2 = "DQL"
s3 = "PSRGWCNB"
s4 = "LCDHBQG"
s5 = "VGLFZS"
s6 = "DGNP"
s7 = "DZPVFCW"
s8 = "CPDMS"
s9 = "ZNWTVMPC"


stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]


def part_one():
    file = open("input.txt", "r")
    for line in file:
        line = line.strip()
        if not "move" in line:
            continue
        _, steps, __, from1, ___, dest = line.split(" ")
        steps = int(steps)
        from1 = int(from1) - 1
        dest = int(dest) - 1
        for s in range(steps):
            c = stacks[from1][-1]
            stacks[dest] += c
            stacks[from1] = stacks[from1][:-1]
    res = ""
    for s in stacks:
        res += s[-1]

    assert res == "VWLCWGSDQ"
    print("Part 1: ", res)


part_one()


stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]


def part_two():
    file = open("input.txt", "r")
    for line in file:
        line = line.strip()
        if not "move" in line:
            continue
        _, steps, __, from1, ___, dest = line.split(" ")
        steps = int(steps)
        from1 = int(from1) - 1
        dest = int(dest) - 1
        c = stacks[from1][-steps:]
        stacks[dest] += c
        stacks[from1] = stacks[from1][:-steps]
    res = ""
    for s in stacks:
        res += s[-1]

    assert res == "TCGLQSLPW"
    print("Part 2: ", res)


part_two()
