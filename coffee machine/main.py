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

choice = input("“What would you like? (espresso/latte/cappuccino): ")

if choice == "espresso":
    if resources["water"] >=MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        quarters = int(input("How many quarters: "))* 0.25
        dimes = int(input("How many dimes: "))* 0.10
        nickles = int(input("How many nickles: "))* 0.05
        pennies = int(input("How many pennies: "))* 0.01
        total = quarters + dimes + nickles + pennies
        if total >= MENU["espresso"]["cost"]:
            change = round(total - MENU["espresso"]["cost"],2)
            print(f"Here is ${change} in change.")
            print("Here is your espresso ☕️. Enjoy!")
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        else:
            print("Sorry that's not enough money. Money refunded.")

elif choice == "cappuccino":
    if resources["water"] >=MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
        quarters = int(input("How many quarters: "))* 0.25
        dimes = int(input("How many dimes: "))* 0.10
        nickles = int(input("How many nickles: "))* 0.05
        pennies = int(input("How many pennies: "))* 0.01
        total = quarters + dimes + nickles + pennies
        if total >= MENU["cappuccino"]["cost"]:
            change = round(total - MENU["cappuccino"]["cost"],2)
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino ☕️. Enjoy!")
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        else:
            print("Sorry that's not enough money. Money refunded.")

        
