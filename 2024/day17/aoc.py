import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]

def xor(a, b):
    return a ^ b
    return (a and not b) or (not a and b)

import math


def part_two():
    # 7749869, 24510697, 24510701, 91635949
    prog = [2,4,1,6,7,5,4,6,1,4,5,5,0,3,3,0]

    test1 = 1
    a = 1
    pattern = []
    while True:
        #a = 84688 * int(math.pow(8, expe)) + a
        ai = a
        if ai % 1000000 == 0:
            print(ai)
        b = 0
        c = 0
        res = []
        i = 0
        add2 = False
        while True:
            if add2:
                i += 2
            if i > len(prog) - 2:
                if prog[-test1:] == res[-test1:]:
                    print(ai, res, len(res))
                    pattern.append(ai)
                    test1 += 1
                    a = ai * 8
                else:
                    a = ai + 1

                if prog == res:
                    print("Part2: ", ai)
                    assert(ai == 90938893795561)
                    exit()
                break
            opcode = prog[i]
            operand = prog[i+1]
            combo = operand
            literal = operand
            if combo == 4:
                combo = a
            elif combo == 5:
                combo = b
            elif combo == 6:
                combo = c
            elif combo == 7:
                break # Error

            if opcode == 3 and a != 0:
                add2 = False
            else:
                add2 = True


            if opcode == 0:
                a = math.trunc(float(a) / math.pow(2, combo))
            elif opcode == 1:
                b = xor(b, literal)
            elif opcode == 2:
                b = combo % 8
            elif opcode == 3:
                if a == 0:
                    continue
                i = literal
            elif opcode == 4:
                b = xor(b, c)
            elif opcode == 5:
                res.append(combo % 8)
            elif opcode == 6:
                b = math.trunc(float(a) / math.pow(2, combo))
            elif opcode == 7:
                c = math.trunc(float(a) / math.pow(2, combo))
            else:
                print("Error > 7")


def part_one():
    sums = 0
    a = 66171486
    b = 0
    c = 0
    prog = [2,4,1,6,7,5,4,6,1,4,5,5,0,3,3,0]
    

    res = []
    i = 0
    add2 = False
    while True:
        if add2:
            i += 2
        if i > len(prog) - 2:
            break
        opcode = prog[i]
        operand = prog[i+1]
        combo = operand
        literal = operand
        if combo == 4:
            combo = a
        elif combo == 5:
            combo = b
        elif combo == 6:
            combo = c
        elif combo == 7:
            print("Error 7 combo")

        if opcode == 3 and a != 0:
            add2 = False
        else:
            add2 = True


        if opcode == 0:
            a = math.trunc(float(a) / math.pow(2, combo))
        elif opcode == 1:
            b = xor(b, literal)
        elif opcode == 2:
            b = combo % 8
        elif opcode == 3:
            if a == 0:
                continue
            i = literal
        elif opcode == 4:
            b = xor(b, c)
        elif opcode == 5:
            res.append(combo % 8)
        elif opcode == 6:
            b = math.trunc(float(a) / math.pow(2, combo))
        elif opcode == 7:
            #print("Error 7")
            c = math.trunc(float(a) / math.pow(2, combo))
        else:
            print("Error > 7")
    rr = ""
    for r in res:
        rr += str(r) + ","
    sums = rr # 236216121 wrong

    print("Part 1: ", sums)
    assert(sums == "2,3,6,2,1,6,1,2,1,")

part_one()
part_two()