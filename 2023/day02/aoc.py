import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

# only 12 red cubes, 13 green cubes, and 14 blue cubes
def part_one():
    games = []
    sums = 0
    for id, line in enumerate(input()):
        gamenbr, rest = line.split(":")
        subsets = rest.split(";")
        ok = True
        for sub in subsets:
            colors = sub.split(",")
            for nbrcol in colors:
                nbr, col = nbrcol.strip().split()
                if col == "red" and int(nbr) > 12:
                    ok = False
                    break
                if col == "green" and int(nbr) > 13:
                    ok = False
                    break
                if col == "blue" and int(nbr) > 14:
                    ok = False
                    break
        if ok:
            sums += id + 1

        games.append(subsets)
        #sum += int(line)

    print("Part 1: ", sums)

def part_two():
    games = []
    sums = 0
    for id, line in enumerate(input()):
        gamenbr, rest = line.split(":")
        subsets = rest.split(";")
        ok = True
        red_max = 1
        green_max = 1
        blue_max = 1
        for sub in subsets:
            colors = sub.split(",")
            for nbrcol in colors:
                nbr, col = nbrcol.strip().split()
                if col == "red" and int(nbr) > red_max:
                    red_max = int(nbr)
                if col == "green" and int(nbr) > green_max:
                    green_max = int(nbr)
                if col == "blue" and int(nbr) > blue_max:
                    blue_max = int(nbr)
        sums += red_max * green_max * blue_max

        games.append(subsets)
        #sum += int(line)
    print("Part 2: ", sums)

#part_one()
part_two()