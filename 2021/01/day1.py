#!/usr/bin/env python3

print("AoC 2021 Day 1")

with open("input", "rt") as f:
    readings = [int(x) for x in f.read().splitlines()]

# Part 1
increases = 0
for reading in readings:
    try:
        if reading > last_reading:
            increases += 1
    except NameError:
        pass
    last_reading = reading

# Part 2
sum_increases = 0
window = 3
for index in range(len(readings) + 1):
    if index >= window:
        current_sum = sum(readings[(index - window) : index])
        try:
            if current_sum > previous_sum:
                sum_increases += 1
        except NameError:
            pass
        previous_sum = current_sum

print(f"Part 1: {increases}")
print(f"Part 2: {sum_increases}")
