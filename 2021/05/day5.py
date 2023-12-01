#!/usr/bin/env python3

print("AoC 2021 Day 5")

with open("input", "rt") as f:
    vent_lines = [line.strip().split(" -> ") for line in f.readlines()]

# Part 1
part1_vent_diagram = dict()
vent_diagram = dict()

for vent_line in vent_lines:
    diagonal_line = False
    line_start, line_end = vent_line
    start_x, start_y = map(int, line_start.split(","))
    end_x, end_y = map(int, line_end.split(","))
    if start_x == end_x:
        # vertical line
        if start_y < end_y:
            line_points = [(start_x, p) for p in range(start_y, end_y + 1)]
        elif end_y < start_y:
            line_points = [(start_x, p) for p in range(end_y, start_y + 1)]
    elif start_y == end_y:
        # horizontal line
        if start_x < end_x:
            line_points = [(p, start_y) for p in range(start_x, end_x + 1)]
        elif end_x < start_x:
            line_points = [(p, start_y) for p in range(end_x, start_x + 1)]
    elif start_x < end_x:
        # diagonal line up
        diagonal_line = True
        if start_y < end_y:
            line_points = [
                ((start_x + i), (start_y + i)) for i in range((end_x - start_x) + 1)
            ]
        elif end_y < start_y:
            line_points = [
                ((start_x + i), (start_y - i)) for i in range((end_x - start_x) + 1)
            ]
    elif end_x < start_x:
        diagonal_line = True
        # diagonal line down
        if start_y < end_y:
            line_points = [
                ((start_x - i), (start_y + i)) for i in range((start_x - end_x) + 1)
            ]
        elif end_y < start_y:
            line_points = [
                ((start_x - i), (start_y - i)) for i in range((start_x - end_x) + 1)
            ]
    # print(f"line:{vent_line}, points:{line_points}")
    for point in line_points:
        if diagonal_line is False:
            try:
                part1_vent_diagram[point] += 1
            except KeyError:
                part1_vent_diagram[point] = 1
        try:
            vent_diagram[point] += 1
        except KeyError:
            vent_diagram[point] = 1

part1_overlapping_points = 0
for k, v in part1_vent_diagram.items():
    if v > 1:
        part1_overlapping_points += 1

overlapping_points = 0
for k, v in vent_diagram.items():
    if v > 1:
        overlapping_points += 1

print(f"Day 1: {part1_overlapping_points}")
print(f"Day 2: {overlapping_points}")
