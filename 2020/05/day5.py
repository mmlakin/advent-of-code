#!/usr/bin/env python3

with open("input.txt", "rt") as f:
    aoc5 = f.read().splitlines()

seats = []
for line in aoc5:
    row = line[:7]
    column = line[7:10]
    rowx = range(128)
    columnx = range(8)
    for i in row:
        rowy = int(len(rowx) / 2)
        if i == "F":
            rowx = range(rowx.start, rowx.start + rowy)
        elif i == "B":
            rowx = range(rowx.stop - rowy, rowx.stop)
    rowid = rowx.start
    for i in column:
        columny = int(len(columnx) / 2)
        if i == "L":
            columnx = range(columnx.start, columnx.start + columny)
        elif i == "R":
            columnx = range(columnx.stop - columny, columnx.stop)
    columnid = columnx.start
    seatid = rowid * 8 + columnid
    seats.append(seatid)

part1 = max(seats)

missing_seatid = [x for x in range(min(seats), max(seats)) if x not in seats][0]
part2 = missing_seatid

print(f"AoC 2020 Day 5")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
