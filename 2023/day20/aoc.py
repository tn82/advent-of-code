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
    config = {}
    flip_flop = {}
    for i, line in enumerate(input()):
        source, dests = line.split("->")
        source = source.strip()
        if source == "broadcaster":
            stype = "broadcaster"
            sname = "broadcaster"
        else:
            stype = source[0]
            sname = source[1:]
        dests_ = dests.split(",")
        dests = []
        for d in dests_:
            dests.append(d.strip())
        config[sname] = (stype, dests)
        if stype == "%":
            flip_flop[sname] = 0

    # init conjunctions
    conjunctions = defaultdict(dict)
    for sname, type_dest in config.items():
        stype, dests = type_dest
        for dest in dests:
            if dest == "output":
                continue
            if dest not in config:
                continue
            dest_type, dest_dests = config[dest]
            if dest_type == "&":
                conjunctions[dest][sname] = "low"


    low_pulses = 0
    high_pulses = 0
    done = False
    #while not done:
    for ii in range(1000):
        #lows, highs, done = send_sig(config, flip_flop, sname, "low")
        #low_pulses += lows
        #high_pulses += highs

        _, dests = config["broadcaster"]
        low_pulses += 1
        q = []
        for d in dests:
            q.append((d, "broadcaster", "low"))
            #low_pulses += 1
        while q:
            dest, source, sig = q.pop(0)
            if sig == "low":
                low_pulses += 1
            else:
                high_pulses += 1
            if dest == "output":
                continue
            if dest not in config:
                continue
            stype, dests = config[dest]
            if stype == "%" and sig == "low":
                if flip_flop[dest] == 0:
                    for d in dests:
                        q.append((d, dest, "high"))
                    flip_flop[dest] = 1
                elif flip_flop[dest] == 1:
                    for d in dests:
                        q.append((d, dest, "low"))
                    flip_flop[dest] = 0
            if stype == "&":
                conjunctions[dest][source] = sig
                all_high = True
                for k, v in conjunctions[dest].items():
                    if v == "low":
                        all_high = False
                        break
                for d in dests:
                    q.append((d, dest, "low" if all_high else "high"))
                #if source in conjunctions:
                #    conjunctions[source] = sig
                #    for d in dests:
                #        q.append((d, dest, "high"))
        
        '''
        done = True
        for sname, v in flip_flop.items():
            if v == 1:
                done = False
                break
        for _, cv in conjunctions.items():
            for __, v in conjunctions.items():
                if v == "high":
                    done = False
                    break
                    '''




    print("Part 1: ", low_pulses * high_pulses)
    assert(low_pulses * high_pulses == 839775244)


def part_two():
    config = {}
    flip_flop = {}
    for i, line in enumerate(input()):
        source, dests = line.split("->")
        source = source.strip()
        if source == "broadcaster":
            stype = "broadcaster"
            sname = "broadcaster"
        else:
            stype = source[0]
            sname = source[1:]
        dests_ = dests.split(",")
        dests = []
        for d in dests_:
            dests.append(d.strip())
        config[sname] = (stype, dests)
        if stype == "%":
            flip_flop[sname] = 0

    # init conjunctions
    conjunctions = defaultdict(dict)
    for sname, type_dest in config.items():
        stype, dests = type_dest
        for dest in dests:
            if dest == "output":
                continue
            if dest not in config:
                continue
            dest_type, dest_dests = config[dest]
            if dest_type == "&":
                conjunctions[dest][sname] = "low"


    low_pulses = 0
    high_pulses = 0
    done = False
    #while not done:
    for ii in range(2):
        low_rx = 0
        high_rx = 0

        _, dests = config["broadcaster"]
        low_pulses += 1
        q = []
        for d in dests:
            q.append((d, "broadcaster", "low"))
            #low_pulses += 1
        while q:
            dest, source, sig = q.pop(0)
            if sig == "low":
                low_pulses += 1
            else:
                high_pulses += 1
            if dest == "output":
                continue
            if dest == "rx":
                if sig == "low":
                    low_rx += 1
                else:
                    high_rx += 1
                continue
            if dest == "zh":
                ister = 0
            if dest in ("dj", "nx", "zp", "bz"):
                ister = 0
            stype, dests = config[dest]
            if stype == "%" and sig == "low":
                if flip_flop[dest] == 0:
                    for d in dests:
                        q.append((d, dest, "high"))
                    flip_flop[dest] = 1
                elif flip_flop[dest] == 1:
                    for d in dests:
                        q.append((d, dest, "low"))
                    flip_flop[dest] = 0
            if stype == "&":
                conjunctions[dest][source] = sig
                all_high = True
                for k, v in conjunctions[dest].items():
                    if v == "low":
                        all_high = False
                        break
                if not all_high and dest in ("vd", "ns", "bh", "dl"):
                    ister = 0
                for d in dests:
                    q.append((d, dest, "low" if all_high else "high"))
        if low_rx == 1 and high_rx == 0:
            print("Part 2:", ii + 1)
            exit(0)
        if ii % 1e6 == 0:
            print("Iteration: ", ii)
        if low_rx:
            print("low_rx, high_rx:", ii + 1, low_rx, high_rx)
        for k, v in conjunctions["zh"].items():
            if v == "high":
                print("zh high", k, ii + 1)
        filt = {k: v for k, v in config.items() if "zh" in v[1]}
        for name, dd in filt.items():
            continue
            all_low = True
            cc = conjunctions[name]
            for k, v in cc.items():
                if v != "low":
                    all_low = False
                    break
            if all_low:
                print(name, conjunctions[name], ii + 1)
        for name in ("dj", "nx", "zp", "bz"):
        #for name in ("vd", "ns", "bh", "dl"):
            continue
            all_high = True
            cc = conjunctions[name]
            for k, v in cc.items():
                if v == "low":
                    all_high = False
                    break
            if all_high:
                print("all_high", name, conjunctions[name], ii + 1)
            else:
                print("not_all_high", name, conjunctions[name], ii + 1)
            all_low = True
            for k, v in cc.items():
                if v != "low":
                    all_low = False
                    break

import math
print(math.lcm(3761, 3767, 3779,3881))  # 207787533680413 
#part_one()
part_two()
