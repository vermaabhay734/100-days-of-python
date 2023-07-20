import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (user >= 3 or user < 0):
    print("You must type valid number!")
else:
    print(game_images[user])

    comp = random.randint(0, 2)
    print("Computer choose:")
    print(game_images[comp])


    if user == 0 and comp == 2:
        print("You win!")
    elif user == 2 and comp == 0:
        print("You Lose!")
    elif (comp < user):
        print ("You Win!")
    elif (comp > user):
        print ("You Lose!")
    elif (user == comp):
        print ("Draw!")
