print("Welcome to the Roller Coster. ")
height = int(input("What is your height in cm? "))
bill = 0

if height>=120: 
    print("You can ride the Roller Coster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 200
        print("Child ticket are Rs 200. ")
    elif age <= 18:
        bill = 500
        print("Youth ticket are Rs 500. ")
    elif age >=45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else :
        bill = 1000
        print("Adult ticket are Rs 1000. ")

    want_photo = input("Photo Price is extra Rs 500, Do you want photo taken? Y or N.")
    if want_photo == "Y" :
        bill += 300
        
    print(f"your total bill is Rs {bill}.")

else : print("Sorry, You have to grow taller before you can ride. ")