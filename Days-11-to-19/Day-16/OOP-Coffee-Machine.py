from click import option
import coffee_maker
import menu
import money_machine

coffee_menu = menu.Menu()

latte = menu.MenuItem(name = "latte", water= 100, milk= 60, coffee= 40, cost= 1.50)

espresso = menu.MenuItem(name = "espresso", water= 100, milk= 20, coffee= 80, cost= 1.25)

cappuchino = menu.MenuItem("cappuchino", 100, 50, 50, 1.50)

coffee_menu.menu = [latte, espresso, cappuchino]

coffee_strings = {
    "latte": latte,
    "cappuchino": cappuchino,
    "espresso": espresso
}



options = coffee_menu.get_items()

def find_drink(order_name):
    coffee_menu.find_drink(order_name)


coffee_machine = coffee_maker.CoffeeMaker()

def coffee_report():
    coffee_machine.report()

def resource_check(drink):
    coffee_machine.is_resource_sufficient(drink)

def make_coffee(order):
    coffee_machine.make_coffee(order)

cash_register = money_machine.MoneyMachine()

def cash_report():
    cash_register.report()
def make_payment(cost):
    cash_register.make_payment(cost)

def coffee_order():

    coffee = input(f"What would you like? {options}" )
    if coffee == "report":
        coffee_report()
        cash_report()
        coffee_order()
    elif coffee == "off":
        return
    else:
        coffee_choice = coffee_strings[coffee]
    
    resource_checking = resource_check(coffee_choice)
    if resource_checking == False:
        print("Sorry. Machine does not have enough resources")
    else:
        print(f"Making your {coffee}...")
    
    transaction = make_payment(coffee_choice.cost)
    if transaction == False:
        input("Money insufficient. Press ENTER to continue")
        coffee_order()
    else:
        order_again = input(f"Enjoy your {coffee}! Would you like to order again? Type 'y' if yes or 'n' to exit.")
        if order_again == "y":
            coffee_order()
        else:
            return

    
coffee_order()

    
