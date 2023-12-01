#!/usr/bin/env python3

your_bag = "shiny gold"

with open("input.txt", "rt") as f:
    aoc7 = f.read().splitlines()

bag_ref = dict()
for line in aoc7:
    bag, contents = line.split(" bags contain ")
    if contents == "no other bags.":
        contents = []
    else:
        contents = [x.strip().split(" bag")[0] for x in contents.split(",")]
        contents = [":".join(x.split(" ", maxsplit=1)) for x in contents]
    bag_ref[bag] = contents


def check_bag(outside_bag, inside_bag):
    bag_contents = [x.split(":")[1] for x in bag_ref[outside_bag]]
    if inside_bag in bag_contents:
        return True
    else:
        for bag in bag_contents:
            results = check_bag(bag, inside_bag)
            if results:
                return results
    return False


def count_bags(bag):
    total = 1
    for item in bag_ref[bag]:
        num, bag_name = item.split(":")
        bags = int(num) * count_bags(bag_name)
        total += bags
    return total


total = len([bag for bag in bag_ref.keys() if check_bag(bag, your_bag)])
part1 = total
part2 = count_bags(your_bag) - 1

print(f"AoC 2020 Day 7")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
