def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


def printer(c: int):
    return c == 20 or c == 60 or c == 100 or c == 140 or c == 180 or c == 220

def ctr(X, c):
    return X <= c <= X + 2

def part_one():
    X = 1
    c = 1
    count = 0
    for line in input():
        com = line.strip().split()
        if com[0] == "noop":
            addx = 0
            c += 1
            if printer(c):
                count += c * X
        else:
            addx = int(com[1])
            c += 1
            if printer(c):
                count += c * X
            X += addx
            c += 1
            if printer(c):
                count += c * X

    print("Part 1: ", count)
    assert count == 15020

    X = 1
    c = 1
    CTR = ""
    for line in input_test():
        com = line.strip().split()
        if com[0] == "noop":
            addx = 0
            if ctr(X, c):
                CTR += "#"
            else:
                CTR += "."
            c += 1
            if c > 40:
                c = 0
                CTR += "\n"
        else:
            addx = int(com[1])
            if ctr(X, c):
                CTR += "#"
            else:
                CTR += "."
            
            c += 1
            if c > 40:
                c = 0
                CTR += "\n"

            if ctr(X, c):
                CTR += "#"
            else:
                CTR += "."
            X += addx
            c += 1
            if c > 40:
                c = 0
                CTR += "\n"



    print(CTR) # Incorrect EFUGLPRP, EFUGLPAP?
    print("Part 2: ", 0)


part_one()
