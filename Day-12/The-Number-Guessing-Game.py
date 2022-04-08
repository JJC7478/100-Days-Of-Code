import random


number_list = []
for n in range(1,101):
    number_list.append(n)

game_start = True
while game_start:
    def number_picker():

        """Picks a random number from 1-100"""

        chosen_number = random.choice(number_list)
        return chosen_number

    def choose_difficulty():
        """Chooses difficulty and returns starting lives"""

        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            lives = 10
            return lives
        elif difficulty == "hard":
            lives = 5
            return lives
    
    lives = choose_difficulty()

    def play_game():

        """Prompts user to chose a number from 1-100 until they guess it right or are out of lives"""
        
        global lives
        chosen_number = number_picker()
        playing_game = True
        while playing_game:
            print(f"You have {lives} attempts to guess the number.")
            guess = int(input("Make a guess: "))
            if guess != chosen_number:
                lives -= 1
                if lives == 0:
                    print(f"Out of attempts. The number was {chosen_number}.")
                    playing_game = False
                elif guess > chosen_number:
                    print("Too High.\nGuess again.")
                elif guess < chosen_number:
                    print("Too Low.\nGuess again.")
            else:
                print("You got it right!")
                playing_game = False
    
    play_game()

    play_again = input("Would you like to play again? Type 'y' if yes or 'n' to exit: ")
    if play_again == "n": 
        game_start = False

input("Press ENTER to exit")
        





        