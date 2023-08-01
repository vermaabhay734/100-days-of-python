def prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime is True:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is not a Prime Number.")

number = int(input("Enter the number: "))
prime(number)