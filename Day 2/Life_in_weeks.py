age = input("What is your current age? ")

#Write your code below this line 👇

days = 365*(90 - int(age))
months = 12*(90-int(age))
weeks = (90-int(age))*52

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
