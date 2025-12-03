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


def part_one2():
    sums = 0
    for i, line in enumerate(test()):
        ranges = line.split(",")
        for r in ranges:
            intervals = r.split("-")
            for i in range(int(intervals[0]), int(intervals[1]) + 1):
                i_str = str(i)
                l_str = len(i_str)
                ok = False
                for j in range(1, int(l_str / 2) + 1):
                    inner_ok = True
                    base = i_str[0:j]
                    for x in range(1, int(l_str / j)):
                        if i_str[j*x:j*(x+1)] != base:
                            inner_ok = False
                            break    
                    if inner_ok:
                        ok = True
                        break
                if ok:
                    print(i)
                    sums += i
            
    print("Part 1: ", sums)
    #assert(sums == 0) # high 
    # 64148975435
    # 2633884357545164
    # test 1227775554
    # test 38596002

def part_one():
    sums = 0
    for i, line in enumerate(input()):
        ranges = line.split(",")
        for r in ranges:
            intervals = r.split("-")
            for i in range(int(intervals[0]), int(intervals[1]) + 1):
                istr = str(i)
                if istr[0:int(len(istr)/2)] == istr[int(len(istr)/2):]:
                    print(i)
                    sums += i
            
    print("Part 1: ", sums)

def part_two():
    sums = 0
    for i, line in enumerate(input()):
        ranges = line.split(",")
        for r in ranges:
            intervals = r.split("-")
            for i in range(int(intervals[0]), int(intervals[1]) + 1):
                istr = str(i)
                for j in range(1, int(len(istr)/2)+1):
                    istr = str(i)
                    if len(istr) % j == 0:
                        p1, istr = istr[0:j], istr[j:]
                        if p1 == istr[0:j]:
                            p1, istr = istr[0:j], istr[j:]
                            if not istr:
                                print(i)
                                sums += i
                                break
                            if len(istr) < len(p1):
                                break
                            if p1 == istr[0:j]:
                                p1, istr = istr[0:j], istr[j:]
                                if not istr:
                                    print(i)
                                    sums += i
                                    break
                                if len(istr) < len(p1):
                                    break
                                if p1 == istr[0:j]:
                                    p1, istr = istr[0:j], istr[j:]
                                    if not istr:
                                        print(i)
                                        sums += i
                                        break
                                    if len(istr) < len(p1):
                                        break
                                    if p1 == istr[0:j]:
                                        p1, istr = istr[0:j], istr[j:]
                                        if not istr:
                                            print(i)
                                            sums += i
                                            break
                                        if len(istr) < len(p1):
                                            break
                                        if p1 == istr[0:j]:
                                            p1, istr = istr[0:j], istr[j:]
                                            if not istr:
                                                print(i)
                                                sums += i
                                                break
                                            if len(istr) < len(p1):
                                                break
                                            if p1 == istr[0:j]:
                                                p1, istr = istr[0:j], istr[j:]
                                                if not istr:
                                                    print(i)
                                                    sums += i
                                                    break
                                                if len(istr) < len(p1):
                                                    break


    print("Part 2: ", sums)
    #assert(sums == 0)


#part_one()
part_two()