import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

#Time:        48     87     69     81
#Distance:   255   1288   1117   1623

# Time:      7  15   30
# Distance:  9  40  200
def part_one():
    tests = ((7, 9), (15, 40), (30, 200))
    inputs = ((48, 255), (87, 1288), (69, 1117), (81, 1623))
    sums = 1
    for race in inputs:
        time, dist = race
        wins = 0
        for t in range(1, time):
            speed = t
            d = speed * (time - t)
            if d > dist:
                wins += 1
        sums *= wins



    print("Part 1: ", sums)
    #assert(sums == 0)


def part_two():
    tests = (71530, 940200)
    inputs = (48876981, 255128811171623)
    sums = 1
    time, dist = inputs
    wins = 0
    for t in range(1, time):
        speed = t
        d = speed * (time - t)
        if d > dist:
            wins += 1
    sums *= wins
    print("Part 2: ", sums)

#part_one()
part_two()