import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
computer_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]


def add_to_17(arr):
    if sum(arr) < 17:
        arr.append(cards[random.randint(0, len(cards) - 1)])
        add_to_17(arr)

def play():
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    get_another = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_another == "n":
        add_to_17(computer_cards)
          
    # print(player_cards, computer_cards)

# play()

# flag = True
# play_flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# while play_flag == "y":
#     pass


# print(random.randint(1,3))
