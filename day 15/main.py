from data import (MENU, resources)

profit = 0
is_on = True

def cost(choice):
    """ Returns the cost of the drink """
    coffee_choice = choice["cost"]
    return coffee_choice


# TODO 2: Checks if resources are enough
def enough_ingredients(order_ingredients):
    """ Checks if there are engouh ingredients to make the drink """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no {item} enough to this drink.")
            return False
    return True


# TODO 3: Process coins payment
def process_coins():
    """ Multiply the inputs according to its values and return the total """
    print("Please insert coins.")
    total = int(input("How many pennies: ")) * 0.01
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many dimmes: ")) * 0.10
    total += int(input("How many quarters: ")) * 0.25
    return total


# TODO 4: Checks if transition was successful
def transaction(payment, drink_cost):
    """ Checks if the users inserted engouh money to pay for the drink and calculates it's change """
    if payment >= drink_cost:
                change = round(payment - drink_cost)
                print("You bought it. \n" +
                      f"You had ${payment} and the drink is ${drink_cost}\n" + 
                      f"Here is ${change} as change.")
                global profit
                profit += drink_cost
    else:
        print("Sorry that's not enough money\n" +
                f"You paid ${payment}, but the drink is ${drink_cost}\n" +
                "Refunding money ...")
        

# TODO 5: Make coffee
def make_coffee(drink_name, order_ingredients):
    """ Run inside each item from the resouces and ingredients and deduct the value """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {drink_name}")
     

################# MAINLY PROGRAM ###################
while is_on:
    users_choice = str(input("What's your choice?\n" +
                             "1 - Espresso \n" +
                             "2 - Latte \n" +
                             "3 - Cappuccino \n" +
                             ">>>")).lower()
    if users_choice == "off":
        is_on = False
    # TODO 1: Print report
    elif users_choice == "report":
        print(f"Water: {resources['water']}ml\n" +
              f"Milk: {resources['milk']}ml\n" +
              f"Coffee: {resources['coffee']}ml")
    else:
        choice = MENU[users_choice]
        if enough_ingredients(choice["ingredients"]):
            payment = process_coins()
            drink_cost = cost(choice)
            transaction(payment, drink_cost)
            make_coffee(users_choice, choice["ingredients"])
            
print(f"Your bill is ${profit}")
############### END OF THE APPLICATION ##############


