with open("input", "rt") as fh:
    input_file = [line.strip() for line in fh.readlines()]

DEBUG = False

total_points = 0
total_scratchcards = 0
card_bonuses = {}

card_pile = input_file

for card in card_pile:
    # parse card, example: Card   1: winning_numbers|your_numbers
    card_id, card_number_lists = card.split(":")
    card_id = int(card_id.split(" ")[-1])
    winning_numbers, your_numbers = [
        number_list.strip() for number_list in card_number_lists.split("|")
    ]

    # use sets to not count multiple numbers twice
    winning_numbers = set(
        [number for number in winning_numbers.split(" ") if number.isdigit()]
    )
    your_numbers = set(
        [number for number in your_numbers.split(" ") if number.isdigit()]
    )

    # parse number sets to find matches
    matching_numbers = 0
    for winning_number in winning_numbers:
        if winning_number in your_numbers:
            if DEBUG:
                print(f"card {card_id} - {winning_number}")
            matching_numbers += 1

    # get this card's bonus cards, if any (default to 0)
    bonus_cards = card_bonuses.get(card_id, 0)

    # add this card and this card's bonus cards to total
    total_scratchcards += 1 + bonus_cards

    # if any numbers match, process score and card bonuses
    if matching_numbers > 0:
        # points double for each match, so just use powers of 2; e.g. 2^0 = 1
        points_exponent = matching_numbers - 1
        total_points += pow(2, points_exponent)

        # process card bonuses
        bonus_cards_counted = 0
        # run at least once, and again for each card bonus
        while bonus_cards_counted <= bonus_cards:
            if DEBUG:
                print(f"checking card {card_id}")

            # add bonuses to future cards based on number of matches
            for match_num in range(1, matching_numbers + 1):
                next_card = card_id + match_num
                # card bonus might not exist yet, so default to 0 before adding
                card_bonuses[next_card] = card_bonuses.get(next_card, 0) + 1
            bonus_cards_counted += 1

        if DEBUG:
            print(
                f"card: {card_id} matching_numbers: {matching_numbers} total: {total_points}, total_cards: {total_scratchcards}"
            )

print(f"part 1: {total_points}")
print(f"part 2: {total_scratchcards}")
