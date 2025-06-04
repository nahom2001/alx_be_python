FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  
    return fahrenheit

def main():
    temp = float(input("Enter the temperature to convert: "))
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if scale == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    elif scale == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    else:
        print("Invalid scale. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
