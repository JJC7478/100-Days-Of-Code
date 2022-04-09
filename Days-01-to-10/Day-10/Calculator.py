#Calculator

from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    for key in operations:
        print(key)

    operation_symbol = input("Pick an operation from the line above: ")

    is_Calculating = True
    while is_Calculating:

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        response = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'e' to stop calculating. ")
        if response == "y":
            num1 = answer
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))
        elif response == "n":
            is_Calculating = False
            calculator()
        else:
            is_Calculating = False

calculator()
exit_app = input("Press ENTER to exit.")