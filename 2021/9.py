
def day_9():
    file = open('9.txt', 'r')
    input = []
    for line in file:
        line = [int(l) for l in list(line.strip())]
        input.append(line)
    nrows = len(input)
    ncols = len(input[0])

    sum = 0
    for r in range(nrows):
        for c in range(ncols):
            if r > 0:
                if input[r][c] >= input[r - 1][c]:
                    continue
            if c > 0:
                if input[r][c] >= input[r][c - 1]:
                    continue
            if r < nrows - 1:
                if input[r][c] >= input[r + 1][c]:
                    continue
            if c < ncols - 1:
                if input[r][c] >= input[r][c + 1]:
                    continue
            sum += input[r][c] + 1
    print(sum)

#day_9()

def count_basin(input, visited, r, c):
    nrows = len(input)
    ncols = len(input[0])
    counter = 1
    visited[r][c] = 1

    if r > 0:
        if visited[r - 1][c] == 0 and input[r - 1][c] < 9:
            counter += count_basin(input, visited, r - 1, c)
    if c > 0:
        if visited[r][c - 1] == 0 and input[r][c - 1] < 9:
            counter += count_basin(input, visited, r, c - 1)
    if r < nrows - 1:
        if visited[r + 1][c] == 0 and input[r + 1][c] < 9:
            counter += count_basin(input, visited, r + 1, c)
    if c < ncols - 1:
        if visited[r][c + 1] == 0 and input[r][c + 1] < 9:
            counter += count_basin(input, visited, r, c + 1)
    return counter

def day_9_2():
    file = open('9.txt', 'r')
    input = []
    for line in file:
        line = [int(l) for l in list(line.strip())]
        input.append(line)
    nrows = len(input)
    ncols = len(input[0])

    basins = []
    visited = [[0]*ncols for i in range(nrows)]
    for r in range(nrows):
        for c in range(ncols):
            if r > 0:
                if input[r][c] >= input[r - 1][c]:
                    continue
            if c > 0:
                if input[r][c] >= input[r][c - 1]:
                    continue
            if r < nrows - 1:
                if input[r][c] >= input[r + 1][c]:
                    continue
            if c < ncols - 1:
                if input[r][c] >= input[r][c + 1]:
                    continue
            bas = count_basin(input, visited, r, c)
            basins.append(bas)

    basins = sorted(basins)
    print(basins[-1])
    print(basins[-2])
    print(basins[-3])
    print(basins[-1] * basins[-2] * basins[-3])

day_9_2()
