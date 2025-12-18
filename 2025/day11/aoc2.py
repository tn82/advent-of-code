import os
#from collections import defaultdict
#import heapq
#import copy
#from functools import cache

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

data = dict()
for line in input():
    i, o = line.strip().split(':')
    data[i] = set(o.split())
data['out'] = []

def countWaysToReach(end):
    counts = dict()
    newCounts = { node: (1 if node == end else 0) for node in data }

    while newCounts != counts:
        counts = newCounts
        newCounts = {
            node: (1 if node == end
                   else sum(counts[child] for child in data[node]))
            for node in counts
        }

    return newCounts

print(countWaysToReach('fft')['svr'])
print(1, countWaysToReach('dac')['fft'])
print(countWaysToReach('out')['dac'])

print(  countWaysToReach('fft')['svr']
      * countWaysToReach('dac')['fft']
      * countWaysToReach('out')['dac']
      + countWaysToReach('dac')['svr']
      * countWaysToReach('fft')['dac']
      * countWaysToReach('out')['fft'])