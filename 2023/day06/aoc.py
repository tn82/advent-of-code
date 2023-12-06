
def day06(input):
    sums = 1
    for race in input:
        time, dist = race
        wins = 0
        for t in range(1, time):
            if t * (time - t) > dist:
                wins += 1
        sums *= wins

    return sums

part1 = day06(((48, 255), (87, 1288), (69, 1117), (81, 1623)))
print(f"Part 1: {part1}")
assert(part1 == 252000)

part2 = day06(((48876981, 255128811171623),))
print(f"Part 2: {part2}")
assert(part2 == 36992486)
