from art import logo
from art import vs
from game_data import data
import random
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def choose_A():
    choice_A = random.choice(data)
    return choice_A

def choose_B():
    choice_B = random.choice(data)
    return choice_B


def play_game():
    score = 0
    is_Playing = True

    while is_Playing:
        choice_A = choose_A()
        choice_B = choose_B()
        
        a_name = choice_A["name"]
        a_followers = choice_A["follower_count"]
        a_description = choice_A["description"]
        a_country = choice_A["country"]

        b_name = choice_B["name"]
        b_followers = choice_B["follower_count"]
        b_description = choice_B["description"]
        b_country = choice_B["country"]

        clearConsole()
        print(logo)
        print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")

        print(vs)
        print(f"Against B: {b_name}, a {b_description}, from {b_country}.")


        player_choice = input("Who has more followers? Type 'A' or 'B': ")
        if player_choice == "A":
            if a_followers > b_followers:
                score += 1
                print(f"You got it right! Your current score is {score}")
                input("Press ENTER to continue")
            else:
                print("Sorry, you got it wrong.")
                is_Playing = False
        elif player_choice == "B":
            if b_followers > a_followers:
                score += 1
                print(f"You got it right! Your current score is {score}")
                input("Press ENTER to continue")
            else:
                print("Sorry, you got it wrong.")
                is_Playing = False
    clearConsole()
    print(f"Your final score is {score}!")
    game_again = input("Would you like to play again? Type 'y' to continue or press ENTER to exit:")
    if game_again == "y":
        play_game()


play_game()