print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

name1_T = lowercase_name1.count('t')
name1_R = lowercase_name1.count('r')
name1_U = lowercase_name1.count('u')
name1_E = lowercase_name1.count('e')
name2_T = lowercase_name2.count('t')
name2_R = lowercase_name2.count('r')
name2_U = lowercase_name2.count('u')
name2_E = lowercase_name2.count('e')

name1_L = lowercase_name1.count('l')
name1_O = lowercase_name1.count('o')
name1_V = lowercase_name1.count('v')
name1_EE = lowercase_name1.count('e')
name2_L = lowercase_name2.count('l')
name2_O = lowercase_name2.count('o')
name2_V = lowercase_name2.count('v')
name2_EE = lowercase_name2.count('e')

name1_LOVE = name1_L + name1_O + name1_V + name1_EE
name2_LOVE = name2_L + name2_O + name2_V + name2_EE

name1_TRUE = name1_T + name1_R + name1_U + name1_E
name2_TRUE = name2_T + name2_R + name2_U + name2_E

TRUE = str(name1_TRUE + name2_TRUE)
LOVE = str(name2_LOVE + name1_LOVE)

TRUE_LOVE = TRUE + LOVE
TRUE_LOVE = int(TRUE_LOVE)

if TRUE_LOVE < 10 or TRUE_LOVE > 90:
    print(f"Your score is {TRUE_LOVE}, you go together like coke and mentos.")
elif TRUE_LOVE > 40 and TRUE_LOVE < 50:
    print(f"Your score is {TRUE_LOVE}, you are alright together.")
else:
    print(f"Your score is {TRUE_LOVE}.")