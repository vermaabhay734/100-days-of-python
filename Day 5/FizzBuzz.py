# Rules of fizz buzz challenge:
# 1. program should print each number from 1 to 100 in turn, 
# 2. when the number is divisible by 3 then instead of printing the number, print "Fizz"
# 2. when the number is divisible by 5 then instead of printing the number, print "Buzz"
# 2. when the number is divisible by both 3 & 5 then instead of printing the number, print "FizzBuzz"

print("Welcome to the fizz buzz challenge")

for i in range(1, 100):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)