from dictionary import MENU
from dictionary import resources

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Machine turning off...")
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{resources['money']}")

    elif choice in MENU:
        resources_sufficient = True
        recipe = MENU[choice]["ingredients"]
        if recipe["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            resources_sufficient = False
            continue
        if recipe.get("milk", 0) > resources["milk"]:
            print("Sorry there is not enough milk.")
            resources_sufficient = False
            continue
        if recipe["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            resources_sufficient = False
            continue

        if resources_sufficient:
            print("Please insert coins.")
            try:
                ten_rupees = int(input("How many ₹10 notes/coins?: "))
                five_rupees = int(input("How many ₹5 notes/coins?: "))
                two_rupees = int(input("How many ₹2 coins?: "))
                one_rupee = int(input("How many ₹1 coins?: "))

                if ten_rupees < 0 or five_rupees < 0 or two_rupees < 0 or one_rupee < 0:
                    print("Coin/note amounts cannot be negative.")
                    continue

                total = (ten_rupees * 10) + (five_rupees * 5) + (two_rupees * 2) + (one_rupee * 1)

            except ValueError:
                print("Invalid input. Please enter numbers. ")
                continue

            cost = MENU[choice]["cost"]
            if total < cost:
                print("Sorry that's not enough money. Money refunded.")
                continue
            elif total >= cost:
                resources["money"] += cost
                change = total - cost
                if change == 0:
                    print("No change")
                else:
                    change = round(change, 2)
                    print(f"Here is ₹{change} in change.")

                resources["water"] -= recipe["water"]
                resources["milk"] -= recipe.get("milk", 0)
                resources["coffee"] -= recipe["coffee"]

                print(f"Here is your {choice.capitalize()}☕. Enjoy!")

    else:
        print("Invalid choice. Please try again.")
