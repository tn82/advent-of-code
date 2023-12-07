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

def mapper(datas, i):
    m = []
    while True:
        if i + 1 > len(datas):
            return m, i
        if not datas[i]:
            return m, i

        if datas[i][0].isdigit():
            m.append(int_list(datas[i].split()))
            i = i + 1

def s_map(s, m):
    for r in m:
        if s >= r[1] and s < r[1] + r[2]:
            return s + r[0] - r[1]
    return s

def part_one():
    datas = input()
    seeds = []
    seeds_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_hum = []
    humidity_location = []

    for i in range(len(datas)):
        if datas[i].startswith("seeds:"):
            _, s = datas[i].split(":")
            seeds = int_list(s.split())
            i += 1
        if "seed-to-soil map:" in datas[i]:
            i += 1
            seeds_soil, i = mapper(datas, i)
        if "soil-to-fertilizer map:" in datas[i]:
            i += 1
            soil_fertilizer, i = mapper(datas, i)
        if "fertilizer-to-water map:" in datas[i]:
            i += 1
            fertilizer_water, i = mapper(datas, i)
        if "water-to-light map:" in datas[i]:
            i += 1
            water_light, i = mapper(datas, i)
        if "light-to-temperature map:" in datas[i]:
            i += 1
            light_temperature, i = mapper(datas, i)
        if "temperature-to-humidity map:" in datas[i]:
            i += 1
            temperature_hum, i = mapper(datas, i)
        if "humidity-to-location map:" in datas[i]:
            i += 1
            humidity_location, i = mapper(datas, i)

    low_ball = 10000000000000000000000
    for s in seeds:
        t = s_map(s, seeds_soil)
        t = s_map(t, soil_fertilizer)
        t = s_map(t, fertilizer_water)
        t = s_map(t, water_light)
        t = s_map(t, light_temperature)
        t = s_map(t, temperature_hum)
        t = s_map(t, humidity_location)
        if t < low_ball:
            low_ball = t
            print(low_ball)

    print("Part 1: ", low_ball)
    assert(low_ball == 111627841)


def part_two():
    datas = input()
    seeds = []
    seeds_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_hum = []
    humidity_location = []

    for i in range(len(datas)):
        if datas[i].startswith("seeds:"):
            _, s = datas[i].split(":")
            seeds = int_list(s.split())
            i += 1
        if "seed-to-soil map:" in datas[i]:
            i += 1
            seeds_soil, i = mapper(datas, i)
        if "soil-to-fertilizer map:" in datas[i]:
            i += 1
            soil_fertilizer, i = mapper(datas, i)
        if "fertilizer-to-water map:" in datas[i]:
            i += 1
            fertilizer_water, i = mapper(datas, i)
        if "water-to-light map:" in datas[i]:
            i += 1
            water_light, i = mapper(datas, i)
        if "light-to-temperature map:" in datas[i]:
            i += 1
            light_temperature, i = mapper(datas, i)
        if "temperature-to-humidity map:" in datas[i]:
            i += 1
            temperature_hum, i = mapper(datas, i)
        if "humidity-to-location map:" in datas[i]:
            i += 1
            humidity_location, i = mapper(datas, i)

    low_ball = 10000000000000000000000
    for i in range(int(len(seeds)/2)):
        j = seeds[i*2]
        prev = 0
        steps = 1
        local_steps = 0
        while j < seeds[i*2] + seeds[i*2 + 1] + 1:
            t = s_map(j, seeds_soil)
            t = s_map(t, soil_fertilizer)
            t = s_map(t, fertilizer_water)
            t = s_map(t, water_light)
            t = s_map(t, light_temperature)
            t = s_map(t, temperature_hum)
            t = s_map(t, humidity_location)
            local_steps += 1
            if t < low_ball:
                low_ball = t
                print(low_ball)
            if t - prev == steps and local_steps > 5001 and steps == 1:
                steps = 5000
                local_steps = 0
            elif t - prev != steps and steps != 1:
                j -= (steps + 10)
                steps = 1
                local_steps = 0
            j += steps
            if steps != 1 and j >= seeds[i*2] + seeds[i*2 + 1]+1:
                j -= (steps + 10)
                steps = 1
                local_steps = 0
            prev = t
        
    print("Part 2: ", low_ball)
    assert(low_ball == 69323688)

part_one()
part_two()
