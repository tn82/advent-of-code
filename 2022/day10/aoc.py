def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]


def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


def check_signal(c: int):
    return c == 20 or c == 60 or c == 100 or c == 140 or c == 180 or c == 220


def update_cyle(X, cycle, pixel, CTR):
    if X - 1 <= pixel <= X + 1:
        CTR += "#"
    else:
        CTR += "."
    cycle += 1
    pixel += 1
    if pixel > 39:
        pixel = 0
        CTR += "\n"

    return cycle, pixel, CTR


def day10():
    X = 1
    cycle = 1
    count = 0
    pixel = 0
    CTR = ""
    for line in input():
        com = line.strip().split()
        if com[0] == "noop":
            cycle, pixel, CTR = update_cyle(X, cycle, pixel, CTR)
            if check_signal(cycle):
                count += cycle * X
        else:
            addx = int(com[1])
            cycle, pixel, CTR = update_cyle(X, cycle, pixel, CTR)
            if check_signal(cycle):
                count += cycle * X
            cycle, pixel, CTR = update_cyle(X, cycle, pixel, CTR)
            X += addx
            if check_signal(cycle):
                count += cycle * X

    print("Part 1: ", count)
    assert count == 15020

    print(CTR)
    print("Part 2: ", "EFUGLPAP")


day10()
