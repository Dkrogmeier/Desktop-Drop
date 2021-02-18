import math

print("Welcome to our multiplication table App!")

name = input("Whats your name? ").title()
print("Hi " + name)


num = float(input("Now pick a number: "))

print("\nMultiplication table for " + str(num))
print("\n\t 1.0**" + str(num) + " = " + str(round((num*1.0),4))+ "\n\t 2.0**" + str(num) + " = " + str(round((num*2.0),4))+
      "\n\t 3.0**" + str(num) + " = " + str(round((num*3.0),4))+ "\n\t 4.0**" + str(num) + " = " + str(round((num*4.0),4))+
      "\n\t 5.0**" + str(num) + " = " + str(round((num*5.0),4))+ "\n\t 6.0**" + str(num) + " = " + str(round((num*6.0),4))+
      "\n\t 7.0**" + str(num) + " = " + str(round((num*7.0),4))+ "\n\t 8.0**" + str(num) + " = " + str(round((num*8.0),4))+
      "\n\t 9.0**" + str(num) + " = " + str(round((num*9.0),4)))

print("\nExponent table for " + str(num))
print("\n\t 1.0**" + str(num) + " = " + str(round((num**1.0),4))+ "\n\t 2.0**" + str(num) + " = " + str(round((num**2.0),4))+
      "\n\t 3.0**" + str(num) + " = " + str(round((num**3.0),4))+ "\n\t 4.0**" + str(num) + " = " + str(round((num**4.0),4))+
      "\n\t 5.0**" + str(num) + " = " + str(round((num**5.0),4))+ "\n\t 6.0**" + str(num) + " = " + str(round((num**6.0),4))+
      "\n\t 7.0**" + str(num) + " = " + str(round((num**7.0),4))+ "\n\t 8.0**" + str(num) + " = " + str(round((num**8.0),4))+
      "\n\t 9.0**" + str(num) + " = " + str(round((num**9.0),4)))

print(name)
print("\t" + name.lower())
print("\t\t" + name.title())
print("\t\t\t" + name.upper())

