import os
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    sum = 0
    for line in input_test():
        tens = 0
        for c in line:
            if c.isdigit():
                tens = int(c)
                break
        ones = 0
        for c in line[::-1]:
            if c.isdigit():
                ones = int(c)
                break
        sum += tens * 10 + ones
    print("Part 1: ", sum)

digges = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def part_two():
    sum = 0
    for line in input_test():
        tens = 0
        for i, c in enumerate(line):
            line_strip = line[i:]
            if c.isdigit():
                tens = int(c)
                break
            for di, d in enumerate(digges):
                if line_strip.startswith(d):
                    tens = di + 1
                    break
            else: # continue on NOT break
                continue
            break  # break on break

        ones = 0
        rev = line[::-1]
        for i, c in enumerate(rev):
            line_strip = rev[i:]
            if c.isdigit():
                ones = int(c)
                break
            for di, d in enumerate(digges):
                if line_strip.startswith(d[::-1]):
                    ones = di + 1
                    break
            else: # only executed if the inner loop did NOT break
                continue
            break  # only executed if the inner loop DID break

        sum += tens * 10 + ones
    print("Part 2: ", sum)

part_one() # 54667
part_two() # 54203