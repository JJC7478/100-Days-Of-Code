print("Welcome to the tip calculator")
bill = input("What was the total bill?")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
split = input("How many people to split the bill?")
num_bill = float(bill)
num_tip = float(tip)
num_split = float(split)

split_amount = round(((num_bill + (num_bill * (num_tip/100.0))) / num_split),2)

print(f"Each person should pay: ${split_amount}")