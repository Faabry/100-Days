def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide 
}

num1 = int(input("Enter with the first number: "))

for symbol in operations:
    print(symbol)3

op = str(input("Enter with one of the operations above:\n>>>"))
num2 = int(input("Enter with the second number: "))
calculation_function = operations[op]
result = calculation_function(num1, num2)
print(f"{num1} {op} {num2} = {result}")
