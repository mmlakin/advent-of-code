#!/usr/bin/env python3

with open("input.txt", "rt") as f:
    aoc8 = f.read().splitlines()

accumulator = 0

line = 0
line_history = []

while 1:
    if line in line_history:
        break
    line_history.append(line)
    op, arg = aoc8[line].split()
    arg = int(arg)
    if op == "acc":
        accumulator += arg
        line += 1
    elif op == "nop":
        line += 1
    elif op == "jmp":
        line += arg

part1 = accumulator

# Part 2:
with open("input.txt", "rt") as f:
    original_program = f.read().splitlines()

current_program = original_program.copy()
accumulator, line = (0, 0)
next_mod_line = 0
line_history = []


def modify_program(program, next_mod_line):
    """ Swap the first jmp or nop in program, starting at next_mod_line """
    for line in range(next_mod_line, len(program)):
        op, arg = program[line].split()
        if op == "jmp" or op == "nop":
            if op == "jmp":
                op = "nop"
            elif op == "nop":
                op = "jmp"
            program[line] = " ".join([op, arg])
            return program, line + 1


while 1:
    if line == len(current_program):
        # termination!
        break
    elif line in line_history:
        # modify program and try again
        accumulator, line = (0, 0)
        line_history = []
        new_program = original_program.copy()
        current_program, next_mod_line = modify_program(new_program, next_mod_line)
    else:
        line_history.append(line)
        op, arg = current_program[line].split()
        arg = int(arg)
        if op == "acc":
            accumulator += arg
            line += 1
        elif op == "nop":
            line += 1
        elif op == "jmp":
            line += arg

part2 = accumulator

print(f"AoC 2020 Day 8")
print(f"Part 1 - {part1}")
print(f"Part 2 - {part2}")
