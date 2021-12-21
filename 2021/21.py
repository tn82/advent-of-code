
def dice100(dice, dice_n, n):
    sum = 0
    for _ in range(n):
        dice += 1
        dice_n += 1
        dice = (dice - 1) % 100 + 1
        sum += dice
    return dice, dice_n, sum

def split3(p1s, p2s, p1p, p2p, p1win, p2win, states, multi):
    for s1 in states:
        p1sl = p1s + s1[0]
        p1sl = (p1sl - 1) % 10 + 1
        p1pl = p1p + p1sl
        if p1pl >= 21:
            p1win += s1[1] * multi
        else:
            p2win, p1win = split3(p2s, p1sl, p2p, p1pl, p2win, p1win, states, s1[1] * multi)
    return p1win, p2win

def day21():
    player1_s = 5
    player2_s = 6
    player1_p = 0
    player2_p = 0
    states = []
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                states.append(sum([d1, d2, d3]))
    super_states = []
    for s in range(3,10):
        if states.count(s):
            super_states.append([s, states.count(s)])
    p1w = 0
    p2w = 0
    p1w, p2w = split3(player1_s, player2_s, player1_p, player2_p, p1w, p2w, super_states, 1)
    print(f"Part 2: {p1w}, {p2w}")
    
    dice = 0 
    dice_n = 0
    while True:
        dice, dice_n, sums = dice100(dice, dice_n, 3)
        player1_s += sums
        player1_s = (player1_s - 1) % 10 + 1
        player1_p += player1_s
        if player1_p >= 1000:
            break
        dice, dice_n, sums = dice100(dice, dice_n, 3)
        player2_s += sums
        player2_s = (player2_s - 1) % 10 + 1
        player2_p += player2_s
        if player2_p >= 1000:
            break
    print(f"Part 1: {player2_p * dice_n if player1_p > player2_p else player1_p * dice_n}")

import time
time_start = time.perf_counter()
day21()
print(f"Time: {time.perf_counter() - time_start}") 