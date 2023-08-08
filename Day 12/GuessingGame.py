import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def art():
    logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
    print(logo)

# function to check user guess against actual answer.
def check_answer(guess, answer, turns):
    """Check answer against guess, Returns the number of turns remaining"""
    if guess == answer:
        print(f"You got it! The answer is {answer}.")
    elif guess > answer:
        print("Too High!")
        return turns - 1
    else:
        print("Too Low!")
        return turns - 1

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    art()
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    answer = random.randint(1,100)
    print(f"Answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You've run out of guesses, you lose!")
            return

game()