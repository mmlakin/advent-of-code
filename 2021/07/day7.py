#!/usr/bin/env python3

print("AoC 2021 Day 7")

with open("input", "rt") as f:
    crab_positions = [int(position) for position in f.read().split(",")]

# Part 1
possible_positions = range(min(crab_positions), max(crab_positions))
basic_fuel_costs = [
    sum([abs(crab_position - possible_position) for crab_position in crab_positions])
    for possible_position in possible_positions
]
print(f"Part 1: {min(basic_fuel_costs)} ")

# Part 2
max_distance = max(crab_positions) - min(crab_positions) + 2
movement_costs = {distance: sum(range(distance)) for distance in range(max_distance)}
actual_fuel_costs = [
    sum(
        [
            movement_costs[abs(crab_position - possible_position) + 1]
            for crab_position in crab_positions
        ]
    )
    for possible_position in possible_positions
]
print(f"Part 2: {min(actual_fuel_costs)} ")
