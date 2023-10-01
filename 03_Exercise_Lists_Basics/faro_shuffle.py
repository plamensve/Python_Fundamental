deck_of_cards = input().split()
count_of_shuffles = int(input())


for shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]

    shuffling_deck = []

    for card_index in range(len(left_part)):
        shuffling_deck.append(left_part[card_index])
        shuffling_deck.append(right_part[card_index])

    deck_of_cards = shuffling_deck
print(deck_of_cards)
