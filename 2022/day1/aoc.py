def part_one():
    file = open("input.txt", "r")
    calories = []
    cal_tmp = 0
    for line in file:
        line = line.strip()
        if line:
            cal_tmp = cal_tmp + int(line)
        else:
            calories.append(cal_tmp)
            cal_tmp = 0
    calories.sort(reverse=True)
    print("Part 1: ", calories[0])
    print("Part 2: ", sum(calories[0:3]))


part_one()
