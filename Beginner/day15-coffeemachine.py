MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {
    "quarters": 0.25,
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10
}


def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def ask_payment():
    # quarters = int(input("How many quarters?"))
    total = 0
    print("Please insert coins")
    for coin in coins:
        number_of_coins = int(input(f"How many {coin}?: "))
        total = total + (coins[coin] * number_of_coins)
    return total


def check_ingredients(order):
    if order in MENU:
        recipe = MENU[order]['ingredients']
        for ingredient in recipe:
            if recipe[ingredient] > resources[ingredient]:
                print(f"Sorry there is not enought {ingredient}")
                return False
        return True


def make_coffee(order):
    if order in MENU:
        recipe = MENU[order]['ingredients']
        for ingredient in recipe:
            resources[ingredient] -= recipe[ingredient]
        
        resources["money"] += MENU[order]["cost"]
        

def coffee_machine():
    is_on = True
    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "report":
            show_report()
        elif order == "off":
            is_on = False
        else:
            if check_ingredients(order):
                bill = MENU[order]["cost"]
                recieved_payment = ask_payment()
                
                if bill > recieved_payment:
                    print("Sorry that's not enough money. Money refunded.")
                elif recieved_payment > bill:
                    print(f"Here is ${round(recieved_payment-bill,2)} in change.")
                    make_coffee(order)
                    print(f"Here is your {order} ☕ Enjoy!")
                else:
                    make_coffee(order)
                    print(f"Here is your {order} ☕ Enjoy!")


coffee_machine()