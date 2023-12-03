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
    """get_part_number takes 3 lines of part numbers and symbols
    and checks the middle line for symbols and finds which part
    numbers are adjacent (including diagonally) in all lines, and
    also finds gear ratios by multiplying part numbers if exactly
    two are adjacent to a '*' symbol.
    """
    if DEBUG:
        print(above_line)
        print(middle_line)
        print(below_line)

    # create lists that will be filled and returned
    all_part_numbers = []
    all_gear_ratios = []

    # create dummy strings if above or below are missing
    if above_line is None:
        above_line = "." * len(middle_line)
    if below_line is None:
        below_line = "." * len(middle_line)

    # create lists of characters from each string
    above_list = [_ for _ in above_line]
    middle_list = [_ for _ in middle_line]
    below_list = [_ for _ in below_line]

    # parse all lists for part numbers
    for part_list in (above_list, middle_list, below_list):
        is_number = False
        number = ""
        number_indexes = []
        # check each character of the line
        for index, character in enumerate(part_list):
            if character.isdigit():
                # if digit, it's the start of a number; build up
                # the number string and add indexes of the number
                is_number = True
                number += character
                number_indexes.append(index)
            else:
                # no digit means the last number is complete; save it
                #  to each index of the original digits and reset vars
                if is_number is True:
                    for number_index in number_indexes:
                        part_list[number_index] = number
                    is_number = False
                    number = ""
                    number_indexes = []
            # end of the line also means the last number is complete
            if is_number is True:
                for number_index in number_indexes:
                    part_list[number_index] = number

    # parse middle_list for symbols
    for index, character in enumerate(middle_list):
        if is_symbol(character):
            is_gear = False
            if DEBUG:
                print(f"symbol: {character}")
            if character == "*":
                is_gear = True
            if index == 0:
                # if symbol is the first character, don't search "to the left"
                first_nearby = 0
            else:
                # if not, we need to search one to the left on each line
                first_nearby = index - 1
            # we need to search one to the right, but list slicing is exclusive so +2
            last_nearby = index + 2
            # use set because the symbol will see the same number multiple times
            # in the list if adjacent to more than one digit of the number in the line
            above_nearby_numbers = set(above_list[first_nearby:last_nearby])
            middle_nearby_numbers = set(middle_list[first_nearby:last_nearby])
            below_nearby_numbers = set(below_list[first_nearby:last_nearby])

            if DEBUG:
                print(above_nearby_numbers)
                print(middle_nearby_numbers)
                print(below_nearby_numbers)

            # The following ugly code is for when the symbol is adjacent to two
            # instances of the same number, e.g. 123*123 (or diagonally), but
            # my input did not actually include this, not sure if anyone's did!
            if index != 0 and index != len(middle_list) - 1:
                for nearby_list in (above_list, middle_list, below_list):
                    if nearby_list[index - 1] == nearby_list[index + 1]:
                        if nearby_list[index - 1] != nearby_list[index]:
                            if nearby_list[index - 1] != "." and not is_symbol(
                                nearby_list[index - 1]
                            ):
                                all_part_numbers.extend(nearby_list[index - 1])

            # get all surrounding part numbers
            surrounding_part_numbers = [
                part_num
                for part_num in (
                    # must use union beacuse you can't concat sets
                    above_nearby_numbers.union(
                        middle_nearby_numbers, below_nearby_numbers
                    )
                )
                # exclude '.' and symbols
                if part_num.isdigit()
            ]

            # add to return list
            all_part_numbers.extend(surrounding_part_numbers)

            # find gears
            if is_gear and len(surrounding_part_numbers) == 2:
                # cast strings to int and multiple for gear ratio
                new_gear_ratio = prod(map(int, surrounding_part_numbers))
                # add to return list
                all_gear_ratios.append(new_gear_ratio)

    # return part numbers and gear ratios found
    return (all_part_numbers, all_gear_ratios)


# totals to sum later for solutions
part_numbers = []
gear_ratios = []

previous_line = None
last_line = None
this_line = None

# parse lines in input
for line in input_file:
    if this_line is None:
        # first line
        this_line = line
        continue
    previous_line = last_line
    last_line = this_line
    this_line = line
    # send 3 lines to process last line's symbols
    found_part_numbers, found_gear_ratios = get_part_numbers(
        previous_line, last_line, this_line
    )
    if found_part_numbers:
        # add found part numbers to total
        part_numbers.extend(found_part_numbers)
        if DEBUG:
            print(f"added part numbers {found_part_numbers}")
    if found_gear_ratios:
        # add found gear ratios to total
        gear_ratios.extend(found_gear_ratios)

# run again to process the last lines
found_part_numbers, found_gear_ratios = get_part_numbers(last_line, this_line, None)
if found_part_numbers:
    # add found part numbers to total
    part_numbers.extend(found_part_numbers)
    if DEBUG:
        print(f"added part numbers {found_part_numbers}")
if found_gear_ratios:
    # add found gear ratios to total
    gear_ratios.extend(found_gear_ratios)

# sum totals and output solutions
sum_part_numbers = sum(map(int, part_numbers))
sum_gear_ratios = sum(map(int, gear_ratios))
print(f"part 1: {sum_part_numbers}")
print(f"part 1: {sum_gear_ratios}")
