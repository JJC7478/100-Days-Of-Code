import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

coffee_machine = {
    "Water": 1000,
    "Milk" : 300,
    "Coffee": 500,
    "Money": 0

}

espresso = {
    "Water": 100,
    "Milk" : 25,
    "Coffee": 75,
    "Money": 3.50
}

cappuchino = {
    "Water": 100,
    "Milk" : 50,
    "Coffee": 45,
    "Money": 4.25
}

latte = {
    "Water": 100,
    "Milk": 75,
    "Coffee": 35,
    "Money": 5.00
}

coffee_strings = {
    "espresso": espresso,
    "cappuchino": cappuchino,
    "latte": latte
}

resources = ["Water", "Milk", "Coffee"]

def coffee_choice():
    """Returns the user's coffee choice, or a report of coffee machine resources
    with the 'report' argument."""

    coffee_choice = input("What would you like? (espresso/cappuchino/latte) ")
    if coffee_choice == "report":
        report()
    return coffee_choice

def report():
    """Prints coffee machine resources."""

    for key in coffee_machine:
        print(key, ":", coffee_machine[key])

def calculate_money():
    """Takes the user's money and calculates the total payment. Returns total user payment."""

    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    user_cash = quarters + dimes + nickels + pennies
    return user_cash

def transaction_check(coffee_pick):
    """Calculates user's payment for coffee based on their selection."""

    coffee_ref = coffee_strings[coffee_pick]
    coffee_price = coffee_ref["Money"]
    user_money = calculate_money()
    difference = user_money - coffee_price
    if user_money != coffee_price:
        if user_money < coffee_price:
            print("Sorry that's not enough money. Money refunded.")
            return 0
        elif user_money > coffee_price:
            print(f"Your change is {difference}.")
    

def resource_check(coffee_pick):
    """Checks for sufficient resources to make the user's coffee."""

    user_coffee = coffee_strings[coffee_pick]
    for resource in resources:
        if coffee_machine[resource] < user_coffee[resource]:
            print(f"Sorry, there is not enough {resource.lower()}.")
            return 0
        else:
            return user_coffee

def refill():
    """Resets coffee machine resources to default values."""

    refill = input("Would you like to refill the coffee machine? Type 'y' to refill and 'n' if not: ")
    if refill == 'y':
        for resource in coffee_machine:
            if resource == "Water":
                coffee_machine[resource] = 1000
            elif resource == "Milk":
                coffee_machine[resource] = 300
            elif resource == "Coffee":
                coffee_machine[resource] = 500
    else:
        return 0

def make_coffee():
    """Uses coffee machine to create user's choice of coffee and calculates
    costs."""
    coffee = coffee_choice()
    if coffee == "report":
        make_coffee()
    coffee_price = (coffee_strings[coffee])["Money"]
    print(f"A(n) {coffee} is {coffee_price}.")
    resources = resource_check(coffee)
    if resources == 0:
        refill()
        if refill == 0:
            return
        else:
            clearConsole()
            make_coffee()
    transaction = transaction_check(coffee)
    if transaction == 0:
        make_coffee()
    print(f"Enjoy your {coffee}!")
    more_coffee = input("Would you like to order more coffee? Type 'y' if yes or 'n' to exit: ")
    if more_coffee == "y":
        clearConsole()
        make_coffee()
    else:
        return

make_coffee()
leave_app = input("Press ENTER to exit")
