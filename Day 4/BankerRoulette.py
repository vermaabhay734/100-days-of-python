import random

print("Welcome to the Banker Roulette.")
name_string = input("Please enter the name of all the member separated by comma. ")
names = name_string.split(", ")

num_item = len(names)
random_choice = random.randint(0,num_item-1)
people_name = names[random_choice]

#people_name = random.choice(names)
print(f"{people_name} is going to buy the meal today.")