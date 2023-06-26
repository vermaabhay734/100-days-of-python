#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill?"))

final_bill = round(((bill + (bill * tip / 100)) / people), 2)
result = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${result}")

# Welcome to the Tip Calculator.
# What was the total bill? $15243
# What percentage tip would you like to give? 10, 12, or 15? 20
# How many people to split the bill?7
# Each person should pay: $2613.09

