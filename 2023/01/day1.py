with open("input", "rt") as fh:
    doc = [line.strip() for line in fh.readlines()]

# Part 1
calibration_values = []

for line in doc:
    for character in line:
        if character.isdigit():
            p1_first_digit = character
            break
    for rev_character in reversed(line):
        if rev_character.isdigit():
            p1_last_digit = rev_character
            break

    calibration_values.append(int(p1_first_digit + p1_last_digit))

sum_values = sum(calibration_values)
print(f"part 1: {sum_values}")

# Part 2
number_names = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

number_digits = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

all_numbers = number_names + number_digits


def num2digit(number: str):
    if number.isdigit():
        return number
    else:
        # look up number digit using name index
        return number_digits[number_names.index(number)]


p2_calibration_values = []

for p2_line in doc:
    # create list of numbers found and their indexes
    number_index_map = []

    for number in all_numbers:
        # find lowest number index using find
        lowest_number = p2_line.find(number)
        if lowest_number != -1:
            number_index_map.append((number, lowest_number))
        # find highest number index using rfind
        highest_number = p2_line.rfind(number)
        if highest_number != -1:
            number_index_map.append((number, highest_number))

    # sort map based on found number indexes
    sorted_map = sorted(number_index_map, key=lambda l: l[1])

    # numbers found with lowest and highest indexes
    first_number_found = sorted_map[0][0]
    last_number_found = sorted_map[-1][0]

    # convert numbers to digits
    p2_first_digit = num2digit(first_number_found)
    p2_last_digit = num2digit(last_number_found)

    # concat digits for new value
    new_value = p2_first_digit + p2_last_digit

    # convert to int and add to list
    p2_calibration_values.append(int(new_value))

# sum all values
new_sum_values = sum(p2_calibration_values)
print(f"part 2: {new_sum_values}")

# Initial solve using ugly and hard to read code
#
# number_locations_low = [loc for loc in map(p2_line.find, all_numbers)]
# number_locations_high = [loc for loc in map(p2_line.rfind, all_numbers)]
# found_numbers_map_low = [
#     num_loc
#     for num_loc in zip(all_numbers, number_locations_low)
#     if num_loc[1] != -1
# ]
# found_numbers_map_high = [
#     num_loc
#     for num_loc in zip(all_numbers, number_locations_high)
#     if num_loc[1] != -1
# ]
# sorted_map_low = sorted(found_numbers_map_low, key=lambda l: l[1])
# sorted_map_high = sorted(found_numbers_map_high, key=lambda l: l[1])
# new_first_digit = num2digit(sorted_map_low[0][0])
# new_last_digit = num2digit(sorted_map_high[-1][0])
# new_value = new_first_digit + new_last_digit
#
# p2_calibration_values.append(int(new_value))
# new_sum_values = sum(p2_calibration_values)

# print(f"part 2: {new_sum_values}")
