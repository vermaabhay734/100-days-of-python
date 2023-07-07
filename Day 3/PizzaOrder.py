print("Welcome to Python Pizza!")
Size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0;

if Size == "S": 
    bill += 150
elif Size == "M":
    bill += 200
elif Size == "L":
    bill += 250
else:
    print("Please enter correct input! ")

if add_pepperoni == "Y":
    if Size == "S":
        bill += 20
    else:
        bill += 30
        
if extra_cheese == "Y":
    bill += 10

print(f"your final bill is : {bill}")