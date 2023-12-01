#!/usr/bin/env python3

with open("input.txt", "rt") as f:
    aoc1 = f.read().splitlines()

aoc1 = list(map(int, aoc1))
part1 = set([x * y for x in aoc1 for y in aoc1 if x + y == 2020]).pop()
part2 = set(
    [x * y * z for x in aoc1 for y in aoc1 for z in aoc1 if x + y + z == 2020]
).pop()

print(f"AoC 2020 Day 1")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
