# Conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

try:
    temperature = float(input("Enter the temperature to convert: "))
except:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

case = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if case == 'f':
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
elif case == 'c':
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
else:
    print("Invalid unit.")
