# match_case_calculator.py

# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match-case to perform the selected operation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation selected.")
