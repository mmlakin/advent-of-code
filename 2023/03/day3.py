from math import prod

with open("input", "rt") as fh:
    input_file = [line.strip() for line in fh.readlines()]


DEBUG = False


def is_symbol(c):
    if c == ".":
        return False
    if c.isdigit():
        return False
    return True


def get_part_numbers(above_line, middle_line, below_line):
    if DEBUG:
        print(above_line)
        print(middle_line)
        print(below_line)
    all_part_numbers = []
    all_gear_ratios = []
    # evaluate middle line for symbols to find part numbers
    if above_line is None:
        above_line = "." * len(middle_line)
    if below_line is None:
        below_line = "." * len(middle_line)
    above_list = [_ for _ in above_line]
    middle_list = [_ for _ in middle_line]
    below_list = [_ for _ in below_line]
    # parse above and below lists for part numbers
    for part_list in (above_list, middle_list, below_list):
        is_number = False
        number = ""
        number_indexes = []
        for index, character in enumerate(part_list):
            if character.isdigit():
                is_number = True
                number += character
                number_indexes.append(index)
            else:
                if is_number is True:
                    for number_index in number_indexes:
                        part_list[number_index] = number
                    is_number = False
                    number = ""
                    number_indexes = []
            if is_number is True:
                for number_index in number_indexes:
                    part_list[number_index] = number

    # parse middle_list for symbols
    for index, character in enumerate(middle_list):
        if is_symbol(character):
            if DEBUG:
                print(f"symbol: {character}")
            if character == "*":
                is_gear = True
            if index == 0:
                first_nearby = 0
            else:
                first_nearby = index - 1
            last_nearby = index + 2
            above_nearby_numbers = set(above_list[first_nearby:last_nearby])
            middle_nearby_numbers = set(middle_list[first_nearby:last_nearby])
            below_nearby_numbers = set(below_list[first_nearby:last_nearby])
            if DEBUG:
                print(above_nearby_numbers)
                print(middle_nearby_numbers)
                print(below_nearby_numbers)
            # The following addresses edge cases where the same number is seen
            #  twice by one symbol, but this doesn't actually appear in my input...
            if index != 0 and index != len(middle_list) - 1:
                for nearby_list in (above_list, middle_list, below_list):
                    if nearby_list[index - 1] == nearby_list[index + 1]:
                        if nearby_list[index - 1] != nearby_list[index]:
                            if nearby_list[index - 1] != "." and not is_symbol(
                                nearby_list[index - 1]
                            ):
                                all_part_numbers.extend(nearby_list[index - 1])
            surrounding_part_numbers = [
                part_num
                for part_num in (
                    above_nearby_numbers.union(
                        middle_nearby_numbers, below_nearby_numbers
                    )
                )
                if part_num.isdigit()
            ]
            all_part_numbers.extend(surrounding_part_numbers)
            if len(surrounding_part_numbers) == 2:
                all_gear_ratios.append(prod(map(int, surrounding_part_numbers)))
    return (all_part_numbers, all_gear_ratios)


part_numbers = []
gear_ratios = []
previous_line = None
last_line = None
this_line = None
for line in input_file:
    if this_line is None:
        this_line = line
        continue
    previous_line = last_line
    last_line = this_line
    this_line = line
    found_part_numbers, found_gear_ratios = get_part_numbers(
        previous_line, last_line, this_line
    )
    if found_part_numbers:
        part_numbers.extend(found_part_numbers)
        if DEBUG:
            print(f"added part numbers {found_part_numbers}")
    if found_gear_ratios:
        gear_ratios.extend(found_gear_ratios)
# run for last line
found_part_numbers, found_gear_ratios = get_part_numbers(last_line, this_line, None)
if found_part_numbers:
    part_numbers.extend(found_part_numbers)
    if DEBUG:
        print(f"added part numbers {found_part_numbers}")
if found_gear_ratios:
    gear_ratios.extend(found_gear_ratios)

sum_part_numbers = sum(map(int, part_numbers))
sum_gear_ratios = sum(map(int, gear_ratios))
print(f"part 1: {sum_part_numbers}")
print(f"part 1: {sum_gear_ratios}")
