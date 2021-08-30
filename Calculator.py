# Functions for the operators

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2


# Store the functions in a dict

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

#  Take Input
num1 = float(input("Whats the first number? "))


# loop through the dict to select symbol
for symbol in operations:
    print(symbol)

operations_symbol = input("Pick an operator from above")

num2 = float(input("Whats the second number? "))

calculation_function = operations[operations_symbol]

answer = calculation_function(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")
print(f"{num1} {operations_symbol} {num2} = {answer}")

