
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Write your code below this line 👇

bmi = round(weight / height ** 2)

if bmi > 35:
    category = "clinically obese"
elif bmi > 30 and bmi < 35:
    category = "obese"
elif bmi > 25 and bmi < 30:
    category = "slightly overweight"
elif bmi > 18.5 and bmi < 25:
    category = "normal weight"
else:
    category = "underweight"

print(f"Your BMI is {bmi}, you are {category}.")