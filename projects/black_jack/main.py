import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def deal_card():
    """Returns random card from the deck"""
    return random.choice(cards)



def calculate_score(cards):
    """Take list of cards and calculate score from the list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose, opponent has  Black Jack"
    elif u_score == 0:
        return "Win with Black Jack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)

    user_hand = []
    computer_hand = []
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f"user cards: {user_hand}, user score: {user_score}")
        print(f"Computers first card {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type n tpe pass ")
            if user_should_deal == 'y':
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)


    print(f"Your final hand: {user_hand} your score: {user_score}")
    print(f"Computer final hand {computer_hand} and coputer score : {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a Black Jack game, type 'y' or 'n'") == 'y':
    print("\n"*20)
    play_game()