#!/usr/bin/env python3

with open("input.txt", "rt") as f:
    aoc3 = f.read().splitlines()

# remove first line, and set index to third row (2)
aoc3 = aoc3[1:]
# get width minus newline
width = len(aoc3[0].replace("\n", ""))
index = 3
trees = 0
for line in aoc3:
    if index >= width:
        index = index - width
    if line[index] == "#":
        trees += 1
    index += 3

part1 = trees

# Part 2:
with open("input.txt", "rt") as f:
    aoc3 = f.read().splitlines()
# set total to 1 so the first answer will set total (itself * 1)
total = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope in slopes:
    right, down = slope
    skip = down
    index = 0
    trees = 0
    first = True
    for line in aoc3:
        if first:
            first = False
        elif skip == down:
            index += right
            if index >= width:
                index = index - width
            if line[index] == "#":
                trees += 1
        skip -= 1
        if skip == 0:
            skip = down
    total *= trees

part2 = total

print(f"AoC 2020 Day 3")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
