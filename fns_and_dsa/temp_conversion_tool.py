# -------- Global Conversion Factors --------
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# -------- Conversion Functions --------
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# -------- Main User Interaction --------
def main():
    print("Temperature Conversion Tool")
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

if __name__ == "__main__":
    main()
