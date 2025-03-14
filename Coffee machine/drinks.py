Menu={
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 20,
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
    },
    
}

profit=0
resources={
    "water":300,
    "milk":200,
    "coffee":100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough=False
    return is_enough

def process_coins():
    """Returns the total calculated from coins inserted."""
    total=int(input("How many quarters?: "))*0.25
    total+=int(input("How many dimes?: "))*0.10
    total+=int(input("How many nickles?: "))*0.05
    total+=int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        global profit
        print(f"Here is ${change} in change.")
        profit+=drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True


while is_on:
    print("Welcome to the coffee machine!")
    print("Please select a drink from the menu:")
    print("1. Espresso")    
    print("2. Latte")
    print("3. Cappuccino")
    user_choice = input("What would you like? ").lower()
    if user_choice=="off":
        is_on=False
    elif user_choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"profit: ${profit}")
    elif user_choice in Menu:
        drink=Menu[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])
    else:
        print("Currently unavailable...Let us add it to the menu for you soon :)")

