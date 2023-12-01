#!/usr/bin/env python3

print("AoC 2021 Day 3")

with open("input", "rt") as f:
    report = f.read().splitlines()

# Part 1
gamma = epsilon = ""

for considered_bits in zip(*report):
    zeroes = considered_bits.count("0")
    ones = considered_bits.count("1")
    most_common = max(zeroes, ones)
    if zeroes == most_common:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)

print(f"Part 1: {gamma * epsilon}")

# Part 2
def decode_report(report_data: list, criteria: str, bit=0) -> int:
    """Recursive function to decode a report based on certain criteria."""
    bit_columns = zip(*report_data)
    for _ in range(bit + 1):
        considered_bits = next(bit_columns)

    zeroes = considered_bits.count("0")
    ones = considered_bits.count("1")
    equal = zeroes == ones
    if not equal:
        most_common = max(zeroes, ones)
        least_common = min(zeroes, ones)

    if criteria == "most_common":
        if equal or ones == most_common:
            bit_match = "1"
        else:
            bit_match = "0"
    elif criteria == "least_common":
        if equal or zeroes == least_common:
            bit_match = "0"
        else:
            bit_match = "1"
    else:
        raise ValueError(f"'{criteria}' is not a valid criteria for decode_report()")

    filtered_report_data = [
        number for number in report_data if number[bit] == bit_match
    ]
    if len(filtered_report_data) == 1:
        rating_value = filtered_report_data[0]
        return int(rating_value, base=2)
    else:
        return decode_report(filtered_report_data, criteria, bit + 1)


oxygen = decode_report(report, "most_common")
co2 = decode_report(report, "least_common")

print(f"Part 2: {oxygen * co2}")
