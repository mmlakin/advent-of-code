#!/usr/bin/env python3
from itertools import chain

print("AoC 2021 Day 8")

with open("input", "rt") as f:
    floor_map = (line.strip() for line in f.readlines())

# Part 1
low_points = list()
previous_line = None
current_line = None
for line in chain(floor_map, [None]):
    if current_line is None:
        current_line = line
        continue
    next_line = line
    previous_number = 10
    current_number = None
    line_index = -2
    for number in chain(current_line, [10]):
        line_index += 1
        number = int(number)
        if current_number is None:
            current_number = number
            continue
        else:
            next_number = number
            if previous_number > current_number < next_number:
                try:
                    top_number = previous_line[line_index]
                except:
                    top_number = 10
                if int(top_number) > current_number:
                    try:
                        bottom_number = next_line[line_index]
                    except:
                        bottom_number = 10
                    if int(bottom_number) > current_number:
                        low_points.append(current_number)
            previous_number = current_number
            current_number = next_number
    previous_line = current_line
    current_line = next_line

risk_levels = sum(num + 1 for num in low_points)
print(f"Part 1: {risk_levels}")
