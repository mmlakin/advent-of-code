with open("input", "rt") as fh:
    game_input = [line.strip() for line in fh.readlines()]

bag_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

possible_games = 0
for game in game_input:
    impossible = False
    game_id, game_info = game.split(":")
    _, game_num = game_id.split(" ")
    game_sets = game_info.split(";")
    for game_set in game_sets:
        game_cubes_total = {}
        set_cubes = game_set.split(",")
        for cubes in set_cubes:
            count, color = cubes.strip().split()
            if game_cubes_total.get(color) is None:
                game_cubes_total[color] = int(count)
            else:
                game_cubes_total[color] += int(count)
        for cube_total in game_cubes_total.items():
            cube_total_color, cube_total_count = cube_total
            try:
                if game_cubes_total[cube_total_color] > bag_cubes[cube_total_color]:
                    impossible = True
                    print(f"game {game_num} - {cube_total}")
                    break
            except KeyError:
                pass
        if impossible == True:
            break
    if impossible == False:
        possible_games += int(game_num)
        print(f"POSSIBLE: {game_num}")

# sum_of_ids = sum(map(int, possible_games))
print(possible_games)
# print(f"part 1: {sum_of_ids}")
