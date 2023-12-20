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

'''
    x: Extremely cool looking
    m: Musical (it makes a noise when you hit it)
    a: Aerodynamic
    s: Shiny
'''
def part_one():
    sums = 0
    flow = True
    rules = {}
    parts = []
    for i, line in enumerate(input()):
        if not line:
            flow = False
            continue
        if flow:
            name, rule = line.rstrip("}").split("{")
            rule = rule.split(",")
            rules[name] = rule
        else:
            part = line.lstrip("{").rstrip("}")
            p2 = {}
            for p in part.split(","):
                pn, pi = p.split("=")
                p2[pn] = int(pi)
            parts.append(p2)

    accepted = []
    rejected = []

    for part in parts:
        wfs = rules["in"]
        i = 0
        while True:
            wf = wfs[i]
            dest = ""
            if "<" in wf:
                tt, dest = wf.split(":")
                t, v = tt.split("<")
                if int(v) <= part[t]:
                    i += 1
                    continue # Next wf
            elif ">" in wf:
                tt, dest = wf.split(":")
                t, v = tt.split(">")
                if int(v) >= part[t]:
                    i += 1
                    continue # Next wf
            else:
                dest = wf
            if dest == "A":
                accepted.append(part)
                break
            if dest == "R":
                rejected.append(part)
                break
            wfs = rules[dest]
            i = 0

    for a in accepted:
        sums += sum(a.values())
    print("Part 1: ", sums)
    assert(sums == 263678)

import time
def part_two():
    sums = 0
    flow = True
    rules = {}
    parts = []

    for i, line in enumerate(test()):
        if not line:
            flow = False
            continue
        if flow:
            name, rule = line.rstrip("}").split("{")
            rulle = []
            for r in rule.split(","):
                if "<" in r:
                    tt, dest = r.split(":")
                    t, v = tt.split("<")
                    rulle.append((t, "<", int(v), dest))
                elif ">" in r:
                    tt, dest = r.split(":")
                    t, v = tt.split(">")
                    rulle.append((t, ">", int(v), dest))
                else:
                    rulle.append((r,))

            rules[name] = rulle
        else:
            part = line.lstrip("{").rstrip("}")
            p2 = {}
            for p in part.split(","):
                pn, pi = p.split("=")
                p2[pn] = int(pi)
            parts.append(p2)

    all_ranges = defaultdict(set)
    all_ranges["x"].add(1)
    all_ranges["x"].add(4000)
    all_ranges["m"].add(1)
    all_ranges["m"].add(4000)
    all_ranges["a"].add(1)
    all_ranges["a"].add(4000)
    all_ranges["s"].add(1)
    all_ranges["s"].add(4000)
    for k, r in rules.items():
        for wf in r:
            if "<" in wf:
                all_ranges[wf[0]].add(wf[2]) # rätt
                all_ranges[wf[0]].add(wf[2] + 1)
                all_ranges[wf[0]].add(wf[2] - 1) # rätt
            if ">" in wf:
                all_ranges[wf[0]].add(wf[2])
                all_ranges[wf[0]].add(wf[2] + 1) # rätt
                all_ranges[wf[0]].add(wf[2] - 1)

    sums = 0
    x_prev = 0
    prev = ""
    for x in sorted(all_ranges["x"]):
        seconds = time.time()
        m_prev = 0
        for m in sorted(all_ranges["m"]):
            a_prev = 0
            for a in sorted(all_ranges["a"]):
                s_prev = 0
                for s in sorted(all_ranges["s"]):
                    part = {"x": x, "m": m, "a": a, "s": s}
                    wfs = rules["in"]
                    i = 0
                    while True:
                        wf = wfs[i]
                        dest = ""
                        if "<" in wf:
                            dest = wf[3]
                            if wf[2] <= part[wf[0]]:
                                i += 1
                                continue # Next wf
                        elif ">" in wf:
                            dest = wf[3]
                            if wf[2] >= part[wf[0]]:
                                i += 1
                                continue # Next wf
                        else:
                            dest = wf[0]
                        if dest == "A":
                            if prev == "A":
                                sums += (x - x_prev) * (m - m_prev) * (a - a_prev) * (s - s_prev)
                            else:
                                iii = 1
                            prev = dest
                            break
                        if dest == "R":
                            if prev == "A":
                                sums += (x - x_prev) * (m - m_prev) * (a - a_prev) * (s - s_prev)
                            else:
                                iii = 1
                            prev = dest
                            break
                        wfs = rules[dest]
                        i = 0
                    s_prev = s
                a_prev = a
            m_prev = m
        print("Time per x:", time.time() - seconds)
        x_prev = x

    print("Part 2: ", sums + 1)
    #assert(sums ==)
    # 167409079868000

def rules():
    flow = True
    rules = {}
    for i, line in enumerate(input()):
        if not line:
            flow = False
            continue
        if flow:
            name, rule = line.rstrip("}").split("{")
            rulle = []
            for r in rule.split(","):
                if "<" in r:
                    tt, dest = r.split(":")
                    t, v = tt.split("<")
                    rulle.append((t, "<", int(v), dest))
                elif ">" in r:
                    tt, dest = r.split(":")
                    t, v = tt.split(">")
                    rulle.append((t, ">", int(v), dest))
                else:
                    rulle.append((r,))

            rules[name] = rulle
        else:
            continue
    return rules

def filter_test(comp, comp_val, vals):
    if comp == "<":
        return tuple([v for v in vals if v < comp_val])
    if comp == ">":
        return tuple([v for v in vals if v > comp_val])

def filter_neg_test(comp, comp_val, vals):
    if comp == "<":
        return tuple([v for v in vals if v >= comp_val])
    if comp == ">":
        return tuple([v for v in vals if v <= comp_val])

def count_recur(w_name, x, m, a, s, rules):
    if w_name == 'A':
        return len(x) * len(m) * len(a) * len(s)
    if w_name == 'R':
        return 0

    wfs = rules[w_name]

    c = 0
    for r in wfs:
        if len(r) == 4:
            dest = r[3]
            var = r[0]
            comp = r[1]
            comp_val = r[2]

            if var == 'x':
                filter_vars = filter_test(comp, comp_val, x)
                if filter_vars:
                    c += count_recur(dest, filter_vars, m, a, s, rules)
                x = filter_neg_test(comp, comp_val, x)
            elif var == 'm':
                filter_vars = filter_test(comp, comp_val, m)
                if filter_vars:
                    c += count_recur(dest, x, filter_vars, a, s, rules)
                m = filter_neg_test(comp, comp_val, m)
            elif var == 'a':
                filter_vars = filter_test(comp, comp_val, a)
                if filter_vars:
                    c += count_recur(dest, x, m, filter_vars, s, rules)
                a = filter_neg_test(comp, comp_val, a)
            elif var == 's':
                filter_vars = filter_test(comp, comp_val, s)
                if filter_vars:
                    c += count_recur(dest, x, m, a, filter_vars, rules)
                s = filter_neg_test(comp, comp_val, s)
        else:
            c += count_recur(r[0], x, m, a, s, rules)

    return c

def part_two2():
    sums = count_recur('in',
                        tuple(range(1, 4001)),
                        tuple(range(1, 4001)),
                        tuple(range(1, 4001)),
                        tuple(range(1, 4001)),
                        rules())
    print("Part 2:", sums)
    assert(sums == 125455345557345)

part_one()
part_two2()
