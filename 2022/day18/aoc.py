def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]

shifts = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def find_air(p, grid, visited, mins, maxs):
    for shift in shifts:
        ps = (shift[0] + p[0], shift[1] + p[1], shift[2] + p[2])
        if ps not in grid and ps not in visited:
            visited.add(ps)
            if ps[0] > maxs[0] or ps[0] < mins[0] or ps[1] > maxs[1] or ps[1] < mins[1] or ps[2] > maxs[2] or ps[2] < mins[2]:
                return 1
            else:
                c = find_air(ps, grid, visited, mins, maxs)
                if c != 0:
                    return c
    return 0


def day18():
    grid = {}
    for line in input():
        x, y, z = line.split(",")
        grid[(int(x), int(y), int(z))] = 1

    xs = [x for (x, _, _) in grid.keys()]
    ys = [y for (_, y, _) in grid.keys()]
    zs = [z for (_, _, z) in grid.keys()]
    mins = (min(xs), min(ys), min(zs))
    maxs = (max(xs), max(ys), max(zs))

    part_one = 0
    part_two = 0
    visited_interior = set()
    for p in grid:
        for shift in shifts:
            ps = (shift[0] + p[0], shift[1] + p[1], shift[2] + p[2])
            if ps not in grid:
                part_one += 1
                visited = visited_interior.copy()
                c = find_air(ps, grid, visited, mins, maxs)
                if c == 0:
                    visited_interior = visited_interior.union(visited)
                part_two += c


    print("Part 1: ", part_one)
    assert part_one == 3564

    print("Part 2: ", part_two)
    assert part_two == 2106


day18()
