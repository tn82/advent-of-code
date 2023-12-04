import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    sums = 0
    for _, line in enumerate(input()):
        _, ll = line.split(":")
        win, my = ll.split("|")
        wins = win.split()
        p = 0.5
        for m in my.split():
            if m in wins:
                p *= 2
        if int(p) > 0:
            sums += p

    print("Part 1: ", sums)
    assert(sums == 17782)


def part_two():
    cards = []
    for card, line in enumerate(input()):
        cards.append(1)
    for card, line in enumerate(input()):
        _, ll = line.split(":")
        win, my = ll.split("|")
        wins = []
        wins = win.split()
        p = 0
        for m in my.split():
            if m in wins:
                p += 1
        if p > 0:
            for i in range(1, min(int(p) + 1, len(cards))):
               cards[card + i] += cards[card]

    print("Part 2: ", sum(cards))
    assert(sum(cards) == 8477787)

part_one()
part_two()