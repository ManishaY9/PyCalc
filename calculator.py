def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# def divide(a, b):
#     return a / b if b != 0 else "Error: Division by zero"

# def modulus(a, b):
#     return a % b if b != 0 else "Error: Modulus by zero"
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Modulus by zero"
    
def power(a, b):
    return a ** b

def calculate(a, b, operation):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%': modulus,
        '**': power
    }
    func = operations.get(operation)
    return func(a, b) if func else "Invalid operation"
