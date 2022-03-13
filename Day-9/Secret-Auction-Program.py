from art import logo
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

are_Bidders = True
print(logo)
print("Welcome to the secret auction program.")


while are_Bidders:
    bidders = []
    bidder_name = input("What is your name?: ")
    bidder_amt =  input("What's your bid?: ")

    def add_new_bidder(user_name, bid):
        new_bidder = {}
        new_bidder["Name"] = bidder_name
        new_bidder["Bid"] = float(bidder_amt)
        bidders.append(new_bidder)
    
    add_new_bidder(bidder_name, bidder_amt)
    response = input("Are there any other bidders? Type 'yes' or 'no'. ")
    clearConsole()
    if response == "no":
        are_Bidders = False

clearConsole()
bid_initial = 0
for people in bidders:
    if (people["Bid"]) > bid_initial:
        max_bid = people["Bid"]
        bid_initial = max_bid
        winner = people["Name"]

print(f"The winnner is {winner} with a bid of ${max_bid}.")
input("Press 'Enter' to exit.")
