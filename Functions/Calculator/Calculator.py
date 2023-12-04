'''Calculator'''

import os
from art import logo

# Addition
def add(n1, n2):
    '''Adds two numbers.'''
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    '''Subtracts two numbers.'''
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    '''Multiply two numbers.'''
    return n1 * n2

# Division
def divide(n1, n2):
    '''Divide first number by second number.'''
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    '''Main function for calculator. Input not required.'''

    print(logo)

    first_num = float(input("What's the first number?: "))
    exit_loop = False
    while not exit_loop:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")

        second_num = float(input("What's the next number?: "))

        selected_operation = operations[operation_symbol]
        answer = selected_operation(n1=first_num, n2=second_num)

        print(f"{first_num} {operation_symbol} {second_num} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            first_num = answer
        else:
            exit_loop = True
            os.system('clear')
            calculator()

calculator()
