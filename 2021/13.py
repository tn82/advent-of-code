from operator import itemgetter

def ascii_print(grid):
    max_x = max(grid, key=itemgetter(0))[0]
    max_y = max(grid, key=itemgetter(1))[1]
    plot = [[" "] * (max_x + 1) for _ in range(max_y + 1)]
    for coo in grid:
        plot[coo[1]][coo[0]] = "#"
    for row in plot:
        for val in row:
            print(val, end='')
        print()

def day_13():
    file = open('13.txt', 'r')
    grid = {}
    cuts = []
    for line in file:
        row = line.strip().split(",")
        if not row[0]:
            continue
        if len(row) == 1:
            cut = row[0].replace('fold along ', '').split("=")
            cuts.append([cut[0], int(cut[1])])
        else:
            coo = [int(i) for i in row]
            grid[tuple(coo)] = 1

    print_part1 = True
    for cut in cuts:
        grid_cut = {}
        if cut[0] == "y":
            for coo in grid:
                if coo[1] < cut[1]:
                    grid_cut[coo] = 1
                if coo[1] > cut[1]:
                    grid_cut[coo[0], cut[1] * 2 - coo[1]] = 1
        if cut[0] == "x":
            for coo in grid:
                if coo[0] < cut[1]:
                    grid_cut[coo] = 1
                if coo[0] > cut[1]:
                    grid_cut[cut[1] * 2 - coo[0], coo[1]] = 1
        grid = grid_cut
        if print_part1:
            print(f"Part one: {len(grid)}")
            print_part1 = False
    print("Part two:")
    ascii_print(grid)

day_13()