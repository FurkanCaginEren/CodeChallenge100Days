############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]


while True:
    player_cards = []
    table_cards = []
    player_hand = 0
    table_hand = 0

    for i in range(2):
        player_cards.append(random.choice(cards))
        table_cards.append(random.choice(cards))
        player_hand += player_cards[i]
        table_hand += table_cards[i]
    print(player_cards)
    print(table_cards[0])

    pick_card = input("wanna pick card Y/N ").lower()

    while pick_card == "y":
        i = 2
        player_cards.append(random.choice(cards))
        player_hand += player_cards[i]
        print(player_cards)
        i += 1
        if pick_card == "n" or player_hand > 21:
            break
        pick_card = input("wanna pick card Y/N ").lower()

    while table_hand < 17:
        i = 2
        table_cards.append(random.choice(cards))
        table_hand += table_cards[i]
        i += 1

    print(table_cards)
    print(f"Player hand total = {player_hand}")
    print(f"Table hand total = {table_hand}")

    if player_hand > 21 or table_hand > player_hand:
        print("Table wins")
    elif (table_hand > 21 and player_hand < 22) or player_hand > table_hand:
        print("Player wins")

    if input("Do U want to play another game Y/N").lower() == "n":
        break
