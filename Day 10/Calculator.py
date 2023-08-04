import Art

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiplication(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiplication,
    "/" : divide
}

def calculator():
    print(Art.logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operational_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operational_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operational_symbol} {num2} = {answer}")

        if input(f"Type 'y' with continue calculating with {answer}, or type 'n' to start new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
