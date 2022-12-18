def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]

def day15():
    count = 0
    gridS = {}
    gridB = {}
    for line in input():
        line = line.replace("Sensor at ", "")
        line = line.replace(" closest beacon is at ", "")
        S, B = line.split(":")
        Sx, Sy = S.split(", ")
        Bx, By = B.split(", ")
        Sx = int(Sx.replace("x=", ""))
        Sy = int(Sy.replace("y=", ""))
        Bx = int(Bx.replace("x=", ""))
        By = int(By.replace("y=", ""))
        dist = abs(Sx - Bx) + abs(Sy - By)
        gridS[(Sx, Sy)] = dist
        gridB[(Bx, By)] = 1

    count = 0
    grid = {}
    for coo, dist in gridS.items():
        Sx = coo[0]
        Sy = coo[1]
        if Sy - dist <= 2000000 <= Sy + dist:
            for x in range(Sx - dist, Sx + dist + 1):
                y = 2000000
                if abs(Sx - x) + abs(Sy - y) > dist:
                    continue
                if (x, y) in gridB:
                    continue
                grid[(x, y)] = 1

    count = len(grid)

    print("Part 1: ", count)
    assert count == 5367037

    count = 0
    found = False
    done = False
    x = 2960000 # Speed up test
    lim = 4000000
    while not done:
        if x > lim:
            break
        if x % 40000 == 0:
            print(x)
        y = 0
        while True:
            found = False
            if y > lim:
                break
            for coo, dist in gridS.items():
                Sx, Sy = coo
                p_dist = abs(Sx - x) + abs(Sy - y)
                if p_dist <= dist:
                    y = Sy + dist - abs(Sx - x) + 1
                    found = True
                    break
            if not found:
                print(x, y)
                count = x * 4000000 + y
                done = True
                break
        x += 1

    print("Part 2: ", count)
    assert count == 11914583249288

day15()