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

Money = 0


def resource():
    """Print the resources that we have"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {Money}$")



def check_resources(order_ingredients):
    """Check if resource is available then Reduce the resource."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry There is not enough {item}.")
            is_enough = False
    return is_enough



def process_coins(user_input):
    """For Calculating money"""
    print("Please insert coins.")
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    user_money = quaters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return user_money


def is_transaction_successfull(money_received, drink_cost):
    """Return true when the payment is accepted, or false if money is insufficient"""
    if user_money > MENU[user_input]['cost']:
        refund = user_money - MENU[user_input]['cost']
        print(f"Here is ${refund} in change.")
        print(f"Here is your {user_input}, Enjoy!")
    else:
        print(f"Sorry thats not enough money, ${user_money} refunded.")


is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        resource()
    else:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            user_money = process_coins(user_input)
            is_transaction_successfull()
