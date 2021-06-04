from os import system

clear = lambda: system('cls')
# clear()

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    """
    Adds two numbers 
    and returns the sum
    """
    return n1+n2


def sub(n1, n2):
    """
    Subtracts second number from 
    first number and returns the difference
    """
    return n1-n2


def mul(n1, n2):
    """
    Multiplies two numbers 
    and returns the product
    """
    return n1*n2


def div(n1, n2):
    """
    Divides first number by second number 
    and returns the quotient
    """
    return n1/n2

operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    
    choice = "y"
    while choice == "y":
        for operation in operations:
            print(operation)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        if operation in operations:
            result = operations[operation](first_number, second_number)
        else:
            print("Invalid operation chosen! Try again.")
            continue

        print(f"{first_number} {operation} {second_number} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ")
        first_number = result
    if choice == "n":
        clear()
        calculator()
    else:
        exit()


calculator()