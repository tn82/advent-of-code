enchance = "##....###.#.##...##....####..###.#.######.#.#.##.#.####.#.#####.##.##..##.###.###..##.##..#####.##..#..##..#...#.####..#.###..#....####.#..##.##...#######.###...#.######..#..#...###..###.#####.##..#.#.###.#.###.#..#.###.###.#..##.....####..#.##.##.#..#...###.#.....##..#....#.##..#....#....####.#...#.#.##.#...#.##..#..#.#..###.###.#.##...##.#.##.##..#..##.#..#...######.#.#..###....##...##....#....##....#.#..##..#####.####.#.##...#...#.#.#....#.####...#.##..#...#..#....#..#..#..##.#.#.#.#######.###..##.#....."
# test data
#enchance = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"

def day_20():
    grid = {}
    # Padding
    steps = 50
    dim = 100
    for x in range(-2*steps,dim+steps*2):
        for y in range(-2*steps,dim+steps*2):
            grid[x, y] = 0
    r = 0
    file = open('20.txt', 'r')
    for line in file:
        c = 0
        row = line.strip()
        for l in row:
            grid[r, c] = 1 if l == "#" else 0
            c += 1
        r += 1
    print(r,c)

    for _ in range(50):
        print(len([k for k, v in grid.items() if v == 1]))
        new_grid = {}
        for p in grid:
            p_bin = ""
            for x in range(p[0]-1, p[0]+2):
                for y in range(p[1]-1, p[1]+2):
                    p_bin += "0" if (x, y) not in grid else str(grid[x, y])
            new_grid[p] = 1 if enchance[int(p_bin, 2)] == "#" else 0
        grid = new_grid

    # Trim, for every step the outter bounderies is corrupted
    for x in range(-2*steps,dim+steps*2):
        for y in range(-2*steps,dim+steps*2):
            if x > (dim + steps) or x < -steps or y > (dim + steps) or y < -steps:
                grid[x, y] = 0
    print(len([k for k, v in grid.items() if v == 1])) # 5461 correct # 18226 correct

day_20()