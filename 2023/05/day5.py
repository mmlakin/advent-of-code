import pdb

with open("testinput", "rt") as fh:
    testinput_file = [line.strip() for line in fh.readlines()]

with open("input", "rt") as fh:
    input_file = [line.strip() for line in fh.readlines()]

DEBUG = False
# DEBUG = True

almanac = input_file
# almanac = testinput_file


class gardening_map:
    def __init__(self, map_name: str, input_maps: list):
        # self.conversion_map = {}
        self.name = map_name
        self.conversion_maps = input_maps
        # lol this code works on testinput but pegs cpu on regular input
        # for input_map in input_maps:
        #     destination_range, source_range, range_length = map(
        #         int, input_map.split(" ")
        #     )
        #     for x in range(range_length):
        #         self.conversion_map[source_range + x] = destination_range + x

    def convert(self, input_number: int):
        # return self.conversion_map.get(input_number, input_number)
        for conversion_map in self.conversion_maps:
            destination_range, source_range, range_length = map(
                int, conversion_map.split(" ")
            )
            if input_number in range(source_range, source_range + range_length):
                number_difference = input_number - source_range
                return destination_range + number_difference
        return input_number

    def lowest_number(self):
        return min(
            [
                int(conversion_map.split(" ")[0])
                for conversion_map in self.conversion_maps
            ]
        )

    def unconvert(self, input_number: int):
        for conversion_map in self.conversion_maps:
            destination_range, source_range, range_length = map(
                int, conversion_map.split(" ")
            )
            if input_number in range(
                destination_range, destination_range + range_length
            ):
                number_difference = input_number - destination_range
                return source_range + number_difference
        return input_number


seeds_line = almanac[0]
_, *seeds = seeds_line.split(" ")
seeds = list(map(int, seeds))

almanac_maps = almanac[2:]
almanac_maps = [line for line in almanac_maps if line != ""]

maps = []
map_numbers = []

# read maps
for line in almanac_maps:
    if line[-1] == ":":
        if map_numbers != []:
            maps.append(gardening_map(map_name, map_numbers))
            map_numbers = []
        map_name = line[:-1]
    else:
        map_numbers.append(line)

# save last map
if map_numbers != []:
    maps.append(gardening_map(map_name, map_numbers))


end_values = []
for seed in seeds:
    if DEBUG:
        print(f"current seed: {seed}")
    current_number = None
    for current_map in maps:
        if current_number is None:
            current_number = seed
        current_number = current_map.convert(current_number)
        if DEBUG:
            print(f"  {current_map.name}: {current_number}")
    end_values.append(current_number)

print(f"part1: {min(end_values)}")

# PART 2
# look backwards?
lowest_number = maps[-1].lowest_number()

for low_number in range(lowest_number, 0, -1):
    current_number = low_number
    for current_map in reversed(maps[:-1]):
        current_number = current_map.unconvert(current_number)
    if current_number in seeds:
        lowest_number = low_number
        print(f"new lowest number: {lowest_number}")

print(f"part2: {lowest_number}")

# # works for testinput but pegs CPU on regular input
# part2_end_values = []
# seed_start = None
# for seed in seeds:
#     if seed_start is None:
#         seed_start = seed
#         continue
#     seed_range = seed
#     for current_seed in range(seed_start, seed_start + seed_range):
#         if DEBUG:
#             print(f"\ncurrent seed: {current_seed}")
#         current_number = None
#         for current_map in maps:
#             if current_number is None:
#                 current_number = current_seed
#             if DEBUG:
#                 print(current_map.name)
#                 print(f"converting {current_number}")
#             current_number = current_map.convert(current_number)
#         part2_end_values.append(current_number)
#     seed_start = None
#
#
# print(f"part2: {min(part2_end_values)}")
