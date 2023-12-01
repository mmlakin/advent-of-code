#!/usr/bin/env python3

print("AoC 2021 Day 2")

with open("input", "rt") as f:
    commands = f.read().splitlines()

# Parts 1 & 2
horizontal_position = 0
assumed_depth = 0
actual_depth = 0
aim = 0

for command in commands:
    direction, units = command.split(" ")
    units = int(units)
    if direction == "forward":
        horizontal_position += units
        actual_depth += aim * units
    elif direction == "down":
        assumed_depth += units
        aim += units
    elif direction == "up":
        assumed_depth -= units
        aim -= units

print(f"Part 1 - {horizontal_position * assumed_depth}")
print(f"Part 2 - {horizontal_position * actual_depth}")
