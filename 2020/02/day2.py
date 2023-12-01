#!/usr/bin/env python3

with open("input.txt", "rt") as f:
    aoc2 = f.read().splitlines()

valid = 0
for item in aoc2:
    pol, pw = item.split(":")
    pw = pw.lstrip()
    polnum, polletter = pol.split()
    polnum1, polnum2 = map(int, polnum.split("-"))
    if polnum1 <= pw.count(polletter) <= polnum2:
        valid += 1

part1 = valid

# Part 2:
valid = 0
for item in aoc2:
    pol, pw = item.split(":")
    pw = pw.lstrip()
    polnum, polletter = pol.split()
    polnum1, polnum2 = map(int, polnum.split("-"))
    polnum1 -= 1
    polnum2 -= 1
    match1 = pw[polnum1] == polletter
    match2 = pw[polnum2] == polletter
    if match1 and not match2:
        valid += 1
    elif match2 and not match1:
        valid += 1

part2 = valid

print(f"AoC 2020 Day 2")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
