import os
from collections import defaultdict
import heapq
import copy
from functools import cache

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]

def part_one():
    sums = 0
    for i, line in enumerate(input()):
        bank = int_list(line)
        max_value = max(bank[:-1])
        first_index = bank.index(max_value)
        max_value2 = max(bank[first_index + 1:])
        m = str(max_value) + str(max_value2)
        print(m)
        sums += int(m)

    print("Part 1: ", sums)
    #assert(sums == 0)


def part_two():
    sums = 0
    for i, line in enumerate(input()):
        bank = int_list(line)
        max_value1 = max(bank[:-11])
        idx1 = bank.index(max_value1)
        max_value2 = max(bank[idx1 + 1:-10])
        idx2 = bank[idx1+1:].index(max_value2)+1+idx1
        max_value3 = max(bank[idx2 + 1:-9])
        idx3 = bank[idx2+1:].index(max_value3)+1+idx2
        max_value4 = max(bank[idx3 + 1:-8])
        idx4 = bank[idx3+1:].index(max_value4)+1+idx3
        max_value5 = max(bank[idx4 + 1:-7])
        idx5 = bank[idx4+1:].index(max_value5)+1+idx4
        max_value6 = max(bank[idx5 + 1:-6])
        idx6 = bank[idx5+1:].index(max_value6)+1+idx5
        max_value7 = max(bank[idx6 + 1:-5])
        idx7 = bank[idx6+1:].index(max_value7)+1+idx6
        max_value8 = max(bank[idx7 + 1:-4])
        idx8 = bank[idx7+1:].index(max_value8)+1+idx7
        max_value9 = max(bank[idx8 + 1:-3])
        idx9 = bank[idx8+1:].index(max_value9)+1+idx8
        max_value10 = max(bank[idx9 + 1:-2])
        idx10 = bank[idx9+1:].index(max_value10)+1+idx9
        max_value11 = max(bank[idx10 + 1:-1])
        idx11 = bank[idx10+1:].index(max_value11)+1+idx10
        max_value12 = max(bank[idx11 + 1:])

        m = str(max_value1) + str(max_value2)+ str(max_value3)+ str(max_value4)+ str(max_value5)+ str(max_value6)+ str(max_value7)+ str(max_value8)+ str(max_value9)+ str(max_value10)+ str(max_value11)+ str(max_value12)
        print(m)
        sums += int(m)

    print("Part 2: ", sums)
    #assert(sums == 0)


#part_one()
part_two()