with open("input", "rt") as fh:
    input_file = [line.strip() for line in fh.readlines()]

DEBUG = False

total_points = 0
total_scratchcards = 0
card_bonuses = {}

for card in input_file:
    matching_numbers = 0
    total_scratchcards += 1
    card_num, card_numbers = card.split(":")
    card_num = int(card_num.split(" ")[-1])
    winning_numbers, your_numbers = [x.strip() for x in card_numbers.split("|")]
    winning_numbers = set([x for x in winning_numbers.split(" ") if x.isdigit()])
    your_numbers = set([x for x in your_numbers.split(" ") if x.isdigit()])
    for number in winning_numbers:
        if number in your_numbers:
            if DEBUG:
                print(f"card {card_num} - {number}")
            matching_numbers += 1
    card_bonus = card_bonuses.get(card_num, 0)
    total_scratchcards += card_bonus
    if matching_numbers > 0:
        total_points += pow(2, matching_numbers - 1)
        cards_counted = 0
        while cards_counted <= card_bonus:
            if DEBUG:
                print(f"checking card {card_num}")
            for match_num in range(1, matching_numbers + 1):
                next_card = card_num + match_num
                card_bonuses[next_card] = card_bonuses.get(next_card, 0) + 1
            cards_counted += 1
        if DEBUG:
            print(
                f"card: {card_num} matching_numbers: {matching_numbers} total: {total_points}, total_cards: {total_scratchcards}"
            )

print(f"part 1: {total_points}")
print(f"part 2: {total_scratchcards}")
