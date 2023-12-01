#!/usr/bin/env python3

with open("input.txt", "rt") as f:
    aoc6 = f.read().splitlines()

sums = list()
group = set()
for line in aoc6:
    if line == "":
        sums.append(len(group))
        group = set()
    else:
        for item in line:
            group.add(item)

if group != set():
    sums.append(len(group))

part1 = sum(sums)

# Part 2:
with open("input.txt", "rt") as f:
    aoc6 = f.read().splitlines()

sums = list()
group = list()
for line in aoc6:
    if line == "":
        common_items = list(group[0])
        for item in list(group[0]):
            for items in group:
                if item not in items:
                    common_items.remove(item)
                    break
        sums.append(len(common_items))
        group = list()
    else:
        line_items = set()
        for item in line:
            line_items.add(item)
        group.append(line_items)

if group != list():
    common_items = list(group[0])
    for item in list(group[0]):
        for items in group:
            if item not in items:
                common_items.remove(item)
                break
    sums.append(len(common_items))

part2 = sum(sums)

print(f"AoC 2020 Day 6")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
