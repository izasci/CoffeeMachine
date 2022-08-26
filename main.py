from replit import clear
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}
turn_on_machine = True
water_am = resources["water"]
milk_am = resources["milk"]
coffee_am = resources["coffee"]
money_am = resources["money"]

coins = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}
values = [0.25, 0.1, 0.05, 0.01]


def creating_report(water, milk, coffee, money):
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def check_ingredients(water, milk, coffee, choice, menu):
    if water >= menu[choice]["ingredients"]["water"] and milk >= menu[choice]["ingredients"]["milk"] and coffee >= menu[choice]["ingredients"]["coffee"]:
        return True
    else:
        return False


def missing_ingredients(water, menu, choice, milk, coffee):
    if water < menu[choice]["ingredients"]["water"]:
        print("Sorry. There is not enough water.")
    elif milk < menu[choice]["ingredients"]["milk"]:
        print("Sorry. There is not enough milk.")
    elif coffee > menu[choice]["ingredients"]["coffee"]:
        print("Sorry. There is not enough coffee.")


def collecting_coins(coin, values):
    correct_coins = False
    while not correct_coins:
        for value in coin:
            coin[value] = input(f"How many {value}? ")
            try:
                int(coin[value])
                coin[value] = int(coin[value])
                if coin[value] < 0:
                    correct_coins = False
                else:
                    correct_coins = True
            except ValueError:
                correct_coins = False
    total_amount = 0
    i = 0
    for key in coin:
        total_amount += (coin[key] * values[i])
        i += 1
    return total_amount


while turn_on_machine:
    if water_am < MENU["espresso"]["ingredients"]["water"] or coffee_am < MENU["espresso"]["ingredients"]["coffee"]:
        turn_on_machine = False
        print("Machine will turn off. Insufficient amount of ingredients")
        report = input("Do you want a final report? Type 'report' ")
        if report == "report":
            creating_report(water_am, milk_am, coffee_am, money_am)
    else:
        decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if decision == "off":
            turn_on_machine = False
        elif decision == "report":
            creating_report(water_am, milk_am, coffee_am, money_am)
        elif decision == "espresso" or decision == "latte" or decision == "cappuccino":
            enough_ingredients = check_ingredients(water_am, milk_am, coffee_am, decision, MENU)
            if enough_ingredients:
                payment = MENU[decision]["cost"]
                print(f"It will be ${payment}. Please insert coins.")
                total_coins = collecting_coins(coins, values)
                if total_coins < payment:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    if total_coins > payment:
                        remaining = round(total_coins - payment, 2)
                        print(f"Here is ${remaining} in change.")
                        print(f"Here is your {decision} ☕. Enjoy!")
                    elif total_coins == payment:
                        print(f"Here is your {decision} ☕. Enjoy!")
                    water_am -= MENU[decision]["ingredients"]["water"]
                    milk_am -= MENU[decision]["ingredients"]["milk"]
                    coffee_am -= MENU[decision]["ingredients"]["coffee"]
                    money_am += payment
            else:
                missing_ingredients(water_am, MENU, decision, milk_am, coffee_am)
