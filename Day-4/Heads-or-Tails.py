import random	 
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

heads_tails = random.randint(0,1)
if heads_tails == 0:
    print("Tails")
else:
    print("Heads")