import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return file.read()


def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return file.read()

def int_list(char_list):
    return [int(c) for c in char_list]

def part_one():
    sums = 0
    data = int_list(list(str(input())))
    id = 0
    parsed = []
    while data:
        blocks = data.pop(0)
        siz = data.pop(0) if data else 0
        for i in range(int(blocks)):
            parsed.append(id)
        for i in range(siz):
            parsed.append(".")
        id += 1


    for ri, r in enumerate(reversed(parsed)):
        if r != ".":
            try:
                index = parsed.index(".")
                if index >= len(parsed) - ri - 1:
                    break
                parsed[index] = r
                parsed[len(parsed) - ri - 1] = "."
            except ValueError:
                print(parsed)
            parsed.index(".")

    for i, p in enumerate(parsed):
        if p == ".":
            break
        sums += p * i
    print("Part 1: ", sums)
    assert(sums == 6320029754031)


def find_consecutive_values(my_list, value, count, max_index):
  consecutive_count = 0
  for i in range(len(my_list)):
    if i >= max_index:
        break
    if my_list[i] == value:
      consecutive_count += 1
      if consecutive_count == count:
        return i - count + 1
    else:
      consecutive_count = 0
  return -1


def part_two():
    sums = 0
    sums = 0
    data = int_list(list(str(input())))
    id = 0
    parsed = []
    while data:
        blocks = data.pop(0)
        siz = data.pop(0) if data else 0
        for i in range(int(blocks)):
            parsed.append(id)
        for i in range(siz):
            parsed.append(".")
        id += 1

    tested = set()
    for ri, r in enumerate(reversed(parsed)):
        if r != ".":
            if r in tested:
                continue
            tested.add(r)
            try:
                i_first = parsed.index(r)
                tot = len(parsed) - ri - i_first
                index = find_consecutive_values(parsed, ".", tot, len(parsed) - ri - 1)
                if index < 0:
                    continue
                if index >= len(parsed) - ri - 1:
                    break
                for _ in range(tot):
                    parsed[index] = r
                    parsed[len(parsed) - ri - 1] = "."
                    index += 1
                    ri += 1
            except ValueError:
                print(parsed)

    for i, p in enumerate(parsed):
        if p == ".":
            continue
        sums += p * i
    print("Part 2: ", sums)
    assert(sums == 6347435485773)


part_one()
part_two()