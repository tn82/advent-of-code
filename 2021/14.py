import string


def day_14():
    file = open('14_test.txt', 'r')
    state = ""
    input = []
    first = True
    for line in file:
        if first:
            state = line.strip()
            first = False
        elif line.strip():
            row = line.strip().split(" -> ")
            input.append(row)
    
    for _ in range(10):
        hits = {}
        for instruction in input:
            i = 0
            while i < len(state) - 1:
                idx = state.find(instruction[0], i, (len(state)))
                if idx != -1:
                    hits[idx + 1] = instruction[1]
                    i = idx + 1
                else:
                    break
        for idx, instruc in sorted(hits.items(), key=lambda item: item[0], reverse=True):
            state = state[:idx] + instruc + state[idx:]

    min = 10000000
    max = 0
    state_set = set()
    for c in state:
        state_set.add(c)
    for c in state_set:
        c1 = state.count(c)
        if c1 > max:
            max = c1
        if c1 < min:
            min = c1

    print(f"Part one: {max - min}")  #3048 correct

from collections import defaultdict
def day_14_2():
    file = open('14.txt', 'r')
    state = ""
    input = []
    first = True
    for line in file:
        if first:
            state = line.strip()
            first = False
        elif line.strip():
            row = line.strip().split(" -> ")
            input.append(row)
    c_d = defaultdict(int)
    c_d[state[-1]] = 1
    combos = defaultdict(int)
    for i, _ in enumerate(state):
        if i > len(state) - 2:
            break
        combos[state[i] + state[i + 1]] += 1
    for _ in range(40):
        combos_tmp = defaultdict(int)
        for instruction in input:
            if instruction[0] in combos:
                new1 = instruction[0][0] + instruction[1]
                new2 = instruction[1] + instruction[0][1]
                combos_tmp[new1] += combos[instruction[0]]
                combos_tmp[new2] += combos[instruction[0]]
                combos[instruction[0]] = 0
        combos.update(combos_tmp)

    for k, v in combos.items():
        c_d[k[0]] += v
    print(f"Part two: {max(c_d.values())}, {min(c_d.values())}, {max(c_d.values()) - min(c_d.values())}")
    #3288891573057 correct
day_14_2()