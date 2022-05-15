#Password Generator Project
from random import randint, choice, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)

random_letters = [choice(letters) for letter in range(nr_letters)]
random_symbols = [choice(symbols) for symbol in range(nr_symbols)]
random_numbers = [choice(numbers) for number in range(nr_numbers)]

char_list = [random_letters, random_symbols, random_numbers]
char_list = [char for sublist in char_list for char in sublist]

shuffle(char_list)

password = "".join(char_list)

print(f"Your password is: {password}")