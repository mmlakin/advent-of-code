#!/usr/bin/env python3

import re

with open("input.txt", "rt") as f:
    aoc4 = f.read().splitlines()

passports = list()
passport = dict()
for line in aoc4:
    if line == "":
        passports.append(passport)
        passport = dict()
    else:
        for entry in line.split():
            passport.update([entry.split(":")])

if passport != dict():
    passports.append(passport)

required_fields = [
    sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]),
    sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]),
]
valid = [x for x in passports if sorted(x.keys()) in required_fields]
part1 = len(valid)
print(f"{len(valid)} valid passports.")


validated_passports = list()
for pp in valid:
    try:
        if 1920 <= int(pp["byr"]) <= 2002:
            if 2010 <= int(pp["iyr"]) <= 2020:
                if 2020 <= int(pp["eyr"]) <= 2030:
                    hgtx = pp["hgt"][:-2]
                    hgty = pp["hgt"][-2:]
                    if (hgty == "cm" and 150 <= int(hgtx) <= 193) or (
                        hgty == "in" and 59 <= int(hgtx) <= 76
                    ):
                        if re.match(r"^\#[0-9a-f]{6}$", pp["hcl"]):
                            if pp["ecl"] in [
                                "amb",
                                "blu",
                                "brn",
                                "gry",
                                "grn",
                                "hzl",
                                "oth",
                            ]:
                                if re.match(r"^[0-9]{9}$", pp["pid"]):
                                    validated_passports.append(pp)
    except Exception as ex:
        print(f"Exception: {ex}")

part2 = len(validated_passports)

print(f"AoC 2020 Day 4")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
