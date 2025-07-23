# -------- Global Conversion Factors --------
FAHRENHEIT_TO_CELSIUS = lambda f: (f - 32) * 5 / 9
CELSIUS_TO_FAHRENHEIT = lambda c: (c * 9 / 5) + 32

# -------- Conversion Functions --------
def convert_to_celsius(f):
    return FAHRENHEIT_TO_CELSIUS(f)

def convert_to_fahrenheit(c):
    return CELSIUS_TO_FAHRENHEIT(c)

# -------- Main User Interaction --------
def main():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    try:
        choice = int(input("Enter choice (1 or 2): "))
        if choice == 1:
            c = float(input("Enter temperature in Celsius: "))
            f = convert_to_fahrenheit(c)
            print(f"{c}°C = {f:.2f}°F")
        elif choice == 2:
            f = float(input("Enter temperature in Fahrenheit: "))
            c = convert_to_celsius(f)
            print(f"{f}°F = {c:.2f}°C")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter valid numeric input.")

if __name__ == "__main__":
    main()
