def part_one():
    file = open("input.txt", "r")
    forrest = {}
    for y, line in enumerate(file):
        line = line.strip()
        for x, r in enumerate(line.strip()):
            forrest[(x, y)] = int(r)
    x_max = x
    y_max = y
    count = 0
    for key, val in forrest.items():
        x, y = key
        blockers = 0
        for i in range(0, x):
            if forrest[(i, y)] >= val:
                blockers += 1
                break
        for i in range(x + 1, x_max + 1):
            if forrest[(i, y)] >= val:
                blockers += 1
                break
        for j in range(0, y):
            if forrest[(x, j)] >= val:
                blockers += 1
                break
        for j in range(y + 1, y_max + 1):
            if forrest[(x, j)] >= val:
                blockers += 1
                break
        if blockers < 4:
            count += 1

    print("Part 1: ", count)
    assert count == 1782

    best_view = 0
    for key, val in forrest.items():
        x, y = key
        if x == 0 or x == x_max or y == 0 or y == y_max:
            continue
        view1 = 0
        for i in range(max(x - 1, 0), -1, -1):
            view1 += 1
            if forrest[(i, y)] >= val:
                break
        view2 = 0
        for i in range(x + 1, x_max + 1):
            view2 += 1
            if forrest[(i, y)] >= val:
                break
        view3 = 0
        for j in range(max(y - 1, 0), -1, -1):
            view3 += 1
            if forrest[(x, j)] >= val:
                break
        view4 = 0
        for j in range(y + 1, y_max + 1):
            view4 += 1
            if forrest[(x, j)] >= val:
                break
        view = view1 * view2 * view3 * view4
        if view > best_view:
            best_view = view

    print("Part 2: ", best_view)
    assert best_view == 474606


part_one()
