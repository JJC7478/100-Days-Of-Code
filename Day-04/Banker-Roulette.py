import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
winner = random.randint(0, num_items - 1)
winner_name = names[winner]
print(f"{winner_name} is going to buy the meal today!")