def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]

from dataclasses import dataclass
import re

@dataclass
class BluePrint:
    ore_robo_ore: int
    clay_robo_ore: int
    obs_robo_ore: int
    obs_robo_clay: int
    geode_robo_ore: int
    geode_robo_obs: int

    def max_ore(self):
        return max(self.ore_robo_ore, self.clay_robo_ore, self.obs_robo_ore, self.geode_robo_ore)


@dataclass
class State:
    nbr_ore_robo = 1
    nbr_clay_robo = 0
    nbr_obs_robo = 0
    nbr_geode_robo = 0

    ore = 0
    clay = 0
    obs = 0
    geode = 0

    none_s = 0

    def __hash__(self):
        return hash((self.nbr_ore_robo, self.nbr_clay_robo, self.nbr_obs_robo, self.nbr_geode_robo, self.ore, self.clay, self.obs, self.geode))

    def update_time(self):
        self.ore += self.nbr_ore_robo
        self.clay += self.nbr_clay_robo
        self.obs += self.nbr_obs_robo
        self.geode += self.nbr_geode_robo

def s_copy(s, c):
    s.nbr_ore_robo = c.nbr_ore_robo
    s.nbr_clay_robo = c.nbr_clay_robo
    s.nbr_obs_robo = c.nbr_obs_robo
    s.nbr_geode_robo = c.nbr_geode_robo

    s.ore = c.ore
    s.clay = c.clay
    s.obs = c.obs
    s.geode = c.geode

    s.none_s = c.none_s

def miner(state, bp, time, best_state, c, time_lim):
    time = time + 1
    if time > time_lim:
        if best_state.geode < state.geode:
            s_copy(best_state, state)
        return
    if state in c and c[state] <= time:
        return
    c[state] = time

    potential_geode = state.geode
    for i in range(1, time_lim - time + 2):
        potential_geode += i + state.nbr_geode_robo - 1
    if potential_geode <= best_state.geode:
        if time < 20:
            print("potential_geode", time)
        return state

    builds = []
    if state.ore >= bp.geode_robo_ore and state.obs >= bp.geode_robo_obs:
        builds.append("geode")
    else:
        if state.ore >= bp.ore_robo_ore and state.nbr_ore_robo < bp.max_ore():
            builds.append("ore")
        if state.ore >= bp.clay_robo_ore and state.nbr_clay_robo < bp.obs_robo_clay:
            builds.append("clay")
        if state.ore >= bp.obs_robo_ore and state.clay >= bp.obs_robo_clay:
            builds.append("obs")
        if state.none_s < 4:
            builds.append("none")
    state.update_time()

    for build in builds:
        state_copy = State()
        s_copy(state_copy, state)
        if build == "ore":
            state_copy.nbr_ore_robo += 1
            state_copy.ore -= bp.ore_robo_ore
            state_copy.none_s = 0
        if build == "clay":
            state_copy.nbr_clay_robo += 1
            state_copy.ore -= bp.clay_robo_ore
            state_copy.none_s = 0
        if build == "obs":
            state_copy.nbr_obs_robo += 1
            state_copy.ore -= bp.obs_robo_ore
            state_copy.clay -= bp.obs_robo_clay
            state_copy.none_s = 0
        if build == "geode":
            state_copy.nbr_geode_robo += 1
            state_copy.ore -= bp.geode_robo_ore
            state_copy.obs -= bp.geode_robo_obs
            state_copy.none_s = 0
        if build == "none":
            state_copy.none_s += 1
        miner(state_copy, bp, time, best_state, c, time_lim)
    return


def part_one():
    blue_prints = []
    for line in input():
        digits = re.findall(r'\d+', line)
        blue_prints.append(BluePrint(int(digits[1]), int(digits[2]), int(digits[3]), int(digits[4]), int(digits[5]), int(digits[6])))

    ans = 0
    for i, bp in enumerate(blue_prints):
        c = {}
        state = State()
        best_state = State()
        miner(state, bp, 0, best_state, c, 24)
        print(i+1, best_state.geode)
        ans += (i + 1) * best_state.geode

    print("Part 1: ", ans)
    assert ans == 1599

    part_two = 1
    for bp in blue_prints[0:3]:
        c = {}
        state = State()
        best_state = State()
        miner(state, bp, 0, best_state, c, 32)
        print(best_state.geode)
        part_two *= best_state.geode
    print("Part 2: ", part_two) 
    assert part_two == 14112

part_one()
