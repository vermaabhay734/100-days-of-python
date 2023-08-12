from click import clear
from Game_data import data
from Art import logo, vs
import random

def format_data(account):
    """Takes the account data returns the printable format. """
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right!"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Generate the random account from game data.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}.")
    print(vs)
    print(f"Against B : {format_data(account_b)}.")

    guess = input("Who has more instagram followers? Type 'A' or'B': ").lower()

    a_followers_count = account_a['follower_count']
    b_followers_count = account_b['follower_count']
    is_correct = check_answer(guess, a_followers_count, b_followers_count)
    
    clear()
    print(logo)
    

    if is_correct:
        score += 1
        print(f"You're right! Current score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}")