import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list


chosen_word = random.choice(word_list)
display = []
print(logo)
for letter in chosen_word:
    display.append("_")
print(display)

lives = 6
chosen_word_list = list(chosen_word)
while display != chosen_word_list and lives != 0:
    guess = input("Please guess a letter that belongs to the word\n").lower()
    if guess in display:
        print("You have already used this letter. Please guess a different letter")
    for n in range(1, len(chosen_word_list) + 1):
        if guess == chosen_word_list[n-1]:
            display[n-1] = guess
    if guess not in chosen_word_list:
        lives -= 1
        print(f"Sorry, {guess} is not in the word.")
    print(stages[lives])
    print(display)
if lives > 0:
    print("You Win\n")
    input("Press any key to exit")
else:
    print(f"You Lose\n{display}\nThe word was: {chosen_word}")
    input("Press any key to exit")
