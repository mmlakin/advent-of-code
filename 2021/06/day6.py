#!/usr/bin/env python3
from collections import Counter

print("AoC 2021 Day 6")

with open("input", "rt") as f:
    lanternfish_ages = [int(age) for age in f.read().split(",")]

# Parts 1 & 2
days = 256

fish = Counter(lanternfish_ages)

for day in range(days + 1):
    try:
        new_fish = fish.pop(-1)
        fish.update(Counter({6: new_fish, 8: new_fish}))
    except KeyError:
        pass
    fish = Counter({age - 1: count for age, count in fish.items()})
    if day == 80:
        print(f"Part 1: {sum(fish.values())}")

print(f"Part 2: {sum(fish.values())}")
