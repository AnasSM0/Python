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
}

quarters = 0 #0.25
dimes = 0 #0.10
nickles = 0 #0.05
pennies = 0 #0.01
total = 0

while True:
    choice = input("\n“What would you like? (espresso/latte/cappuccino/report/off): ")

    if choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, not enough water to make espresso.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee to make espresso.")
        else:
            quarters = int(input("How many quarters: ")) * 0.25
            dimes = int(input("How many dimes: ")) * 0.10
            nickles = int(input("How many nickles: ")) * 0.05
            pennies = int(input("How many pennies: ")) * 0.01
            total = quarters + dimes + nickles + pennies
            if total >= MENU["espresso"]["cost"]:
                change = round(total - MENU["espresso"]["cost"], 2)
                print(f"Here is ${change} in change.")
                print("Here is your espresso ☕️. Enjoy!")
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    if choice == "cappuccino":
        missing_resource = False
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, not enough water to make cappuccino.")
            missing_resource = True
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, not enough milk to make cappuccino.")
            missing_resource = True
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee to make cappuccino.")
            missing_resource = True
        if not missing_resource:
            quarters = int(input("How many quarters: ")) * 0.25
            dimes = int(input("How many dimes: ")) * 0.10
            nickles = int(input("How many nickles: ")) * 0.05
            pennies = int(input("How many pennies: ")) * 0.01
            total = quarters + dimes + nickles + pennies
            if total >= MENU["cappuccino"]["cost"]:
                change = round(total - MENU["cappuccino"]["cost"], 2)
                print(f"Here is ${change} in change.")
                print("Here is your cappuccino ☕️. Enjoy!")
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    if choice == "latte":
        missing_resource = False
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, not enough water to make latte.")
            missing_resource = True
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, not enough milk to make latte.")
            missing_resource = True
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee to make latte.")
            missing_resource = True
        if not missing_resource:
            quarters = int(input("How many quarters: ")) * 0.25
            dimes = int(input("How many dimes: ")) * 0.10
            nickles = int(input("How many nickles: ")) * 0.05
            pennies = int(input("How many pennies: ")) * 0.01
            total = quarters + dimes + nickles + pennies
            if total >= MENU["latte"]["cost"]:
                change = round(total - MENU["latte"]["cost"], 2)
                print(f"Here is ${change} in change.")
                print("Here is your latte ☕️. Enjoy!")
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            else:
                print("Sorry that's not enough money. Money refunded.")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${total}")

    if choice == "off":
        print("Turning off the coffee machine.")
        exit()

    if choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Invalid option. Please enter espresso, latte, cappuccino, report, or off.")