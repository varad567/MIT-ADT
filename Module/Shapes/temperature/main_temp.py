from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius
from temperature import celsius_to_kelvin

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Converted Temperature:", celsius_to_fahrenheit.convert(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Converted Temperature:", fahrenheit_to_celsius.convert(f))

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    print("Converted Temperature:", celsius_to_kelvin.convert(c))

else:
    print("Invalid choice")