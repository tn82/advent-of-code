import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    freq = 0
    for line in input():
        if line:
            freq += int(line)

    print("Part 1: ", freq)

def part_two():
    freqs = []
    freq = 0
    while True:
        for line in input():
            if line:
                freq += int(line)
                if freq in freqs:
                    print(freq)
                    break
                freqs.append(freq)
        else:
            continue  # only executed if the inner loop did NOT break
        break  # only executed if the inner loop DID break

    print("Part 2: ", freq)

part_one()
part_two()