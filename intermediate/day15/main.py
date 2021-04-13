# Coffee Machine Project
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

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    for resource in resources:
        measure = ""
        if resource == "water" or resource == "milk":
            measure = "ml"
        elif resource == "coffee":
            measure = "g"
        print(f"{resource.title()}: {resources[resource]}{measure}")
    print(f"Money: ${money}")


def check_resources(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarter?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def is_transaction_successful(payment, cost):
    if payment >= cost:
        global money
        money += cost
        change = round(payment - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True

    print("Sorry, that's not enough money. Money refunded")
    return False


def make_coffee(drink_name, ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    print(f"Here is your {drink_name} ☕️")


def serve_coffee():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        return
    elif order == "report":
        print_report()
    elif order not in MENU:
        print("Enter a valid option (espresso/latte/cappuccino).")
    else:
        drink = MENU[order]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
    serve_coffee()


serve_coffee()
