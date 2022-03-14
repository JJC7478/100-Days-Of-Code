import random


rps = ["Rock", "Paper", "Scissors"]

action = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n")
player = rps[int(action)]
print(f"You chose: {player}")

cpu = rps[random.randint(0,2)]
print(f"Computer chose: {cpu}")

if player == "Rock" and cpu == "Scissors":
    print("You Win!\nPress any key to exit")
elif player == "Scissors" and cpu == "Paper":
    print("You Win!\nPress any key to exit")
elif player == "Paper" and cpu == "Rock":
    print("You Win!\nPress any key to exit")
elif player == cpu:
    print("Tie!\n Press any key to exit")
else:
    print("You Lose! Press any key to exit")
