#MPH to MPS converter

print("\nWelcome to our temperature conversion converter!")

temp = float(input("\nWhat is the temperature in degree Fahrenheit? "))

Fahr = round(temp,2)
Kelvin = (Fahr + 459.67)*5/9
Kelvin = round(Kelvin, 2)
Celsius = (Fahr - 32)/1.8000
Celsius = round(Celsius, 2)

print("Fahrenheit: " + str(Fahr))
print("Kelvin: " + str(Kelvin))
print("Celsius: " + str(Celsius))
