
def day_13():
    file = open('13.txt', 'r')
    empty_found = False
    input = []
    cuts = []
    for line in file:
        s = line.strip().split(",")
        if not s[0]:
            empty_found = True
            continue
        if empty_found:
            s1 = s[0].replace('fold along ', '')
            cuts.append(s1.split("="))
        else:
            row = [int(l) for l in list(s)]
            input.append(row)
    grid = {}
    for coo in input:
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
    plot2 = [["0"] * 40 for _ in range(40)]
    for coo in grid:
        if coo[0] > 9+20:
            plot2[coo[1]][coo[0] - 30] = "#"
    print(plot2)
    print(f"Part two: {0}")

day_13()