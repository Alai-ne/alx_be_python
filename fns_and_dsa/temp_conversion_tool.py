FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    temp_input = input("Enter a temperature value: ")
    temperature = float(temp_input)
    
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature} degrees Celsius is {converted_temp:.2f} degrees Fahrenheit.")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature} degrees Fahrenheit is {converted_temp:.2f} degrees Celsius.")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
        print("Invalid temperature. Please enter a numeric value.")

