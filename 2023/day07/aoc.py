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

def part_one():
    sums = 0
    cards_ = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards = {}
    for i, c in enumerate(cards_):
        cards[c] = i
    hands_by_rank = defaultdict(list)
    for i, line in enumerate(input()):
        hand_, bid = line.split()
        hand = [c for c in hand_]
        hand_count = {h: hand.count(h) for h in hand}
        hand_count["bid"] = bid
        hand_count["hand"] = hand
        if 5 in hand_count.values():
            hands_by_rank[7].append(hand_count)
        elif 4 in hand_count.values():
            hands_by_rank[6].append(hand_count)
        elif 3 in hand_count.values() and 2 in hand_count.values():
            hands_by_rank[5].append(hand_count)
        elif 3 in hand_count.values():
            hands_by_rank[4].append(hand_count)
        elif list(hand_count.values()).count(2) == 2:
            hands_by_rank[3].append(hand_count)
        elif 2 in hand_count.values():
            hands_by_rank[2].append(hand_count)
        else:
            hands_by_rank[1].append(hand_count)
    rank = 1
    for p, hands in sorted(hands_by_rank.items()):
        if len(hands) == 1:
            sums += int(hands[0]["bid"]) * rank
            rank += 1
        else:
            hands.sort(key=lambda h: (cards[h["hand"][0]], cards[h["hand"][1]], cards[h["hand"][2]], cards[h["hand"][3]], cards[h["hand"][4]]))
            hands.reverse()
            for han in hands:
                sums += int(han["bid"]) * rank
                rank += 1

    print("Part 1: ", sums)
    assert(sums == 250370104)


def part_two():
    sums = 0
    cards_ = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    cards = {}
    for i, c in enumerate(cards_):
        cards[c] = i
    hands_by_rank = defaultdict(list)
    for i, line in enumerate(input()):
        hand_, bid = line.split()
        hand = [c for c in hand_]
        hand_count = {h: hand.count(h) for h in hand}
        maxc = 0
        for k, v in hand_count.items():
            if k != "J" and v > maxc:
                maxc = v

        hand_count["bid"] = bid
        hand_count["hand"] = hand
        jc = hand_count["J"] if "J" in hand_count else 0
        if maxc + jc == 5:
            hands_by_rank[7].append(hand_count)
        elif maxc + jc == 4:
            hands_by_rank[6].append(hand_count)
        elif 3 in hand_count.values() and 2 in hand_count.values():
            hands_by_rank[5].append(hand_count)
        elif list(hand_count.values()).count(2) == 2 and jc == 1:
            hands_by_rank[5].append(hand_count)
        elif maxc + jc == 3:
            hands_by_rank[4].append(hand_count)
        elif list(hand_count.values()).count(2) == 2:
            hands_by_rank[3].append(hand_count)
        elif 2 in hand_count.values() and jc == 1:
            hands_by_rank[3].append(hand_count)
        elif maxc + jc == 2:
            hands_by_rank[2].append(hand_count)
        else:
            hands_by_rank[1].append(hand_count)
    rank = 1
    for p, hands in sorted(hands_by_rank.items()):
        if len(hands) == 1:
            sums += int(hands[0]["bid"]) * rank
            rank += 1
        else:
            hands.sort(key=lambda h: (cards[h["hand"][0]], cards[h["hand"][1]], cards[h["hand"][2]], cards[h["hand"][3]], cards[h["hand"][4]]))
            hands.reverse()
            for han in hands:
                sums += int(han["bid"]) * rank
                rank += 1

    print("Part 2: ", sums)
    assert(sums == 251735672)


part_one()
part_two()