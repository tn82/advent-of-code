from operator import itemgetter

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
            cuts.append(cut)
        else:
            coo = [int(i) for i in row]
            grid[tuple(coo)] = 1

    for cut in cuts:
        grid_cut = {}
        c = int(cut[1])
        if cut[0] == "y":
            for coo in grid:
                if coo[1] < c:
                    grid_cut[coo] = 1
                if coo[1] > c:
                    grid_cut[coo[0], c * 2 - coo[1]] = 1
        if cut[0] == "x":
            for coo in grid:
                if coo[0] < c:
                    grid_cut[coo] = 1
                if coo[0] > c:
                    grid_cut[c * 2 - coo[0], coo[1]] = 1
        grid = grid_cut
    print(f"Part one: {len(grid)}")

    max_x = max(grid, key=itemgetter(0))[0]
    max_y = max(grid, key=itemgetter(1))[1]
    plot = [["."] * (max_x + 1) for _ in range(max_y + 1)]
    print(f"Part two:")
    x = []
    y = []
    for coo in grid:
        y.append(-coo[1])
        x.append(coo[0])
        plot[coo[1]][coo[0]] = "#"
    for row in plot:
        for val in row:
            print(val, end='')
        print()

day_13()