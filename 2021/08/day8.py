#!/usr/bin/env python3

print("AoC 2021 Day 8")

with open("input", "rt") as f:
    signal_entries = [line.strip() for line in f.read().splitlines()]

# Part 1

only_output_values = [entry.split("|")[1] for entry in signal_entries]
easy_digits_in_output = sum(
    [
        1
        for line in only_output_values
        for word in line.split()
        if len(word) in (2, 3, 4, 7)
    ]
)

print(f"Part 1: {easy_digits_in_output}")

# Part 2

ZERO = "abcefg"
ONE = "cf"
TWO = "acdeg"
THREE = "acdfg"
FOUR = "bcdf"
FIVE = "abdfg"
SIX = "abdefg"
SEVEN = "acf"
EIGHT = "abcdefg"
NINE = "abcdfg"


class Signal:
    def __init__(self, entry):
        patterns, encoded_output = map(str.split, entry.split(" | "))
        self.decode_patterns(patterns)
        self.decode_output(encoded_output)

    def sort_string(self, unsorted_string):
        return "".join(sorted(unsorted_string))

    def decode_patterns(self, patterns):
        """Decode patterns based on the following deductive logic:
        1, 7, 4, and 8 have unique lengths (1: 2, 7: 3, 4: 4, 8: 7)
        a is the letter in 7 and not in 1
        b is the letter in 4, not in 1, and in all 6-length patterns
        c is the letter in 1, and not in all 6 length patterns
        d is the letter in 4, not in 1, that is not b
        0 is the 6 length pattern without d
        6 is the 6 length pattern without c
        9 is the 6 length pattern that is not 0 or 6
        e is the only letter in 8 not in 9
        f is the letter in 1 that is not c
        g is the last letter not identified (from 8)
        2, 3, 5 based on solved segments
        """
        patterns = list(map(self.sort_string, patterns))
        self.numbers = dict()
        self.segments = dict()
        # Length-based numbers
        five_length_patterns = list()
        six_length_patterns = list()
        for pattern in patterns:
            if len(pattern) == 2:
                self.numbers[1] = pattern
            elif len(pattern) == 3:
                self.numbers[7] = pattern
            elif len(pattern) == 4:
                self.numbers[4] = pattern
            elif len(pattern) == 5:
                five_length_patterns.append(pattern)
            elif len(pattern) == 6:
                six_length_patterns.append(pattern)
            elif len(pattern) == 7:
                self.numbers[8] = pattern
        # Segment a
        for letter in self.numbers[7]:
            if letter not in self.numbers[1]:
                self.segments["a"] = letter
        # Segment b
        for letter in self.numbers[4]:
            if letter not in self.numbers[1]:
                if all(map(lambda p: letter in p, six_length_patterns)):
                    self.segments["b"] = letter
        # Segment c
        for letter in self.numbers[1]:
            if not all(map(lambda p: letter in p, six_length_patterns)):
                self.segments["c"] = letter
        # Segment d
        for letter in self.numbers[4]:
            if letter not in self.numbers[1]:
                if letter != self.segments["b"]:
                    self.segments["d"] = letter
        # Number 0
        for pattern in six_length_patterns:
            if self.segments["d"] not in pattern:
                self.numbers[0] = pattern
        # Number 6
        for pattern in six_length_patterns:
            if self.segments["c"] not in pattern:
                self.numbers[6] = pattern
        # Number 9
        for pattern in six_length_patterns:
            if pattern not in [self.numbers[0], self.numbers[6]]:
                self.numbers[9] = pattern
        # Segment e
        for letter in self.numbers[8]:
            if letter not in self.numbers[9]:
                self.segments["e"] = letter
        # Segment f
        for letter in self.numbers[1]:
            if letter != self.segments["c"]:
                self.segments["f"] = letter
        # Segment g
        for letter in self.numbers[8]:
            if letter not in self.segments.values():
                self.segments["g"] = letter
        # Number 2
        self.numbers[2] = self.sort_string(map(lambda l: self.segments[l], TWO))
        # Number 3
        self.numbers[3] = self.sort_string(map(lambda l: self.segments[l], THREE))
        # Number 5
        self.numbers[5] = self.sort_string(map(lambda l: self.segments[l], FIVE))

    def decode_output(self, encoded_output):
        # Lookup map
        self.lookup = dict()
        for number, pattern in self.numbers.items():
            self.lookup[pattern] = number
        # Output signal
        decoded_output = ""
        for output_value in encoded_output:
            decoded_output += str(self.lookup[self.sort_string(output_value)])
        self.output = int(decoded_output)


total_output_values = sum(Signal(entry).output for entry in signal_entries)

print(f"Part 2: {total_output_values}")
