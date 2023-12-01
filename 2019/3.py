#!/usr/bin/env python3

"""
 aoc19 #3 Crossed Wires
"""

from collections import Counter


def find_coords(directions: str) -> list:
    coords = [(0, 0)]
    x = y = 0
    for direction in directions.split(","):
        nav = direction[0]
        num = int(direction[1:])
        for i in range(1, num + 1):
            if nav == "R":
                x += 1
            elif nav == "U":
                y += 1
            elif nav == "L":
                x -= 1
            elif nav == "D":
                y -= 1
            else:
                raise (f"{direction} - Unknown nav '{nav}', Quitting.")
            coords.append((x, y))
    return coords


def main():
    filename = "3input.txt"

    with open(filename, "rt") as f:
        coordslist = [find_coords(line) for line in f]

    wire1 = coordslist[0]
    wire2 = coordslist[1]
    wire1_uniques = list(Counter(wire1).keys())
    wire2_uniques = list(Counter(wire2).keys())
    allcoords = Counter(wire1_uniques + wire2_uniques)

    intersections = [x for x in allcoords if allcoords[x] == 2]

    closest = sorted(intersections, key=taxicab)[1]

    totalsteps = [(wire1.index(x) + wire2.index(x)) for x in intersections]
    fewest_steps = sorted(totalsteps)[1]
    print(f"closest coord: {closest}")
    print(f"distance: {taxicab(closest)}")
    print(f"fewest steps: {fewest_steps}")


def taxicab(coord):
    x, y = coord
    return abs(0 - x) + abs(0 - y)


if __name__ == "__main__":
    main()
