import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
computer_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]


def add_to_17(arr):
    if sum(arr) < 17:
        arr.append(cards[random.randint(0, len(cards) - 1)])
        add_to_17(arr)

def compare_cards(player, computer):
    add_to_17(computer)
    print(f"Your final hand: {player}, final score: {sum(player)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
    if sum(computer) == sum(player):
        print("That's a draw!")
    elif sum(computer) > 21 and sum(player) <= 21:
        print("Opponent went over. You win.")
    elif sum(player) > 21 and sum(computer) <= 21:
        print("You went over. You lose.")
    elif sum(player) <= 21 and sum(computer) < 21 and sum(player) > sum(computer):
        print("You won!")
    elif sum(computer) <= 21 and sum(player) < 21 and sum(player_cards) < sum(computer):
        print("You lose!")

def check_went_over(player):  
    return True if sum(player) > 21 else False

def play():
    if check_went_over(player_cards) and not check_went_over(computer_cards):
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You went over. You lose.")
        return
    if check_went_over(computer_cards) and not check_went_over(player_cards):
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("Opponent went over. You won!")
        return
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    get_another = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_another == "n":
        compare_cards(player_cards, computer_cards)
    elif get_another == "y":
        player_cards.append(cards[random.randint(0, len(cards) - 1)])
        computer_cards.append(cards[random.randint(0, len(cards) - 1)])
        play()

# play()

flag = True
play_flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play_flag == "y":
    play()


