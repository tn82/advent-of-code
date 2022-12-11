def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


def check_signal(c: int):
    return c == 20 or c == 60 or c == 100 or c == 140 or c == 180 or c == 220

def ctr(X, pixel):
    return X - 1 <= pixel <= X + 1

def part_one():
    X = 1
    c = 1
    count = 0
    for line in input():
        com = line.strip().split()
        if com[0] == "noop":
            addx = 0
            c += 1
            if check_signal(c):
                count += c * X
        else:
            addx = int(com[1])
            c += 1
            if check_signal(c):
                count += c * X
            X += addx
            c += 1
            if check_signal(c):
                count += c * X

    print("Part 1: ", count)
    assert count == 15020

    X = 1
    c = 1
    count = 0
    pixel = 0
    CTR = ""
    for line in input():
        com = line.strip().split()
        if com[0] == "noop":
            if ctr(X, pixel):
                CTR += "#"
            else:
                CTR += "."
            c += 1
            pixel += 1
            if pixel > 39:
                pixel = 0
                CTR += "\n"
            if check_signal(c):
                count += c * X
            
        else:
            addx = int(com[1])
            
            if ctr(X, pixel):
                CTR += "#"
            else:
                CTR += "."
            c += 1
            pixel += 1
            if pixel > 39:
                pixel = 0
                CTR += "\n"
            if check_signal(c):
                count += c * X

            if ctr(X, pixel):
                CTR += "#"
            else:
                CTR += "."
            c += 1
            pixel += 1
            if pixel > 39:
                pixel = 0
                CTR += "\n"
            if check_signal(c):
                count += c * X
            X += addx



    print("Part 1: ", count)
    assert count == 15020

    print(CTR) # EFUGLPAP
    print("Part 2: ", "EFUGLPAP")


part_one()
