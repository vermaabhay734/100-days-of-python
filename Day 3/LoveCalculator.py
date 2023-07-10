print("Welcome to the Love Calculator. ")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

full_name = (name1 + name2).lower()

t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")

true = t + r + u + e

l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
# print(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, You go together like coke and mentoes.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, You are alright together.")
else: 
    print(f"You love score is {love_score}")
