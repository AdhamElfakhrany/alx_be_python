def safe_divide(numerator, denominator):

    try:
        result = f"The result of the division is {float(numerator) / float(denominator)}"
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero."
    except ValueError:
        result = "Error: Please enter numeric values only."
    return result
