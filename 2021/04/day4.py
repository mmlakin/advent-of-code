#!/usr/bin/env python3

print("AoC 2021 Day 4")

with open("input", "rt") as f:
    draw_numbers = f.readline().strip().split(",")
    _ = f.readline()
    card_input = f.read().splitlines()

# Part 1 & 2
class BingoCard:
    def __init__(self, card_numbers):
        self.card = [row.split() for row in card_numbers]
        self.bingo = False

    def mark(self, number):
        for row in self.card:
            try:
                row[row.index(number)] = "x"
            except ValueError:
                pass
        self.check_card()

    def check_card(self):
        for row in self.card:
            if row == ["x"] * 5:
                self.bingo = True
        for column in zip(*self.card):
            if column == ("x",) * 5:
                self.bingo = True

    @property
    def score(self):
        return sum([int(num) for row in self.card for num in row if num != "x"])


bingo_cards = list()
temp_card = list()
for row in card_input:
    if row != "":
        temp_card.append(row)
    else:
        bingo_cards.append(BingoCard(temp_card))
        temp_card = list()
bingo_cards.append(BingoCard(temp_card))

winning_cards = 0
for draw_number in draw_numbers:
    for bingo_card in bingo_cards:
        if bingo_card.bingo is False:
            bingo_card.mark(draw_number)
            if bingo_card.bingo is True:
                winning_cards += 1
                if winning_cards == 1:
                    winning_score = int(draw_number) * bingo_card.score
                elif winning_cards == (len(bingo_cards)):
                    losing_score = int(draw_number) * bingo_card.score

print(f"Part 1 - {winning_score}")
print(f"Part 1 - {losing_score}")
