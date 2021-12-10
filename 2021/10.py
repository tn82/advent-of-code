
def lists_to_dict(l1, l2):
    res = {}
    for a, b in zip(l1, l2):
        res[a] = b
        res[b] = a
    return res

def day_10():
    file = open('10.txt', 'r')
    input = []
    for line in file:
        input.append(line)

    part1_sum = 0
    open_chars = "([{<"
    close_chars = ")]}>"
    chars_map = lists_to_dict(open_chars, close_chars)
    part1_points_map = lists_to_dict(close_chars, [3, 57, 1197, 25137])
    part2_points_map = lists_to_dict(close_chars, [1, 2, 3, 4])
    part2_points = []
    for row in input:
        parsed = ""
        good = True
        for c in row:
            if c in open_chars:
                parsed = parsed + c
            if c in close_chars:
                if not parsed:
                    part1_sum += part1_points_map[c]
                    good = False
                    break
                if chars_map[c] != parsed[-1]:
                    part1_sum += part1_points_map[c]
                    good = False
                    break
                else:
                    parsed = parsed[:-1]
        if good:
            points = 0
            for c in reversed(parsed):
                points = points * 5 + part2_points_map[chars_map[c]]
            part2_points.append(points)

    print(f"Part one: {part1_sum}")
    print(f"Part two: {sorted(part2_points)[int(len(part2_points) / 2 - 0.5)]}")

day_10()