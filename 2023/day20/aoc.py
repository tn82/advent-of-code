import os
from collections import defaultdict
import math

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def parse():
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
    return config, flip_flop, conjunctions
    
def part_one():
    config, flip_flop, conjunctions = parse()
    low_pulses = 0
    high_pulses = 0
    for _ in range(1000):
        __, dests = config["broadcaster"]
        low_pulses += 1
        q = []
        for d in dests:
            q.append((d, "broadcaster", "low"))
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

    print("Part 1: ", low_pulses * high_pulses)
    assert(low_pulses * high_pulses == 839775244)


def part_two():
    config, flip_flop, conjunctions = parse()
    lcm_values = []
    for ii in range(5000):
        _, dests = config["broadcaster"]

        q = []
        for d in dests:
            q.append((d, "broadcaster", "low"))
        while q:
            dest, source, sig = q.pop(0)
            if dest in ("output", "rx"):
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
                if not all_high and dest in ("vd", "ns", "bh", "dl"):
                    # zh => low => rx 
                    # if "vd", "ns", "bh", "dl" => high to zh (i.e. not all_high)
                    lcm_values.append(ii + 1)
                for d in dests:
                    q.append((d, dest, "low" if all_high else "high"))

    print("Part 2:", math.lcm(*lcm_values))
    assert(math.lcm(*lcm_values) == 207787533680413)

part_one()
part_two()
