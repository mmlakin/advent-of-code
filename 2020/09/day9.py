#!/usr/bin/env python3

PREAMBLE_LENGTH = 25

with open("input.txt", "rt") as f:
    xmas_number_list = list(map(int, f.read().splitlines()))


class XMASNumber:
    def __init__(self, number, number_list):
        self.number = number
        self.number_list = number_list

    @property
    def valid(self):
        for s in self.sums():
            if s == self.number:
                return True
        return False

    def sums(self):
        for num1 in range(len(self.number_list)):
            for num2 in range(num1 + 1, len(self.number_list)):
                yield self.number_list[num1] + self.number_list[num2]


def find_weakness(invalid_num):
    for x in range(len(xmas_number_list)):
        contiguous_set = [xmas_number_list[x]]
        for y in range(x + 1, len(xmas_number_list)):
            contiguous_set.append(xmas_number_list[y])
            if sum(contiguous_set) == invalid_num:
                return min(contiguous_set) + max(contiguous_set)
            elif sum(contiguous_set) > invalid_num:
                break


for index in range(PREAMBLE_LENGTH, len(xmas_number_list)):
    current_number = xmas_number_list[index]
    current_numlist = xmas_number_list[index - PREAMBLE_LENGTH : index]
    if not XMASNumber(current_number, current_numlist).valid:
        invalid_number = current_number
        encryption_weakness = find_weakness(current_number)

part1 = invalid_number
part2 = encryption_weakness

print(f"AoC 2020 Day 9")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
