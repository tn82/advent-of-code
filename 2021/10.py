
def day_10():
    file = open('10.txt', 'r')
    input = []
    for line in file:
        input.append(line)

    part1_sum = 0
    open_chars = "([{<"
    close_chars = ")]}>"
    close_map = {}
    close_map[")"] = "("
    close_map["]"] = "["
    close_map["}"] = "{"
    close_map[">"] = "<"
    open_map = {}
    open_map["("] = ")"
    open_map["["] = "]"
    open_map["{"] = "}"
    open_map["<"] = ">"
    closep_map = {}
    closep_map[")"] = 3
    closep_map["]"] = 57
    closep_map["}"] = 1197
    closep_map[">"] = 25137
    
    close2_map = {}
    close2_map[")"] = 1
    close2_map["]"] = 2
    close2_map["}"] = 3
    close2_map[">"] = 4
    input2 = []
    part2_points = []
    for row in input:
        s = ""
        good = True
        for c in row:
            if c in open_chars:
                s = s + c
            if c in close_chars:
                if not s:
                    part1_sum += closep_map[c]
                    good = False
                    break
                if close_map[c] != s[-1]:
                    part1_sum += closep_map[c]
                    good = False
                    break
                else:
                    s = s[:-1]
        if good:
            input2.append(row)
            points = 0
            for c2 in reversed(s):
                points = points * 5 + close2_map[open_map[c2]]
            part2_points.append(points)

    print(f"Part one: {part1_sum}")
    print(f"Part two: {sorted(part2_points)[int(len(part2_points) / 2 - 0.5)]}")

day_10()