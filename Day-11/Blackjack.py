from art import logo
import random
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def add(n1, n2):
    return n1 + n2

def blackjack():
    game_start = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print(logo)
    while game_start:

        player_cards = []
        first_player_card = random.choice(cards)
        player_cards.append(first_player_card)
        second_player_card = random.choice(cards)
        player_cards.append(second_player_card)
        player_score = add(first_player_card, second_player_card)
        print(f"Your cards: {player_cards}, current score: {player_score}")



        cpu_cards = []
        first_cpu_card = random.choice(cards)
        cpu_cards.append(first_cpu_card)
        second_cpu_card = random.choice(cards)
        cpu_cards.append(second_cpu_card)
        cpu_score = add(first_cpu_card, second_cpu_card)
        print(f"First CPU card: {first_cpu_card}")

        if player_score < 21:
            in_play = True
        while in_play == True:
            hit_stay = input("Add another card? Type 'y' to hit and 'n' to stay: ")
            if hit_stay == "y":
                first_player_card = player_score
                new_player_card = random.choice(cards)
                player_cards.append(new_player_card)
                player_score = add(first_player_card, new_player_card)
                if cpu_score > 22:
                    for card in range(len(cpu_cards)):
                        if cpu_cards[card] == 11:
                            cpu_cards[card] = 1
                if player_score > 21 or player_score == 21:
                    in_play = False
                else:
                    print(f"Your cards: {player_cards}, current score: {player_score}")
            else:
                in_play = False
        
        while cpu_score < 17 and player_score != 21:
            first_cpu_card = cpu_score
            new_cpu_card = random.choice(cards)
            cpu_cards.append(new_cpu_card)
            cpu_score = add(first_cpu_card, new_cpu_card)
            if cpu_score > 22:
                for card in range(len(cpu_cards)):
                    if cpu_cards[card] == 11:
                        cpu_cards[card] = 1

        if cpu_score == 21:
            print(f"You Lose. CPU Blackjack.")
        elif player_score == 21:
            print(f"You Win! Player Blackjack!")
        elif player_score > 21:
            print("Player Bust. You Lose.")
        elif cpu_score > 21:
            print("CPU Bust! You Win!")
        elif player_score > cpu_score:
            print(f"You Win!")
        elif cpu_score > player_score:
            print(f"You Lose.")
        elif player_score == cpu_score:
            print("Draw.")

        print(f"Your cards: {player_cards}, final score: {player_score}")
        print(f"CPU cards: {cpu_cards}, cpu score: {cpu_score}")
        replay = input("Would you like to play again? Type 'y' to play again or 'n' to exit: ")
        if replay == 'y':
            game_start = False
            clearConsole()
            blackjack()
        else:
            game_start = False


player_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if player_start == "y":
    blackjack()
else:
    exit_bj = input("Press ENTER to exit")

exit_bj1 = input("Press ENTER to exit")